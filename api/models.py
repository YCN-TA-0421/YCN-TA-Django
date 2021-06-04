from django.db import models
from .variables import df

PRODUCTGROEP_OMS_CHOICES = [(item, item) for item in sorted(df.Productgroep_oms.unique())]

# Create your models here.
class Food(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    index = models.IntegerField(blank=True, default = -1)
    Product_omschrijving = models.CharField(max_length=100, help_text=f"Choose one of the following: {PRODUCTGROEP_OMS_CHOICES}")
    Productgroep_oms = models.CharField(choices=PRODUCTGROEP_OMS_CHOICES, default='Diversen', max_length=100)
    ENERCC_kcal = models.IntegerField()
    PROT_g = models.FloatField()
    CHO_g = models.FloatField()
    FAT_g = models.FloatField()
