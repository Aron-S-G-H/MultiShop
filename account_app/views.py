from django.shortcuts import render, redirect, reverse
from django.views.defaults import page_not_found
from django.contrib.auth import authenticate, login, logout
from django.views import View
from account_app.forms import LoginForm, RegisterForm, CheckOtpForm, EditAccountForm
from django.core.mail import send_mail
from django.conf import settings
from userModel_app.models import Otp, User
from random import randint
from uuid import uuid4


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, 'account_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('/')
            else:
                form.add_error('email', 'Invalid User Data')

        return render(request, 'account_app/login.html', {'form': form})


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            form = RegisterForm()
            return render(request, 'account_app/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] != cd['conf_pass']:
                form.add_error('password', 'Passwords are not the same !!')
            else:
                random_code = randint(1000, 9999)
                token = str(uuid4())

                send_mail(subject='Authentication Code',
                          message=f'Here is a authentication code for Arone Shop: {random_code}',
                          from_email=settings.EMAIL_HOST_USER,
                          recipient_list=[cd['email']])

                print(random_code)

                Otp.objects.create(
                    email=cd['email'],
                    fullname=cd['fullname'],
                    phone=cd['phone'],
                    code=random_code,
                    password=cd['password'],
                    token=token)

                return redirect(reverse('account:checkOtp_page') + f'?token={token}')

        return render(request, 'account_app/register.html', {'form': form})


class CheckOtp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            token = request.GET.get('token')
            if token is None:
                return redirect('account:Login_page')
            form = CheckOtpForm()
            return render(request, 'account_app/check_otp.html', {'form': form})

    def post(self, request):
        form = CheckOtpForm(request.POST)
        token = request.GET.get('token')

        if form.is_valid():
            cd = form.cleaned_data

            if Otp.objects.filter(code=cd['code'], token=token).exists():
                new_user = Otp.objects.get(token=token)
                print(type(new_user.phone))
                user = User.objects.create_user(
                    fullname=new_user.fullname,
                    email=new_user.email,
                    phone=new_user.phone,
                    password=new_user.password)

                login(request, user)

                new_user.delete()

                return redirect('/')
            else:
                form.add_error('code', 'Wrong code')
        else:
            form.add_error('code', 'Invalid Data')
        return render(request, 'account_app/check_otp.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


def user_edit(request):
    user = request.user
    if user.is_anonymous:
        return page_not_found(request)
    else:
        form = EditAccountForm(instance=user)
        if request.method == 'POST':
            form = EditAccountForm(instance=user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')

        return render(request, 'account_app/updateAccount.html', context={'form': form})
