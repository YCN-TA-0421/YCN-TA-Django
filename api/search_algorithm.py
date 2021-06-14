import numpy as np
from .models import Food
from .variables import df

WEIGHTS = (11, 8, 5, 3, 2, 1)  # Weights for matching in the first, second, etc. word of the description
EXACT_MATCH_MULT = 4  # Multiplier for an exact match


def search_by_str(items, input_str):
    """
    Returns a list of scores with a score for every item in items based on how well that item matches with input_str.
    """
    scores = np.zeros(len(items))
    for one_word in input_str.strip().split():
        for index_item, one_item in enumerate(items):
            if isinstance(one_item, str) and one_word.lower() in one_item.lower():
                for index_fragment, fragment in enumerate(one_item.strip().split()):
                    if one_word.lower() == fragment.lower():
                        scores[index_item] += WEIGHTS[index_fragment if index_fragment < len(WEIGHTS) else len(WEIGHTS) -1] * EXACT_MATCH_MULT
                    if one_word.lower() in fragment.lower():
                        scores[index_item] += WEIGHTS[index_fragment if index_fragment < len(WEIGHTS) else len(WEIGHTS) -1]
            scores[index_item] -= len(one_item.strip().split()) if isinstance(one_item, str) else 0
    return scores


def convert_scores_to_indices(scores):
    """
    Converts the scores to the matching indexes if the score is above zero and then sorts them by score, descending.
    """
    return sorted([index for index, one_score in enumerate(scores) if one_score > 0], key=lambda index: scores[index], reverse=True)


def recombine_words(df):
    """
    If the first two words in the Product_omschrijving are in the form of "ui zilver-", the dash is removed, the words swapped and concatenated.
    Any other words are concatenated back onto the new word with spaces as separators.
    Returns a list with an item for every item in the input list, either modified as needed or untouched.
    """
    results = []
    for one_item in df['Product_omschrijving'].values:
        splits = one_item.strip().split()
        if len(splits) > 1 and '-' == splits[1][-1]:
            first_word = splits[1][:-1]+splits[0]
            results.append(' '.join([first_word] + splits[2:]))
        else:
            results.append(one_item)
    return results     


def search_indices(input_str):
    """
    Returns the indices of the best matching items ordered by score, descending.
    """
    indices = convert_scores_to_indices(search_by_str(df['Product_omschrijving'].values, input_str))

    if not indices:
        indices = convert_scores_to_indices(search_by_str(recombine_words(df), input_str))
    
    if not indices:
        indices = convert_scores_to_indices(search_by_str(df['Product_synoniemen'].values, input_str))

    return indices


def search_objects(input_str):
    """
    Returns a list of at most 10 food object that best match the input_str by name, recombined name, or synonym.
    """
    scores = search_by_str(df['Product_omschrijving'].values, input_str)

    if max(scores) <= 0:
        scores = search_by_str(recombine_words(df), input_str)

    if max(scores) <= 0:
        scores = search_by_str(df['Product_synoniemen'].values, input_str)

    return [Food.objects.get(index=index) for index in convert_scores_to_indices(scores)[:10]]