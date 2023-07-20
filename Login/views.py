from datetime import datetime, timedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account, Package, Referral
from django.urls import reverse
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully signed in")
            return redirect('dashboard')
        else:
            messages.error(request, "There was an error while signing in")
            return redirect('home')
    else:
        return render(request, 'home.html')


@login_required()
def register_user(request, referrer):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create the referral link (assuming you have a different way to generate referral links)
            # Retrieve the referrer user based on the referrer parameter (assuming referrer is the username)
            try:
                referrer_user = User.objects.get(username=referrer)
            except User.DoesNotExist:
                # Handle the case where the referrer user does not exist
                referrer_user = None
            messages.success(request, "You have successfully registered! Choose a preferred package to continue")
            user_id = request.user.id
            # Create or update the Account and Referral objects for the user
            acc, _ = Account.objects.get_or_create(userid=user_id,
                                                   defaults={'account_balance': 0, 'referral_balance': 0,
                                                             'views_balance': 0})
            if referrer_user:
                ref, _ = Referral.objects.get_or_create(user_id=user_id, referrer_id=referrer_user.id,
                                                        defaults={'amount': 0})
            return render(request, 'package_buy.html',
                          {'username': username})  # Redirect to the appropriate URL for package selection
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def dashboard(request):
    username = request.user.username
    user_id = request.user.id
    account = Account.objects.get(userid=user_id)
    package_ = Package.objects.get(userid=user_id)

    return render(request, 'dashboard.html', {'username': username, 'account': account, 'package': package_})


@login_required
def w_views(request):
    username = request.user.username
    user_id = request.user.id
    account = Account.objects.get(userid=user_id)
    package_ = Package.objects.get(userid=user_id)
    referral_count = Referral.objects.filter(referrer_id=user_id).count()
    print("Referral count:", referral_count)

    return render(request, 'w_views.html',
                  {'username': username, 'account': account, 'package': package_, 'referral_count': referral_count})


@login_required
def package(request):
    username = request.user.username
    return render(request, 'package.html', {'username': username})


def package_buy(request):
    return render(request, 'package_buy.html')


def buy_package(request, username, package_type):
    username = username
    package_type = package_type

    return render(request, 'buy.html', {'username': username, 'package_type': package_type})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


def bought(request, package_type):
    package_type = package_type
    user_id = request.user.id

    # Calculate the due date (now + 30 days)
    due_date = datetime.now() + timedelta(days=30)

    x = Package(userid=user_id, package_type=package_type, due_date=due_date)
    x.save()

    y = Referral.objects.get(user_id=user_id)
    referrer_id = y.referrer_id
    if package_type == 'GOLD':
        y.amount = 500
    elif package_type == 'SILVER':
        y.amount = 200
    else:
        y.amount = 100
    y.save()

    z = Account.objects.get(userid=referrer_id)
    a = Package.objects.get(userid=user_id)
    referrer_package = a.package_type

    if referrer_package == 'GOLD':
        if package_type == 'GOLD':
            z.referral_balance = 175
        elif package_type == 'SILVER':
            z.referral_balance = 70
        else:
            z.referral_balance = 35
    elif referrer_package == 'SILVER':
        if package_type == 'GOLD':
            z.referral_balance = 100
        elif package_type == 'SILVER':
            z.referral_balance = 40
        else:
            z.referral_balance = 20
    else:
        if package_type == 'GOLD':
            z.referral_balance = 50
        elif package_type == 'SILVER':
            z.referral_balance = 20
        else:
            z.referral_balance = 10
    z.save()

    messages.success(request, "Successfully purchased " + package_type)
    return redirect('dashboard')
