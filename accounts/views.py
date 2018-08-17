from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from . import models
from . import forms
from django.contrib.auth.models import User


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    # go to view profile if signing in
                    return HttpResponseRedirect(reverse('accounts:view_profile'))  # TODO: go to profile
                    
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            # go to edit profile if you just signed up to fill out information
            return HttpResponseRedirect(reverse('accounts:view_profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})

@login_required
def view_profile(request):    
    try:
        userprofile = models.UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        userprofile = models.UserProfile()
        userprofile.user = request.user
        userprofile.save()

    return render(request, 'accounts/view_profile.html', {"userprofile": userprofile})
    
@login_required
def edit_profile(request):
    try:
        userprofile = models.UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        userprofile = models.UserProfile()
        userprofile.user = request.user
        userprofile.save()

    if request.method == "POST":
        form = forms.UserProfileForm(request.POST, request.FILES, instance=userprofile)        
        if form.is_valid():
                     
            form.save()
            return HttpResponseRedirect(reverse('accounts:view_profile'))
    else:
        form = forms.UserProfileForm(instance=userprofile)

        return render(request, 'accounts/edit_profile.html', {"userprofileform": form})
    


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))
