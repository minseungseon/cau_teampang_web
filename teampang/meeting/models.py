from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

class MeetingCreate(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateTimeField()
    invite_url = models.URLField()
    member_list = JSONField(null=True) #이후 User , no user로 확장 --> 민승: 초대 기능으로 확장하면 좋을 것 같음 
    # author = models.ForeignKey(User, on_delete=models.CASCADE) #작성자 => 팀장
    def __str__(self):
        return '%s' % (self.name)

def timetable_default():
    return [{"00-02":0}, {"02-04":0}, {"04-06":0}, {"06-08":0}, {"08-10":0}, {"10-12":0}, {"12-14":0}, {"14-16":0}, {"18-20":0}, {"20-22":0}, {"22-24":0}]
    # defalut값이 화면에 보이도록 처리

class MeetingInput(models.Model): #MeetingDetail로 이름 바꾸기
    team = models.ForeignKey(MeetingCreate, related_name='team_input', on_delete=models.CASCADE)
    dummyname = models.CharField(max_length=30)
    date = JSONField(null=True)
    timetable = JSONField(default=timetable_default) #시간 정하기

    class Meta:
        unique_together = ['team', 'date' , 'dummyname', 'timetable']
        ordering = ['team']
    
    def __str__(self):
        return '%s' % (self.dummyname)

class MeetingTime(models.Model):
    team = models.ForeignKey(MeetingCreate, on_delete=models.CASCADE, related_name='team_time')
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
    