from constants.django import *
from user.views import createUser

urlpatterns = [
    path("createUser/",createUser),
]
