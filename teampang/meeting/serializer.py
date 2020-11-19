from .models import Plan, DummyPlan
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

class DummyPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DummyPlan
        fields = '__all__'

class MainPagePlanListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('id', 'name', 'confirmed_date')

class CreateUnconfirmedPlanSerializer(serializers.ModelSerializer):
    name = serializers.JSONField()
    date_range = serializers.JSONField()

    class Meta:
        model = Plan
        fields = ('name', 'date_range')

    def save(self):
        author = serializers.HiddenField(default=serializers.CurrentUserDefault())
        print("hello")

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'