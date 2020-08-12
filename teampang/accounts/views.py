from rest_framework import viewsets, serializers
from django.shortcuts import render
from .models import . #일단 .으로 찍어놓음
from .serializers import . #일단 .으로 찍어놓음
from rest_framework.filters import SearchFilter #일단 검색기능 불러오기 넣어놓았다


# Create your views here.
