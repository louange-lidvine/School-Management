from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import ExtendedUserCreationForm, MemberForm
from events.models import Event
from .models import Member
from facilities.models import Booking

# Ensure these models are imported

def register(request):
    if request.method == 'POST':
        user_form = ExtendedUserCreationForm(request.POST)
        member_form = MemberForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()
            login(request, user)
            return redirect('login')
    else:
        user_form = ExtendedUserCreationForm()
        member_form = MemberForm()
    return render(request, 'register.html', {'user_form': user_form, 'member_form': member_form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                request.session['last_login'] = str(datetime.now())
                request.session.set_expiry(3600)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def dashboard(request):
    user_events = Event.objects.filter(participants=request.user.member)
    user_bookings = Booking.objects.filter(member=request.user.member)
    return render(request, 'dashboard.html', {'user_events': user_events, 'user_bookings': user_bookings})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')