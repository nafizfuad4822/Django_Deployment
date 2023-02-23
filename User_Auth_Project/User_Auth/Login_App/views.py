from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Login_App.forms import UserForm,UserProfileForm

from django.contrib.auth.models import User
from Login_App.models import UserProfile

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def home(request):
    User_info = ''
    User_basic_info = ''
    if request.user.is_authenticated:
        current_user = request.user
        User_id = current_user.id
        User_info = User.objects.get(id=User_id)
        User_basic_info = UserProfile.objects.get(user__pk=User_id)
    diction={'User_info': User_info,'User_basic_info': User_basic_info}
    return render(request,'Login_App/index.html',context=diction)

def register_user(request):
    registered=False
    if request.method == 'POST':
        User_Form = UserForm(data=request.POST)
        User_Profile_Form = UserProfileForm(data=request.POST)
        if User_Form.is_valid() and User_Profile_Form.is_valid():
            user = User_Form.save()
            user.set_password(user.password)
            user.save()
            user_info = User_Profile_Form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
            user_info.save()
            registered=True
    else:
        User_Form = UserForm()
        User_Profile_Form = UserProfileForm()
    diction = {'User_Form':User_Form,'User_Profile_Form':User_Profile_Form,'heading':'User Registration Form','registered':registered}
    return render(request,'Login_App/register_user.html',context=diction)
def login_user(request):
    diction={'heading':'User Login Form'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_App:home'))
            else:
                return HttpResponse('Your account is inactive')
        else:
            return HttpResponse('Invalid Credentials')
    else:
        return render(request, 'Login_App/login_user.html',context=diction)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_App:home'))



    