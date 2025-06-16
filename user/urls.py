from constants.django import *
from user.views import ListUsers,LoginAPI
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("createUser/",ListUsers.as_view()),
    path("login/",LoginAPI.as_view()),
]
