from django.shortcuts import render
from .models import Plan, DummyPlan
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .serializer import *
import json

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

#################### page 4 ####################

    @action(detail = True, methods = ["GET"])
    # 현재 일정 개수 넘겨주기 (+이미 날짜가 지났다면 제외하기)
    def getNumberOfPlan(self, request, pk): 
        pass

    @action(detail = True, methods = ["GET"])
    # 팀플 이름과 날짜만 포함된 리스트 데이터 가져오기
    def getTeampList(self, request, pk):
        serializer = MainPagePlanListSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
        
        

#################### page 4-1 ####################
    @action(detail = True, methods = ["POST"])
    # confirmed date 제외하고 생성
    def makeUnconfirmedPlan(self, request, pk):
        pass

#################### page 4-2 ####################
    @action(detail = True, methods = ["GET"])
    # 링크 복사하기
    def copyLink(self, request, pk): 
        pass

    # 카카오톡으로 공유하기
    def shareLinkToKakao(self, request, pk): 
        pass    

#################### page 6-0 ####################
    @action(detail = True, methods = ["PATCH"])
    # 일정 수합하기
    def determinePlan(self, request, pk): 
        pass

#################### page 6-1 ####################
    @action(detail = True, methods = ["PATCH"])
    # 일정 수정하기(팀장 버전/ 팀원 버전?)
    def editPlan(self, request, pk): 
        pass

#################### page 6-6 ####################
    # 카카오톡으로 결정된 날짜 공유하기
    def sharePlanToKakao(self, request, pk): 
        pass    
    
#   @action(detail=True, methods=["GET"])
#   def meetingInputs(self, request, pk=None):
#         team = self.get_object()    #team은 곧 meetingCreate의 pk값을 의미	        team = self.get_object()    #team은 곧 meetingCreate의 pk값을 의미
#         meetingimputs = MeetingInput.objects.filter(team=team)	 
#         serializer = MeetingInputSerializer(meetingimputs, many=True)
#         return Response(serializer.data, status=200)	      



class DummyPlanViewSet(viewsets.ModelViewSet):
    queryset = DummyPlan.objects.all()
    serializer_class = DummyPlanSerializer
