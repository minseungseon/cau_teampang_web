from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import serializers

class MeetingInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInput
        fields = '__all__'


class MeetingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingTime
        fields = '__all__'

class MeetingCreateSerializer(serializers.ModelSerializer):
    # details = MeetingInputSerializer(many=True, read_only=True),MeetingTimeSerializer(many=True, read_only=True)
    class Meta:
        model = MeetingCreate
            # fields = '__all__'
        fields = ['name', 'due_date', 'invite_url']



