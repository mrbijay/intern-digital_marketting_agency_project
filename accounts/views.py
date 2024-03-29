from django import forms
from django.shortcuts import redirect, render

from accounts.forms import RegistrationForm
from accounts.models import Account
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

#verification send email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator 
from django.core.mail import EmailMessage

# ...............for user profile update
from .forms import UserUpdateForm
from .models import Profile
from base.models import Footer, Header, Navbar

# Create your views here.


def register(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone_number=form.cleaned_data['phone_number']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            city=form.cleaned_data['city']
            province=form.cleaned_data['province']
            username=email.split('@')[0]

            user=Account.objects.create_user(first_name=first_name,last_name=last_name,city=city,province=province,email=email,phone_number=phone_number,username=username,password=password)
            user.save()
            #user aactivation
            current_site=get_current_site(request)
            mail_subject='Please activate your account.'
            message=render_to_string('accounts/account_verification_mail.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email=email
            send_email=EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            # messages.success(request, 'Thank you for registration. We have sent you a verification email.Please Verify. ')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form=RegistrationForm()
    context={
        'form':form,
    }
   
    return render(request,'accounts/register.html',{'data':data,'header':header,'footer':footer,'form':form})

def login(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method =='POST':
        email=request.POST['email']   #name of input 
        password=request.POST['password'] 

        user=auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myprofile')
        else:
            messages.error(request, 'Error:Invalid login Details')
            return redirect('login')


    return render(request,'accounts/login.html',{'data':data,'header':header,'footer':footer})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulation ! Your account is activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')

def forgetPassword(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method == 'POST':
        email=request.POST['email']
        if Account.objects.filter(email=email).exists():
            user=Account.objects.get(email__exact=email)

            #reset password email
            current_site=get_current_site(request)
            mail_subject='Reset your password.'
            message=render_to_string('accounts/reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),

            })
            to_email=email
            send_email=EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request , 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exists.')
            return redirect('forgetPassword')
    return render(request, 'accounts/forgetPassword.html',{'data':data,'header':header,'footer':footer})


def resetpassword_validate(request,uidb64,token):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,Account.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired.')
        return redirect('login')

def resetPassword(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method == 'POST':
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            uid=request.session.get('uid')
            user=Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful.')
            return redirect('login')

        else:
            messages.error(request, 'Password do not match')
            return redirect('resetPassword')
    return render(request, 'accounts/resetPassword.html',{'data':data,'header':header,'footer':footer})

@login_required(login_url='login')
def change_password(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method =="POST":
        current_password=request.POST['current_password']
        new_password=request.POST['new_password']
        confirm_password=request.POST['confirm_password']

        user=Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success=user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password updated Successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Invalid Current Password.')
                return redirect('change_password')

        else:
            messages.error(request, 'Password Does Not Match.')
            return redirect('change_password')

    return render(request, 'accounts/change_password.html',{'data':data,'header':header,'footer':footer})


@login_required(login_url='login')
def myprofile(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    
    return render(request, 'accounts/myprofile.html',{'data':data,'header':header,'footer':footer})

def edit_profile(request):
    data=Navbar.objects.filter(is_active=True)
    header=Header.objects.all()
    footer=Footer.objects.all()
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request , 'Profile updated Successfully.')
            return redirect('myprofile')

    else:
        u_form=UserUpdateForm(instance=request.user)

    context={
        'u_form': u_form,
    }
    return render(request,'accounts/edit_profile.html',{'data':data,'header':header,'footer':footer,'u_form':u_form})
