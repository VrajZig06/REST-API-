from core.constants.django import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse("Hello World")