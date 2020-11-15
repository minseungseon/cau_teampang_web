from django.shortcuts import render
from .models import Plan, DummyPlan
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .serializer import PlanSerializer, DummyPlanSerializer
import json

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = DummyPlanSerializer

class DummyPlanViewSet(viewsets.ModelViewSet):
    queryset = DummyPlan.objects.all()
    serializer_class = MeetingInputSerializer