from django.shortcuts import render
from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .serializer import MeetingCreateSerializer, MeetingInputSerializer, MeetingTimeSerializer
import json

class MeetingCreateViewSet(viewsets.ModelViewSet):
    queryset = MeetingCreate.objects.all()
    serializer_class = MeetingCreateSerializer

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
        data = request.data
        data["team"] = team.id
        serializer = MeetingTimeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=["patch"])
    # 8000/meetingCreate/1/timeMatching/
    def timeMatching(self, request, pk=None):
        team = self.get_object()
        inputs_data = MeetingInput.objects.filter(team=team)
        times_data = MeetingTime.objects.filter(team=team)
        for time_data in times_data:
            time_data.matched_time = "05:30:00"
        team.save()
        serializer = self.get_serializer(team)
        return Response(serializer.data, status=201)

    @action(detail=True, methods=["patch"])
    # 8000/meetingCreate/1/set_F_isOnlyDate/
    def set_F_isOnlyDate(self, request, pk):
        instance = self.get_object()
        instance.isOnlyDate = False 
        self.timeMatching(request, pk)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
       
    #     timetable_sum = [{"00-02":0}, {"02-04":0}, {"04-06":0}, {"06-08":0}, {"08-10":0}, {"10-12":0}, {"12-14":0}, {"14-16":0}, {"18-20":0}, {"20-22":0}, {"22-24":0}]
    #     # for input in team_inputs:
    #     #     json_input = json.load(input)
    #     #     timetable = json_input["timetable"]
    #     #     for i in range(0, len(timetable_sum)):
    #     #         if timetable[i]['18-20'] == 1:
    #     #             timetable_sum[i]['18-20'] += 1
    #     meetingTime = MeetingTime.objects.create()
    #     meetingTime.team = pk
    #     meetingTime.matched_time = timetable_sum
    #     meetingTime.matched_date = null
    
class MeetingInputViewSet(viewsets.ModelViewSet):
    queryset = MeetingInput.objects.all()
    serializer_class = MeetingInputSerializer

class MeetingTimeViewSet(viewsets.ModelViewSet):
    queryset = MeetingTime.objects.all()
    serializer_class = MeetingTimeSerializer