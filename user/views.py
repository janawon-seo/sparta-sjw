from django.shortcuts import render, redirect
from user.models import User
from django.contrib.auth import login, authenticate


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/home/')
        
        return render(request, 'login.html')





def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        user = User()
        user.username = request.POST.get('username', '')
        user.phone = request.POST.get('phone', '')
        user.address = request.POST.get('address', '')
        user.set_password = request.POST.get('password', '')

        user.save()

        return redirect('/login/')    
    

def home(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            return redirect('/login/')

        return render(request, 'home.html')   












      