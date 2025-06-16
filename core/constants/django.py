
from django.contrib import admin
from django.urls import path,include
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt       
from django.contrib.auth.hashers import make_password,check_password