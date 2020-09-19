from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import pyautogui as pu
import time
from datetime import date
from .models import TaskData

lock = False
def button(request):
    global temp
    temp = True
    return render(request, 'contact.html', {'lock': lock, 'temp': temp})


task1 = ""
project1 = ""
start_time1 = None
stop_time = 0
initial_time = 0
total_time = 0
end_time = 0
date1 = ''


def start(request):
    global start_time1, lock, date1, temp
    lock = True
    temp = False
    date2 = date.today()
    date1 = date2
    start_time = time.strftime("%Hhr:%Mmin:%Ssec")
    start_time1 = start_time
    global initial_time
    initial_time = time.time()
    return render(request, 'task_run.html', {'start_time': start_time1, 'lock': lock, 'temp': temp})


def stop(request):
    global lock
    global start_time1, stop_time, total_time, end_time, task1, project1
    # stop_time = time.asctime(time.localtime(time.time()))
    stop_time = time.strftime("%Hhr:%Mmin:%Ssec")
    end_time = time.time()
    total_time = end_time - initial_time
    total_time = str(("%.3f" % total_time) + " " + "sec")  # time in seconds
    xy = TaskData(task=task1, project=project1, Date=date1, start_time=start_time1, stop_time=stop_time,
                  total_time=total_time)
    xy.save()
    lock = False
    return render(request, 'task_run.html', {'total': total_time})


def contact12(request):
    global task1, project1, temp
    if request.method == 'POST':
        task = request.POST['task']
        project3 = request.POST['project']
        task1 = task
        project1 = project3
        temp = True
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            pu.alert("Username already exist")
        else:
            x = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                         password=password)
            x.save()
            pu.confirm("user created")
            return redirect('/')
    return render(request, 'signup.html')


def details(request):
    if request.method == 'POST':
        date2 = request.POST['date2']
        print("Project", date2)
        obj = TaskData.objects.filter(Date=date2)
        return render(request, 'details.html', {'result': obj})
    else:
        return render(request, 'details.html', {'message': "please Select the project."})
