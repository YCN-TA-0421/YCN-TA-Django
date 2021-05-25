from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import pandas as pd
import json

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer


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
    df = pd.read_excel('nevo_online_2019.xlsx')
    return JsonResponse(json.loads(df[['Productgroep_oms', 'Product_omschrijving']].head().to_json()))