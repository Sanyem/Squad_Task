from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse



def signup(request,message):

    if request.method=="GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('UserAuth:profile'))
            # return HttpResponse("User Logged in")
        return render(request, 'UserAuth/signup.html',{"message":message})
    
    if request.method=="POST":
        if CustomUser.objects.filter(username=request.POST.get('email')).count():
            return HttpResponseRedirect(reverse('UserAuth:signup', kwargs={"message":"Email already exists. Please choose some other email"}))
        else:
            if request.POST.get('password')!=request.POST.get('confirm_password'):
                return HttpResponseRedirect(reverse('UserAuth:signup', kwargs={"message":"Passwords don't match"}))
            else:
                try:
                    user = CustomUser()
                    user.first_name = request.POST.get('first_name')
                    user.last_name = request.POST.get('last_name')
                    user.username = request.POST.get('email')
                    user.email = request.POST.get('email')
                    user.set_password(request.POST.get('password'))
                    user.save()
                    return HttpResponseRedirect(reverse('UserAuth:user_login', kwargs={"message":''}))
                except Exception as e:
                    print(e)
                    mes = "An Exception Occured ->" + str(e)
                    return HttpResponseRedirect(reverse('UserAuth:signup', kwargs={"message":mes}))


def user_login(request,message):

    if request.method=="GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('UserAuth:profile'))
            # return HttpResponse("User is already Logged in")
        return render(request, 'UserAuth/login.html',{"message":message})

    if request.method=="POST":
        try:
            login_username = request.POST.get('email')
            login_password = request.POST.get('password')
            print(login_password,login_username)
            doc = get_object_or_404(CustomUser,username=login_username)
            user = authenticate(username=login_username,password=login_password)
            print(doc,user)
            if user is not None:
                print(1)
                login(request,user)
                print(user)
                return HttpResponseRedirect(reverse('UserAuth:profile'))
                # return HttpResponse("User Logged in")
        except Exception as e:
            print(e)
            return HttpResponse(e)


def logout(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            auth.logout(request)
            return HttpResponseRedirect(reverse('UserAuth:home'))
        else:
            return HttpResponseRedirect(reverse('UserAuth:home'))


def home(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('UserAuth:profile'))
            # return HttpResponse("User is Already Logged in")
        return render(request, 'UserAuth/home.html')


def profile(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            user = request.user
            return render(request, 'UserAuth/profile.html',{"user":user})
            # return HttpResponse("User is Already Logged in")
        return HttpResponseRedirect(reverse('UserAuth:home'))

