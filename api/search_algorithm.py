import numpy as np
from datetime import date, datetime

from numpy.core.numeric import indices
from .models import Food
from .variables import df

WEIGHTS = (11, 8, 5, 3, 2, 1)
EXACT_MATCH_MULT = 4
NUM_WORDS_MULT = 1


def search_by_str(items, input_str):
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
    return sorted([index for index, one_score in enumerate(scores) if one_score > 0], key=lambda index: scores[index], reverse=True)


def convert_scores_to_result(df, scores):
    return df.loc[sorted([index for index, one_score in enumerate(scores) if one_score > 0], key=lambda index: scores[index], reverse=True)], sorted([one_score for one_score in scores if one_score > 0], reverse=True)


def search_by_str_from_df(df, column, input_str):
    scores = search_by_str(df[column].values, input_str)
    return convert_scores_to_result(df, scores)


def recombine_words(df):
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
    indices = convert_scores_to_indices(search_by_str(df['Product_omschrijving'].values, input_str))

    if not indices:
        indices = convert_scores_to_indices(search_by_str(recombine_words(df), input_str))
    
    if not indices:
        indices = convert_scores_to_indices(search_by_str(df['Product_synoniemen'].values, input_str))

    return indices


def search_objects(input_str):
    scores = search_by_str(df['Product_omschrijving'].values, input_str)

    if max(scores) <= 0:
        scores = search_by_str(recombine_words(df), input_str)

    if max(scores) <= 0:
        scores = search_by_str(df['Product_synoniemen'].values, input_str)

    return [Food.objects.get(index=index) for index in convert_scores_to_indices(scores)[:10]]


def search_formatted(input_str, max_nr_items=None, columns=None, return_scores=False):
    df_result, scores = search_by_str_from_df(df, 'Product_omschrijving', input_str)

    if len(df_result) == 0:
        scores = search_by_str(recombine_words(df), input_str)
        df_result, scores = convert_scores_to_result(df, scores)

    if len(df_result) == 0:
        df_result, scores = search_by_str_from_df(df, 'Product_synoniemen', input_str)

    if columns is None:
        df_output = df_result.iloc[:max_nr_items].copy()
    else:
        df_output = df_result.iloc[:max_nr_items][columns].copy()

    if return_scores:
        df_output['Score'] = scores[:max_nr_items]
    
    return df_output