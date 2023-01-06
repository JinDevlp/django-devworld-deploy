from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Profile, Technology, Message
from .forms import ProfileForm,TechnologyForm, MessageForm,CustomUserForm
from django.contrib.auth.models import User

from .utils import *
# Create your views here.

def profiles(request):
    profiles,techs, search_query = searchProfiles(request)
    custom_range, profiles = paginationProfiles(request, profiles, 4)

    context = {'profiles': profiles,'techs':techs, "search_query": search_query, 'custom_range':custom_range}
    return render(request,'home.html', context)


@login_required(login_url='login')
def viewInbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all() # messages is related name in our Message Model
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'profile':profile,'messageRequests':messageRequests,'unreadCount':unreadCount}
    return render(request, 'users/inbox.html',context)


@login_required(login_url='login')
def viewMessage(request,pk):
    profile = request.user.profile
    singleMessage = profile.messages.get(id=pk)
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    if singleMessage.is_read == False:
        singleMessage.is_read = True
        singleMessage.save()

    context = {'profile': profile, 'singleMessage': singleMessage,'unreadCount':unreadCount}
    return render(request, 'users/message.html',context)


@login_required(login_url='login')
def sendMessage(request,pk):
    profile = request.user.profile
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = profile
            message.recipient = recipient
            message.save()
            messages.success(request,"Message sent")
            return redirect('profile',pk=recipient.id)

    context= {"profile":profile,"recipient":recipient,'form':form}
    return render(request,'message_form.html',context)

def viewprofile(request,pk):
    profile = Profile.objects.get(id=pk)

    topTechnologys = profile.technology_set.exclude(description__exact="") #filter out blank techs
    otherTechnologys = profile.technology_set.filter(description="")

    context = {'profile':profile,'topTechnologys':topTechnologys, 'otherTechnologys':otherTechnologys }

    return render(request, 'users/profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    technology = profile.technology_set.all()
    posts = profile.post_set.all()

    context = {'profile':profile,'technology':technology, 'posts':posts}
    return render(request, 'users/account.html', context)


@login_required(login_url="login")
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')


    context = {'form':form, 'profile':profile}
    return render(request, 'users/editprofile.html',context)


@login_required(login_url="login")
def addTech(request):
    profile = request.user.profile
    form = TechnologyForm()

    if request.method == "POST":
        form = TechnologyForm(request.POST)
        if form.is_valid():
            tech = form.save(commit=False)
            tech.owner = profile
            tech.save()
            return redirect('account')


    context = {'form':form}
    return render(request, "users/tech_form.html", context)


@login_required(login_url="login")
def deleteTech(request,pk):
    profile = request.user.profile
    tech = profile.technology_set.get(id=pk)

    if request.method == "POST":
        tech.delete()
        messages.success(request,"Tech deleted")
        return redirect('account')

    context = {'tech':tech, 'profile':profile}
    return render(request, "users/edit_tech.html", context)


def loginUser(request):
    # logged in user cant access login page
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist!')

        user = authenticate(request, username=username, password=password) # make sure user username and password is corect

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect('profiles')

        elif username != request.POST['username'] or password != request.POST['password'] :
            messages.error(request,'Username or Password incorrect')

    context = {'page': page }
    return render(request, 'users/login.html',context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out!')
    return redirect('profiles')


def registerUser(request):
    page = 'register'
    form = CustomUserForm()

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User created')

            login(request, user)
            return redirect('edit-profile')

        else:
            messages.error(request, 'Registration Error')


    context = {'page': page, 'form':form}
    return render(request,'users/login.html',context)


