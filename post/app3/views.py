import pyautogui as pu
from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request, user)
            pu.confirm("Login Successful.")
            return redirect('/app2/contact')
        else:
            pu.alert("Please enter correct Username or password.")
            return redirect('login')
    else:
        return render(request, 'login.html')