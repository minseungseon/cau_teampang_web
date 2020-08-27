from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class MeetingResult(models.Model):
    name = models.CharField(max_length=30)
    matched_date = models.DateField()
    matched_time = models.TimeField()
    due_date = models.DateTimeField()
    invite_url = models.URLField()
    member_list = JSONField(null=True) #이후 User , no user로 확장
    # author = models.ForeignKey(User, on_delete=models.CASCADE) #작성자 => 팀장

class MeetingInput(models.Model):
    dummyname = models.CharField(max_length=30)
    timetable = JSONField(null=True)

    
# class MemberList(models.Model):
# 	# authenticated = models. #유저 정보
# 	anonymous = jsonfield.JSONField() #비회원 정보 텍스트
# 	number = models.IntegerField() # 멤버수
#     meetingResult = models.ForeignKey(MeetingResult, on_delete=models.CASCADE)
    