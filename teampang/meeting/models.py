from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class MeetingCreate(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateTimeField()
    invite_url = models.URLField()
    member_list = JSONField(null=True) #이후 User , no user로 확장 --> 민승: 초대 기능으로 확장하면 좋을 것 같음 
    # author = models.ForeignKey(User, on_delete=models.CASCADE) #작성자 => 팀장

class MeetingInput(models.Model): #MeetingDetail로 이름 바꾸기
    team = models.ForeignKey(MeetingCreate, on_delete=models.CASCADE,related_name='team_input')
    dummyname = models.CharField(max_length=30)
    timetable = JSONField(null=True)

    class Meta:
        unique_together = ['team', 'dummyname', 'timetable']
        ordering = ['team']
    
    def __str__(self):
        return '%d: %s , %s' % (self.team, self.dummyname, self.timetable)

class MeetingTime(models.Model):
    team = models.ForeignKey(MeetingCreate, on_delete=models.CASCADE,related_name='team_time')
    matched_date = models.DateField()
    matched_time = models.TimeField()

    class Meta:
        unique_together = ['team', 'matched_date', 'matched_time']
        ordering = ['team']
    
    def __str__(self):
        return '%d: %s , %s' % (self.team, self.matched_time, self.matched_time)
    
# class MemberList(models.Model):
# 	# authenticated = models. #유저 정보
# 	anonymous = jsonfield.JSONField() #비회원 정보 텍스트
# 	number = models.IntegerField() # 멤버수
#     meetingResult = models.ForeignKey(MeetingResult, on_delete=models.CASCADE)
    