from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Food, PRODUCTGROEP_OMS_CHOICES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'index', 'Productgroep_oms', 'Product_omschrijving', 'ENERCC_kcal', 'PROT_g', 'CHO_g', 'FAT_g']