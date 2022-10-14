from django.shortcuts import redirect, render
from django.http import HttpResponse




def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')






def login(request):
    if request.method == "GET":
        return render(request, 'login.html')        






      