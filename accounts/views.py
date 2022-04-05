from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = make_password(request.POST['password'])
        try: 
            User.objects.get(username=username)
            return HttpResponseRedirect('/')
        except:
            user = User(username=username,password=password)
            user.save()
            return HttpResponseRedirect('/')
    return render(request, 'accounts/signup.html')

def login_page(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            pass
    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')