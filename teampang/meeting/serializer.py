from .models import MeetingResult, MeetingInput
from rest_framework import serializers

class MeetingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingResult
            # fields = '__all__'
        fields = ['name', 'matched_date', 'matched_time', 'due_date', 'invite_url']

    
class MeetingInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingInput
        fields = '__all__'