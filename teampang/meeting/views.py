from django.shortcuts import render
from .models import MeetingResult, MeetingInput
from rest_framework import viewsets
from .serializer import MeetingResultSerializer, MeetingInputSerializer

class MeetingResultViewSet(viewsets.ModelViewSet):
    queryset = MeetingResult.objects.all()
    serializer_class = MeetingResultSerializer

class MeetingInputViewSet(viewsets.ModelViewSet):
    queryset = MeetingInput.objects.all()
    serializer_class = MeetingInputSerializer