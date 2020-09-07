from .models import MeetingCreate, MeetingInput, MeetingTime
from rest_framework import serializers

class MeetingInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeetingInput
        fields = '__all__'

class MeetingTimeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = MeetingTime
        fields = '__all__'

class MeetingCreateSerializer(serializers.ModelSerializer):
    team_input = MeetingInputSerializer(many=True)
    team_time = MeetingTimeSerializer(many=True)

    class Meta:
        model = MeetingCreate
        fields = [
            "id",
            "name",
            "due_date",
            "invite_url",
            "member_list",
            "isOnlyDate",
            "team_input",
            "team_time"
        ]
        
    def create(self, validated_data):
        inputs_data = validated_data.pop('team_input')
        times_data = validated_data.pop('team_time')
        team = MeetingCreate.objects.create(**validated_data)
        for input_data in inputs_data:
                MeetingInput.objects.create(team=team, **input_data)
        for time_data in times_data:
                MeetingTime.objects.create(team=team, **times_data)
        return team

    def update(self, instance, validated_data):
        inputs_data = validated_data.pop('team_input')
        times_data = validated_data.pop('team_time')
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.invite_url = validated_data.get('invite_url', instance.invite_url)
        instance.member_list = validated_data.get('member_list', instance.member_list)
        instance.isOnlyDate = validated_data.get('isOnlyDate', instance.isOnlyDate)
        instance.save()

        keep_times = []
        existing_ids = [t.id for t in instance.team_time.all()]
        for time_data in times_data:
            if "id" in time_data.keys():
                if MeetingTime.objects.filter(pk=time_data["id"]).exists():
                    t = MeetingTime.objects.get(pk=time_data["id"])
                    t.matched_date = time_data.get('matched_date', t.matched_date)
                    t.matched_time = time_data.get('matched_time', t.matched_time)
                    t.save()
                    keep_times.append(t.id)
                else:
                    continue
            else:
                t = MeetingTime.objects.create(**time_data)
                keep_times.append(t.id)
        
        for time_data in instance.team_time.all():
            if time_data.id not in keep_times:
                time_data.delete()

        return instance