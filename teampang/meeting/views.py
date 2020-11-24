from django.shortcuts import render
from .models import Plan, DummyPlan
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import HttpResponse
from .serializer import *
import json

from .permissions import IsAuthorReadOnly

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAuthorReadOnly]

#################### page 4 ####################

    @action(detail = False)
    # 현재 일정 개수 넘겨주기 (+이미 날짜가 지났다면 제외하기)
    # 시리얼라이저 없이 직접 data 넘겨주도록 했음. 프론트에서 planlist 원소 수 세는 방법이 더 효율적일까요?
    def getNumberOfPlan(self, request): 
        # 나의 일정 개수 처리
        num = dict(number_of_plan=request.user.plans.count())
        # 딕셔너리로 넘어간다.... !?
        #json_num = json.dumps(num) # "{\"number_of_plan\": 1}"
        return Response(num, status=202) #"number_of_plan": 1
        
    @action(detail = False, methods = ["GET"])
    # 팀플 이름과 날짜만 포함된 리스트 데이터 가져오기
    def getPlans(self, request):
        plan = request.user.plans.all()
        serializer = PlanSerializer(plan, fields=('name', 'confirmed_date'), many=True) #dynamic serializer fields
        return Response(serializer.data, status=200)
    
    #플랜 삭제는 기본 viewset [delete] localhost/Plan/1 이런식으로 가능함.

#################### page 4-1 ####################

    #plan 생성
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        plan = serializer.save(author=self.request.user) #author의 primary key로 연결
        plan.invite_url = "http://127.0.0.1:8000/Plan/"+ str(plan.id) +"/createDummyPlan/"
        plan.save()
        
#################### page 4-2 ####################

    @action(detail = True, methods = ["GET"])
    # 링크 복사하기
    def getLink(self, request, pk): 
        plan = self.get_object()
        serializer = PlanSerializer(plan, fields=('invite_url',)) #dynamic serializer fields
        return Response(serializer.data, status=200)


#################### page 5 ####################

    @action(detail = True, methods = ["POST"])
    # dummyPlan 작성
    def createDummyPlan(self, request, pk): 
        plan = self.get_object()
        serializer = DummyPlanSerializer(DummyPlan(), fields=('name', 'date'), data = request.data)
        if serializer.is_valid():
            serializer.save(connected_plan=plan)
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


################# page 6-0 ~ 6-2 ################# 

    @action(detail = True, methods = ["GET"]) 
    # 더미플랜들 받기
    def getDummyPlans(self, request, pk): 
        plan = self.get_object() #현재 pk값의 object를 get함. 
        dummy_plans = plan.dummy_plans.all() 
        serializer = DummyPlanSerializer(dummy_plans, many=True) 
        return Response(serializer.data, status=200)
        
    #PlanViewSet에서 구현할 수 있는 방법이 없을까.  
    # 아래 DummyPlanViewset에서 일단 구현을 해줬음.  
    @action(detail = True, methods = ["PATCH"]) 
    # 더미플랜 지우기
    def deleteDummyPlan(self, request, pk): 
        plan = self.get_object()
        #request.data는 front에서 삭제할 dummyPlan의 pk 주어야함
        dummy_plan = plan.dummy_plans.get(pk=request.data) 
        dummy_plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#################### page 6-3 ####################
    @action(detail = True, methods = ["PATCH"]) 
    # 일정 확정 짓기
    def confirmPlanDate(self, request, pk):
        plan = self.get_object()
        serializer = PlanSerializer(plan, fields=('confirmed_date',), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400) 


#################### page 6-4 ####################

    @action(detail = True, methods = ["GET"]) 
    # 카카오톡으로 결정된 날짜 공유할 때 사용할 데이터 전송
    def getPlanConfirmedDate(self, request, pk): 
        plan = self.get_object()
        serializer = PlanSerializer(plan, fields=('name', 'confirmed_date')) #dynamic serializer fields
        return Response(serializer.data, status=200)