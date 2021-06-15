import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import StandardScaler
from datetime import datetime

import api.variables
from .models import Food

df = api.variables.df.copy()
df = df.fillna(0)  # The added line

# Summing up the values for the three difference fatty acids that make up Omega-3
# adding up ALA, EPA and DHA
df['omega3_g'] = df['F18_3CN3_g'] + df['F20_5CN3_g'] + df['F22_6CN3_g']

# Scaling the data
scaler = StandardScaler()
numerical_columns = list(df.columns)[11:]  # Skips all columns before ENERGCJ_kJ

# Some of those columns don't have any non-zero values in them, so they are useless
useful_numerical_columns = [col
                            for col in numerical_columns
                            if df[col].std() != 0]

scaled_features = scaler.fit_transform(df[useful_numerical_columns])

# Add all the scaled columns to the main dataframe to reference
for index, one_column in enumerate(useful_numerical_columns):
    df[f"Scaled_{one_column}"] = scaled_features[:, index]

# Blacklists determined per diet type
blacklist = ['Alcoholische dranken', 'Diversen', 'Flesvoeding en preparaten', 'Niet-alcoholische dranken', 'Samengestelde gerechten', 'Kruiden en specerijen']
non_vegetarian = ["Vlees en gevogelte", "Vis", "Vleeswaren", 'Soepen', 'Hartig broodbeleg', 'Hartige snacks en zoutjes', 'Hartige sauzen']
non_vegan = ['Brood', 'Eieren', 'Gebak en koek', 'Graanproducten en bindmiddelen', 'Kaas', 'Melk en melkproducten', 'Suiker, snoep, zoet beleg en zoete sauzen', 'Vetten en oliën', 'Vleesvervangers en zuivelvervangers']

# Cumulatively apply the blacklists
df_regular_diet = df.copy()
for banned in blacklist:
    df_regular_diet = df_regular_diet.drop(
        df[(df.Productgroep_oms == banned)].index
    )

df_vegetarian = df_regular_diet.copy()
for banned in blacklist + non_vegetarian:
    df_vegetarian = df_vegetarian.drop(
        df_regular_diet[(df_regular_diet.Productgroep_oms == banned)].index
    )

df_vegan = df_vegetarian.copy()
for banned in blacklist + non_vegan:
    df_vegan = df_vegan.drop(
        df_vegetarian[(df_vegetarian.Productgroep_oms == banned)].index
    )

def show_most_alike(df_to_select_from, food_to_replace, columns, nr_of_results=10):
    number_of_results = nr_of_results * 2 if nr_of_results * 2 < len(df_to_select_from) else len(df_to_select_from)
    scaled_columns = [f"Scaled_{one_column}"
                      for one_column in columns]
    human_readable_columns = ['Productgroep_oms', 'Product_omschrijving']
    difference_columns = [f"Difference_{one_column}"
                          for one_column in columns]
    columns_extended = human_readable_columns + columns + scaled_columns
    columns_to_display = human_readable_columns + columns + ['Euclidian_distance'] + difference_columns


    df_euclidian = df_to_select_from[columns_extended].copy()

    scaled_values = df_euclidian[scaled_columns].values
    df_euclidian['Euclidian_distance'] = [np.linalg.norm(row)
                                            for row in scaled_values - food_to_replace[scaled_columns].values]
    df_euclidian[difference_columns] = df_euclidian[columns].values - food_to_replace[columns].values

    df_results = pd.DataFrame()
    # Added np.unique() to only show everything with the same Euclidian distance once.
    # As a side-effect this means that if the last of the selected distances is not unique in the whole list 
    # everything with an identical value will still be shown resulting in more records than perhaps expected. This 
    # can be useful as those different food items are equivalent for the analysis. However it might cause issues 
    # if the results would be returned instead of displayed.
    for euclidian_minimum in np.unique(sorted(
        df_euclidian['Euclidian_distance'].values)[:number_of_results]):
        df_results = df_results.append(df_euclidian[df_euclidian['Euclidian_distance'] == euclidian_minimum])
    
    # Return the results, omit the input food if present (it should have a euclidian distance of 0 and be on top)
    if (df_results.iloc[0][human_readable_columns + columns].values == food_to_replace[human_readable_columns + columns].values).all():
        return df_results.iloc[1:nr_of_results+1]
    else:
        return df_results.iloc[:nr_of_results]


