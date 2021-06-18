from django.http import HttpResponse

import dotenv
import os

dotenv.load_dotenv()


def index(request):
    return HttpResponse(f"{os.environ.get('FREEK_AZURE_NAME')} {os.environ.get('FREEK_AZURE_USER')[:3]} {os.environ.get('FREEK_AZURE_PASSWORD')[:3]} {os.environ.get('FREEK_AZURE_HOST')[:3]} {os.environ.get('FREEK_AZURE_PORT')[:3]} <a href='/api/docs/'>/api/docs/</a>")
