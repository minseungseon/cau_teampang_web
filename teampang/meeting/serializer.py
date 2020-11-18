from .models import Plan, DummyPlan
from rest_framework import serializers

class DummyPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = DummyPlan
        fields = '__all__'

class MainPagePlanListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ('name', 'confirmed_date')

class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'