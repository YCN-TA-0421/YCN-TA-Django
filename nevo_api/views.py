from django.http import HttpResponse


def index(request):
    return HttpResponse(f"<a href='/api/docs/'>/api/docs/</a>")
