from django.shortcuts import render
from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import MeetingCreateSerializer, MeetingInputSerializer, MeetingTimeSerializer

class MeetingCreateViewSet(viewsets.ModelViewSet):
    queryset = MeetingCreate.objects.all()
    serializer_class = MeetingCreateSerializer

    # @action(detail=True, methods=['put'])
    # def timeMatch_algorithm(self, request, pk): #pk = team고유값
    #     instance = self.get_object()
    #     serializer = self.get_serializer()
    #     serializer.team_time = MeetingTimeSerializer()
    #     matched_time = [{"00-02":0}, {"02-04":0}, {"04-06":0}, {"06-08":0}, {"08-10":0}, {"10-12":0}, {"12-14":0}, {"14-16":0}, {"18-20":0}, {"20-22":0}, {"22-24":0}]
        
    #     return Response(selializer.data)
    

class MeetingInputViewSet(viewsets.ModelViewSet):
    queryset = MeetingInput.objects.all()
    serializer_class = MeetingInputSerializer

class MeetingTimeViewSet(viewsets.ModelViewSet):
    queryset = MeetingTime.objects.all()
    serializer_class = MeetingTimeSerializer