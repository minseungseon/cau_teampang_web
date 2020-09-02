from .models import Essay, Photo, Account, Profile, User#커스텀유저
from rest_framework import serializers
#from django.contrib.auth.models import User

class EssaySerializer(serializers.ModelSerializer): #User 모델 보여주기

    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'body', 'author_name')

class PhotoSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Photo
        fields = ('pk', 'author_name', 'image')

class ProfileSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.username')
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Profile
        fields = ('pk')



#여기부터 유저 기능
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer): #여기 수정하면 회원가입 해결
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'nickname') #여기 수정하면 회원가입 해결
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user =User.objects.create_user(validated_data['nickname'], validated_data['email'], validated_data['password'])

        return user




