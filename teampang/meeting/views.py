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

    @action(detail=True, methods=["GET"])
    def meetingInputs(self, request, pk=None):
        team = self.get_object()    #team은 곧 meetingCreate의 pk값을 의미
        team_input = MeetingInput.objects.filter(team=team)
        serializer = MeetingInputSerializer(team_input, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def meetingInput(self, request, pk=None):
        team = self.get_object()
        data = request.data
        data["team"] = team.id
        serializer = MeetingInputSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=["POST"])
    # 8000/meetingCreate/1/dateMatching/
    def dateMatching(self, request, pk=None):
        team = self.get_object()
        data = request.data #matched_time은 현재까지 null값으로 처리
        data["team"] = team.id
        serializer = MeetingTimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=["patch"])	
    # 8000/meetingCreate/1/change_isOnlyDate/
    def change_isOnlyDate(self, request, pk):	#isOnlyDate값 반전
        instance = self.get_object()	
        instance.isOnlyDate = not instance.isOnlyDate 	
        instance.save()
        serializer = self.get_serializer(instance)	
        return Response(serializer.data)
        
class DummyPlanViewSet(viewsets.ModelViewSet):
    queryset = MeetingInput.objects.all()
    serializer_class = MeetingInputSerializer