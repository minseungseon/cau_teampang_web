from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib import auth
#from TeampAng.account.models import Profile

# Create your views here.
def myTimetable(request):
    user = get_object_or_404(User, pk=request.user.pk)
    timetable = user.profile.time_table
    return render(request,'myTimetable.html', {'timetable' : [timetable["Mon"],timetable["Tue"],timetable["Wed"],timetable["Thu"], timetable["Fri"]]})
    #{'Mon' : timetable["Mon"], 'Tue' : timetable["Tue"], 'Wed' : timetable["Wed"], 'Thu' : timetable["Thu"], 'Fri' : timetable["Fri"]}