from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from predict import views


from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect(views.index)
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                fname = form.cleaned_data.get('first_name')
                lname = form.cleaned_data.get('last_name')
                messages.success(
                    request, 'Account was created for ' + fname + " " + lname)
                return redirect('login')
        context = {'form': form}
        return render(request, 'reg.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect(views.index)
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            user = authenticate(request, username=email, password=password1)
            if user is not None:
                login(request, user)
                return redirect(views.index)
            else:
                messages.info(request, 'Username Or Password is Incorrect.')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')
