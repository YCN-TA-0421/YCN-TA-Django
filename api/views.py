from django.http.response import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
import json

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer
from .variables import df


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