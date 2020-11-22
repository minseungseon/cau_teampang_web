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
    # permission_classes = [IsAuthenticated] 나중에 권한 있을 때만 사용가능하게도 해줘야l함.

    #author의 primary key로 연결
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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
    def getPlanList(self, request):
        plan = request.user.plans.all()
        serializer = PlanSerializer(plan, fields=('name', 'confirmed_date'), many=True) #dynamic serializer fields
        return Response(serializer.data, status=200)

#################### page 4-1 ####################
    # @action(detail = True, methods = ["POST"])
    # # confirmed date 제외하고 생성
    # def makeUnconfirmedPlan(self, request, pk):
    #     # user = serializers.HiddenField(
    #     #    default=serializers.CurrentUserDefault(),
    #     # )   
    #     #permission_classes = (IsAuthenticated,)
    #     #serializer = CreateUnconfirmedPlanSerializer(data=request.data)
    #     serializer = PlanSerializer(fields=(name, ))
    #     print(CurrentUserDefault())
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     else:
    #         return Response(serializer.errors, status=400)

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
    # dummyPlan들 넘기기
    def determinePlan(self, request, pk): 
        pass

#################### page 6-1 ####################
    @action(detail = True, methods = ["PATCH"])
    # 일정 수정하기(팀장 버전)
    def editPlan(self, request, pk): 
        pass

#################### page 6-6 ####################
    # 카카오톡으로 결정된 날짜 공유하기
    def sharePlanToKakao(self, request, pk): 
        pass

    @action(detail = True, methods = ["POST"])
    # dummyPlan 작성
    def createDummyPlan(self, request, pk): 
        print("Hello")
        serializer = DummyPlanSerializer(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    
#   @action(detail=True, methods=["GET"])
#   def meetingInputs(self, request, pk=None):
#         team = self.get_object()    #team은 곧 meetingCreate의 pk값을 의미	        team = self.get_object()    #team은 곧 meetingCreate의 pk값을 의미
#         meetingimputs = MeetingInput.objects.filter(team=team)	 
#         serializer = MeetingInputSerializer(meetingimputs, many=True)
#         return Response(serializer.data, status=200)