from django.shortcuts import render,redirect
from .models import rDetails
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def reg(request):
    if request.method == "POST":
        rname = request.POST.get('name')
        remail = request.POST.get('email')
        rpassword = request.POST.get('password')
        rpasss = request.POST.get('passs')
        User = get_user_model()
        if rpassword != rpasss:
            messages.warning(request, 'password and confirm password does not match.')
            return render(request, 'Register/register.html')
        else:
            if rname and remail and rpassword and rpasss:
                if rpassword == rpasss:
                    post = rDetails()
                    post.RName = rname
                    post.REmail = remail
                    post.RPassword = make_password(rpassword)
                    post.RConfirm_password= make_password(rpasss)
                    post.is_approved = False  # set is_approved to False
                    post.save()
                    user=User.objects.create(username=request.POST.get('name'),email=request.POST.get('email'),password = make_password(request.POST.get('password')))
                    user.save()
                    messages.success(request, 'Registered successfully.')

                    return render(request, 'Register/register.html')
                else:
                    messages.warning(request, 'password does not match.')
                    return render(request, 'Login/login.html')

            else:
                messages.warning(request, 'Please fill all fields.')
                return render(request, 'Register/register.html')

    else:
        return render(request, 'Register/register.html')