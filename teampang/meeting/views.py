from django.shortcuts import render
from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializer import MeetingCreateSerializer, MeetingInputSerializer, MeetingTimeSerializer

class MeetingCreateViewSet(viewsets.ModelViewSet):
    # def post(self, request, *args, **kwargs):
    #     serializer = MeetingCreateSerializer(data=request.data)
    #     if serializer.is_valid():
            
    
    queryset = MeetingCreate.objects.all()
    serializer_class = MeetingCreateSerializer

class MeetingInputViewSet(viewsets.ModelViewSet):
    queryset = MeetingInput.objects.all()
    serializer_class = MeetingInputSerializer

class MeetingTimeViewSet(viewsets.ModelViewSet):
    queryset = MeetingTime.objects.all()
    serializer_class = MeetingTimeSerializer