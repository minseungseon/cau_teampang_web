from .models import Plan, DummyPlan
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs) 

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DummyPlanSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = DummyPlan
        fields = '__all__'

class PlanSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(read_only=True)
    invite_url= serializers.URLField(default = "http://127.0.0.1:8000/Plan/"+ str(id) +"/createDummyPlan")
    class Meta:
        model = Plan
        fields = '__all__'