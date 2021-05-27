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

# def macro_nutrients(request):
#     request.

def test_pivot(request):
    x = df.loc[0:5, ['Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']]
    return JsonResponse(json.loads(x.to_json(orient='table')))