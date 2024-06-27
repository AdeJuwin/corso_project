from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('remail')
        phone_number = request.POST.get('rphone')
        password1 = request.POST.get('rpass1')
        password2 = request.POST.get('rpass2')
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, f'This username {username} already exist')
                print("Username exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, f'This email {email} already exist')
                return redirect('register')
                
            else:
                user=User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, 'Your Acount has been created!')
                return redirect('login')
        else:
            messages.error(request, 'Password Mismatch')
            print("Password Mismatch")
            return redirect('register')
    else:    
        return render(request, 'register.html', {'title': 'Register'})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['rpass1']
        print(username)
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successful')
            return redirect('profile')
            
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html', {'title':'Login'})

def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out!')
    return redirect('login')

@login_required
def profile_user(request):
    return render(request, 'profile.html', {'title': 'Profile'})

