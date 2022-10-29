import time

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import RegisterUserForm, PasswordChangingForm


def set_password_success(request):

    return render(request, 'set_password_success.html', {})


class MyPasswordChangeview(PasswordChangeView):
    form = PasswordChangingForm
    success_url = reverse_lazy('home')
    # if request.method == 'POST':
    #     if form.is_valid():
    #         redirect('/set_password_success.html')
    # return render(request,'set_password.html',{'form':form})


def login_user(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(
                request, "There was an error occured or your informations didn't match, Please try again...")
            return redirect('/login')
    else:
        return render(request, 'authenticate_pages/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, ('You logout request has been succesfull. '))
    return redirect('authenticate_pages/login.html')


def register_user(request, *args, **kwargs):

    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your registiration has been succesfull')

            return redirect('/login')
        else:
            messages.success(
                request, 'Your registiration has failed, try again')

            return render(request, 'authenticate_pages/register.html', {'form': form})
    else:
        # form = RegisterUserForm
        pass

    return render(request, 'authenticate_pages/register.html', {'form': form})


def reddirecting_page(request):
    t = 5
    time.sleep(t)
    redirect('login/')

    return render(request, 'authenticate_pages/reddirecting_page.html', {'t': t})

