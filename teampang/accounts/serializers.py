from .models import User#커스텀유저
from rest_framework import serializers
#from django.contrib.auth.models import User




#여기부터 유저 기능
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nickname', 'email', 'password', 'birthdate', 'univ', 'major', 'gender', 'profile_photo')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer): #여기 수정하면 회원가입 해결
    class Meta:
        model = User
        fields = ('id', 'nickname', 'email', 'password', 'birthdate', 'univ', 'major', 'gender', 'profile_photo') #여기 수정하면 회원가입 해결
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['nickname'],
            validated_data['email'],
            validated_data['password'],
            validated_data['birthdate'],
            validated_data['univ'],
            validated_data['major'],
            validated_data['gender'],
            validated_data['profile_photo'],
        )

        return user