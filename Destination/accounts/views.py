from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
# User Authentication and login


def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= Username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')


# Register a new User


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=Username):
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email= email):
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username, first_name=first_name, email=email, password=password1, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login ')

        else:
            print("Password not matching")
            return redirect('register')

    else:
        return render(request, 'register.html')

# User logout
def logout(request):
    auth.logout(request)
    return redirect('/')