def meandivide(y, columns):
    return y[columns] / np.sqrt(np.array([scaler.var_[useful_numerical_columns.index(one_column)]
                                           for one_column in columns]))


def scale_df(y, columns):
    return (y[columns] - np.array([scaler.mean_[useful_numerical_columns.index(one_column)]
                                   for one_column in columns])) / np.sqrt(np.array([scaler.var_[useful_numerical_columns.index(one_column)]
                                                                                    for one_column in columns]))


def meandivide_np(y, columns):
    return y / np.sqrt(np.array([scaler.var_[useful_numerical_columns.index(one_column)]
                                           for one_column in columns]))


def scale_np(y, columns):
    return (y - np.array([scaler.mean_[useful_numerical_columns.index(one_column)]
                         for one_column in columns])) / np.sqrt(np.array([scaler.var_[useful_numerical_columns.index(one_column)]
                                                                          for one_column in columns]))


def grams(to_replace, first_replace, columns):
    gramslist = []
    
    ## Plus
    old_score = np.linalg.norm(meandivide_np(to_replace[columns].values - first_replace[columns].values, columns))
    var = 1 + 0.01
    new_score = np.linalg.norm(meandivide_np(to_replace[columns].values - var * first_replace[columns].values, columns))
    if new_score >= old_score:
        var = 1
    while new_score < old_score and var < 100:
        old_score = new_score
        var += .01
        new_score = np.linalg.norm(meandivide_np(to_replace[columns].values - var * first_replace[columns].values, columns))
    gramslist.append((var,old_score))

    ## Min
    old_score = np.linalg.norm(meandivide_np(to_replace[columns].values - first_replace[columns].values, columns))
    var = 1 - 0.01
    new_score = np.linalg.norm(meandivide_np(to_replace[columns].values - var * first_replace[columns].values, columns))
    if new_score >= old_score:
        var = 1
    while new_score < old_score and var > 0:
        old_score = new_score
        var -= .01
        new_score = np.linalg.norm(meandivide_np(to_replace[columns].values - var * first_replace[columns].values, columns))
    gramslist.append((var,old_score))
    
    if gramslist[0][1] < gramslist[1][1]:
        return gramslist[0][0]
    else:
        return gramslist[1][0]


def euclidian(df_to_select_from, food_to_replace, columns):
    most_alike = show_most_alike(df_to_select_from, food_to_replace, columns)
    grams_most_alike = grams(food_to_replace, most_alike, columns)
    most_alike['Amount_g'] = 100 * grams_most_alike

    return most_alike[['Productgroep_oms', 'Product_omschrijving'] + columns + ['Amount_g']]


def presentable_euclidian(food_to_replace, columns):
    human_readable_columns = ['Productgroep_oms', 'Product_omschrijving']
    df_results = food_to_replace[human_readable_columns + columns].copy()
    df_results['Amount_g'] = food_to_replace['Hoeveelheid'].values
    
    df_results = df_results.append(euclidian(df, food_to_replace, columns))
    df_results = df_results.append(euclidian(df_vegetarian, food_to_replace, columns))
    df_results = df_results.append(euclidian(df_vegan, food_to_replace, columns))
    df_results['Type'] = ['Input', 'Regular diet replacement', 'Vegetarian replacement', 'Vegan replacement']
    df_results = df_results[[df_results.columns[-1]] + list(df_results.columns[:-1])]
    
    return df_results


def get_replacement(food_to_replace, diet):
    """
    Expects a Food object to replace. If the index of said food object is between 0 and the length of df then a replacement will be searched.
     Otherwise None will be returned.
    Expects a string that is either 'regular diet', 'vegetarian diet', or 'vegan diet'. If none is given the whole dataset is used.
     If the argument doesn't conform to one of those four options the function returns None.
    """
    if not (0 <= food_to_replace.index < len(df)):
        return
    else:
        index = food_to_replace.index
    
    if diet == 'regular diet':
        df_to_select_from = df_regular_diet
    elif diet == 'vegetarian diet':
        df_to_select_from = df_vegetarian
    elif diet == 'vegan diet':
        df_to_select_from = df_vegan
    elif diet is None:
        df_to_select_from = df
    else:
        return

    results = show_most_alike(df_to_select_from, df.loc[[index]], ['PROT_g', 'CHO_g', 'FAT_g'])

    foods = []
    for index in results.index:
        foods.append(Food.objects.get(index=index))
    
    return foods