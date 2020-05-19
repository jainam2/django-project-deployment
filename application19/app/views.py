from django.shortcuts import render
from app.forms import UserProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):

    return HttpResponse('You are logged in!')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserProfileForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)

            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserProfileForm()

    return render(request, 'register.html', {"registered": registered,
                                             'user_form': user_form,
                                             })


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

        else:
            print('Someone tried to login and failed')
            print(f'Username: {username} and password: {password}')
            return HttpResponse('INVALID LOGIN DETAILS')
    else:
        return render(request, 'login.html', {})

