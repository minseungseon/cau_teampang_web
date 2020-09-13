from rest_framework import viewsets, serializers, generics, permissions #3,4번째는 유저+로그인기능
from django.shortcuts import render
from .models import User#커스텀유저
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.filters import SearchFilter #일단 검색기능 불러오기 넣어놓았다
from rest_framework.response import Response#유저기능
from knox.models import AuthToken#유저기능
from django.contrib.auth import login#로그인/아웃 기능
from rest_framework.authtoken.serializers import AuthTokenSerializer#로그인/아웃기능
from knox.views import LoginView as KnoxLoginView#로그인/아웃
from rest_framework.decorators import api_view


'''
class EssayViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all()
    serializer_class = EssaySerializer

    filter_backends = [SearchFilter]#검색기능 추가
    search_fields = ('title', 'body')#가로친건 튜플이라서

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    def get_queryset(self):#필터링
        qs = super().get_queryset()


        if self.request.user.is_authenticated:#만일 요청한 user가 로그인되어있다면
            qs = qs.filter(author = self.request.user)#요청한 user의 글만 보여줌
        else:
            qs = qs.none()

        return qs
'''

#여기부터 유저 기능
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "nickname": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#여기부터 로그인/아웃 기능
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)