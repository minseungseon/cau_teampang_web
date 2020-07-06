from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.contrib import auth
from .models import Profile

# Create your views here.

# def main(request):
#     return render(request,'main.html')

# def signup(request):
#     if request.method =="POST":
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username=request.POST["username"], password=request.POST["password1"]
#             )
#             auth.login(request, user)
#         return redirect ('register_table')
#     return render(request, 'signup.html')


# def register_table(request):
#     return render(request,'register_table.html')

def main(request):
    return render(request,'main.html')

def signup(request):
    if request.method =="POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            profile = Profile(user=user)
            profile.save()
            auth.login(request, user)
        return redirect ('register_table')
    return render(request, 'signup.html')   


def register_table(request, val):
    #print(request.user.id)
    user = get_object_or_404(User, pk=request.user.pk)
    timetable = user.profile.time_table
    i=val/10
    k=val%10
    timetable[i].k=1
    return render(request,'register_table.html', {'Mon' : timetable["Mon"], 'Tue' : timetable["Tue"], 'Wed' : timetable["Wed"], 'Thu' : timetable["Thu"], 'Fri' : timetable["Fri"]})


def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user =  auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html',{'error' : 'username or password is incorrect'})
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main')



# def logout(request):
#     auth.logout(request)
#     return redirect('main')

