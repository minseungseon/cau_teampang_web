from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class Plan(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date_range = JSONField(null=True)
    confirmed_date = models.DateTimeField(null=True)
    invite_url = models.URLField()
    member_list = JSONField(null=True)
    
    def __str__(self):
        return '%s' % (self.name)

class DummyPlan(models.Model): #MeetingDetail로 이름 바꾸기
    connected_plan = models.ForeignKey(Plan, related_name='DummyPlan', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date = JSONField(null=True)
    
    def __str__(self):
        return 'connected_plan = %s, name = %s' % (self.connected_plan, self.name)