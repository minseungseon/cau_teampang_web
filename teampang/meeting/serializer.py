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
    team_input = MeetingInputSerializer(many=True)
    team_time = MeetingTimeSerializer(many=True)

    class Meta:
        model = MeetingCreate
            # fields = '__all__'
        fields = ['name', 'due_date', 'invite_url', 'team_input','team_time']

    def create(self, validated_data):
        inputs_data = validated_data.pop('team_input')
        times_data = validated_data.pop('team_time')
        team = MeetingCreate.objects.create(**validated_data)
        for input_data in inputs_data:
                MeetingInput.objects.create(team=team, **input_data)
        for time_data in times_data:
                MeetingInput.objects.create(team=team, **times_data)

        return team


