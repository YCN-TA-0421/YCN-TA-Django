from django.http import HttpResponse
import os
# from dotenv import load_dotenv
# load_dotenv()
from . import settings

x = os.environ.get('AZURE_PASSWORD')
if x is not None:
    x = x[0]
def test(request):
    return HttpResponse(f"The azure user is: {os.environ.get('AZURE_USER')}@{os.environ.get('AZURE_HOST')}<br>\
        {os.environ.get('AZURE_NAME')}<br>\
        {os.environ.get('AZURE_USER')}<br>\
        {x}<br>\
        {os.environ.get('AZURE_HOST')}<br>\
        {os.environ.get('AZURE_PORT')}<br>\
        {settings.AZURE_USER}")