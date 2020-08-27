from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import serializers

class MeetingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingCreate
            # fields = '__all__'
        fields = ['name', 'due_date', 'invite_url']

    
class MeetingInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInput
        fields = '__all__'

class MeetingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingTime
        fields = '__all__'
