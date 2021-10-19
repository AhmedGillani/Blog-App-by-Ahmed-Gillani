from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import PostForm, Register, FeedForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        fm = Register(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your account has been created Successfully!')
        else:
            messages.warning(request, 'Invalid Input or Create a Strong Password!')
    fm = Register()
    return render(request, 'display/register.html', {'form': fm})


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            login(request, user)
            return HttpResponseRedirect('/home')
        else:
            messages.warning(request, 'Invalid Input or User Not Registered!')
    fm = AuthenticationForm()
    return render(request, 'display/login.html', {'form': fm})


def home(request):
    if request.user.is_authenticated:
        blog = Post.objects.all()
        return render(request, 'display/home.html', {'blog': blog})
    return HttpResponseRedirect('/')


def post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PostForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Your Blog has been posted Successfully!")
            else:
                messages.warning(request, "Invalid Input or Entre correct info. in required blocks!")
        fm = PostForm()
        return render(request, 'display/post.html', {'form': fm})
    return HttpResponseRedirect('/')


def feedback(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = FeedForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Your Feedback has been posted Successfully!")
            else:
                messages.warning(request, "Invalid Input or Entre correct info. in required blocks!")
        fm = FeedForm()
        return render(request, 'display/feedback.html', {'form': fm})
    return HttpResponseRedirect('/')


def detail(request, id):
    if request.user.is_authenticated:
        x = Post.objects.get(pk=id)
        return render(request, 'display/detail.html', {'x': x, 'id': id})
    return HttpResponseRedirect('/')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')
