
import pandas as pd
import json
from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from pandas.io import api
from rest_framework import HTTP_HEADER_ENCODING, serializers, viewsets, permissions, status
from rest_framework.decorators import api_view
from rest_framework.utils import serializer_helpers
from rest_framework.parsers import JSONParser
from .serializers import UserSerializer, GroupSerializer
from .variables import df
from api.models import Food, PRODUCTGROEP_OMS_CHOICES
from api.serializers import FoodSerializer
from .search_algorithm import search_objects
from .replacement_algorithm import get_replacement, get_replacement_macronutrients

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def five_names(request):
    return JsonResponse(json.loads(df[['Productgroep_oms', 'Product_omschrijving']].head().to_json()))


def dataframe_to_json(df):
    return json.loads(df[['Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']].to_json(orient='table'))


def macro_nutrients_index(request):
    index = request.GET.get('index')
    if not index:
        return HttpResponseBadRequest("Missing index value.")

    try:
        # return JsonResponse(json.loads(df.loc[int(index), ['Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']].to_json(orient='table')))
        return JsonResponse(dataframe_to_json(df.loc[[int(index)]]))
    except ValueError:
        return HttpResponseBadRequest(f"Invalid index '{index}', only integer values are allowed for the index.")
    except KeyError:
        return HttpResponseBadRequest(f"No item found for index {index}.")


def macro_nutrients_name(request):
    name = request.GET.get('name')
    if not name:
        return HttpResponseBadRequest("Missing name value.")

    return_value = df[df['Product_omschrijving'] == name]
    if len(return_value):
        return JsonResponse(dataframe_to_json(return_value))
    else:
        return HttpResponseBadRequest(f"Invalid product name '{name}'. This type of request requires exact names. Use search= to search for the closest product(s) or go to macro-nutrients/ without any parameters for instructions.")


def macro_nutrients_search(request):
    search = request.GET.get('search')
    if not search:
        return HttpResponseBadRequest("Missing search value.")

    # TODO: write search algorithm
    # TODO: implement limit

    print(request.GET)
    print('')
    return HttpResponse(repr(request.GET) + ' ' + str('limit' in request.GET))


def macro_nutrients(request):
    if request.method == 'GET':
        if 'index' in request.GET.keys():
            return macro_nutrients_index(request)
        elif 'name' in request.GET.keys():
            return macro_nutrients_name(request)
        elif 'search' in request.GET.keys():
            return macro_nutrients_search(request)
        else:
            return HttpResponse("Welcome to the macro nutrients api.<br>\
                                 To request any data start by adding a ? after the / in the url.<br>\
                                 To request by index add index= followed by the index you want to retrieve.<br>\
                                 If you wish to search by product name add name= followed by the exact product name.<br>\
                                 To search for similar product add search= followed by the (partial) product name. By default the 5 closest matches will be returned, alternatively, add &limit= followed by the maximum number of matches you want.<br>\
                                 <br>Examples:<br>\
                                 macro-nutrients/?index=5<br>\
                                 macro-nutrients/?name=Aardappelen rauw<br>\
                                 macro-nutrients/?search=aardappel<br>\
                                 macro-nutrients/?search=aardappel&limit=3")
    elif request.method == 'POST':
        print('API POST request on macro_nutrients')
        return HttpResponse("Not implemented (yet)")


def test_pivot(request):
    x = df.loc[0:5, ['Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']]
    return JsonResponse(json.loads(x.to_json(orient='table')))


@api_view(['GET'])
def food_groups(request):
    """
    get:
    Returns the list of all food-groups available.
    """
    if request.method == 'GET':
        # food_groups = {index: group[0]
        #                for index, group in enumerate(PRODUCTGROEP_OMS_CHOICES)}
        # return JsonResponse(food_groups)
        return JsonResponse([group[0] for group in PRODUCTGROEP_OMS_CHOICES], safe=False)


# @api_view(['GET', 'POST'])
@api_view(['GET'])
def food_list(request):
    """
    get:
    Returns a list of all food items.

    post:
    Adds a new food item if the data given is valid.
    """
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def food_detail(request, pk):
    """
    get:
    Returns the food object corrosponding to the input id.

    put:
    Edits the food object corrosponding to the input id if the data given is valid.

    delete:
    Deletes the food object corrosponding to the input id.
    """
    try:
        pk = int(pk)
        food = Food.objects.get(pk=pk)
    except ValueError:
        try:
            food = Food.objects.get(Product_omschrijving=pk)
        except Food.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    except Food.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        serializer = FoodSerializer(food)
        food.delete()
        return JsonResponse(serializer.data)


@api_view(['GET'])
def food_detail_index(request, index):
    """
    get:
    Returns a food object based on the index field.
    """
    try:
        food = Food.objects.get(index=index)
    except Food.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return JsonResponse(serializer.data)


@api_view(['GET'])
def food_detail_name(request, name):
    """
    get:
    Returns a food object based on the Product_omschrijving field.
    """
    try:
        food = Food.objects.get(Product_omschrijving=name)
    except Food.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return JsonResponse(serializer.data)


@api_view(['GET'])
def food_detail_search(request, input_str):
    """
    get:
    Returns a list of the food objects that match the input_str best by name, with a maximum of 10 objects.
    Takes in account the name, the reconstructed name (ui zilver- is also seen as zilverui) or synonym.
    """

    if request.method == 'GET':
        # indices = search_indices(input_str)
        foods = search_objects(input_str)
        if foods:
            serializer = FoodSerializer(foods, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def food_replacement(request, pk, diet=None):
    """
    get:
    Returns the 10 products that best match the food object whose ID was given as input.
    Takes an optional argument diet for when you want to specify a certain diet to choose from. By default any food object is allowed.
    The options are: regular diet, vegetarian diet, vegan diet
    """
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        foods = get_replacement(food, diet)
        if isinstance(foods, int):
            if foods == -1:
                return HttpResponse(f"Invalid diet: {diet}", status.HTTP_400_BAD_REQUEST)
            elif food == -2:
                return HttpResponse(f"Invalid food index (required to be between 0 and {len(df) - 1}): {food.index}", status.HTTP_400_BAD_REQUEST)
            else:
                return HttpResponse(f"Unexpected error code, could not return useful information.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        serializer = FoodSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def food_replacement_macronutrients(request, protein, carbohydrates, fat, diet=None):
    """
    get:
    Returns the 10 products that best match the (hypothetical) food with given amounts of protein, carbohydrates and fat in grams.
    Takes an optional argument diet for when you want to specify a certain diet to choose from. By default any food object is allowed.
    The options are: regular diet, vegetarian diet, vegan diet
    """
    if request.method == 'GET':
        foods = get_replacement_macronutrients(protein, carbohydrates, fat, diet)
        if isinstance(foods, int) and foods == -1:
            return HttpResponse(f"Invalid diet: {diet}", status.HTTP_400_BAD_REQUEST)
        serializer = FoodSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)


# def load_database(request):
#     all_data = json.loads(df[['Product_omschrijving', 'Productgroep_oms', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']].to_json(orient='table'))
#     errors = {}
#     for index, data in enumerate(all_data['data']):
#         serializer = FoodSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#         else:
#             errors[f'{index}'] = 'Invalid data'
#     JsonResponse(errors, status=status.HTTP_200_OK)
