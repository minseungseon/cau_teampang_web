from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class Plan(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'plans', null = True) #null = True 해도 되나
    name = models.CharField(max_length=30)
    date_range = JSONField()
    confirmed_date = JSONField(null=True, blank = True)
    invite_url = models.URLField(null = True, blank = True)
    
    # class Meta:
    #     ordering = ['confirmed_date']

    def __str__(self):
        return '%s' % (self.name)

class DummyPlan(models.Model): #MeetingDetail로 이름 바꾸기
    connected_plan = models.ForeignKey(Plan, related_name='dummy_plans', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date = JSONField(null = True, blank = True)
    
    # class Meta:
    #     ordering = ['confirmed_date']

    def __str__(self):
        return 'connected_plan: %s, name: %s' % (self.connected_plan, self.name)
