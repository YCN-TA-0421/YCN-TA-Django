from django.http import HttpResponse
import os
# from dotenv import load_dotenv
# load_dotenv()

def test(request):
    return HttpResponse(f"The azure user is: {os.environ.get('AZURE_Uid')}@{os.environ.get('AZURE_HOST')}")