from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'This email address is already taken!')
                return redirect('register')
            else:
                 user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
                 user.save()
                 print('user created successfully')
                 return redirect('login/')

        else:
            print('User not created!!!')
            messages.error(request, 'Confirmation of password does not match!')
            return redirect('register')
       

    else:
        return render(request, 'registeration.html')

def login(request):       
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid details!')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')