from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import Signup_Form,User_Form,Profile_Form
from django.contrib.auth   import authenticate, login
from .models import Profile

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=Signup_Form(request.POST)
        if form.is_valid():
            form.save()
            user_name=form.cleaned_data['username']
            pass_word=form.cleaned_data['password1']
            var=authenticate(username=user_name,password=pass_word)
            login(request,var)
            return redirect('/accounts/profile/')

    else:
        form=Signup_Form()

    return render(request,'registration/signup.html',{'form':form})            

def profile(request):
    profile=Profile.objects.get(user=request.user)

    return render(request,'accounts/profile.html',{'profile':profile})

def edit_profile(request):
    profile=Profile.objects.get(user=request.user)
    if request.method=='POST':
        pr_form=Profile_Form(request.POST,request.FILES,instance=profile)
        us_form=User_Form(request.POST,instance=request.user)
        if pr_form.is_valid() and us_form.is_valid():
            us_form.save()
            myprof=pr_form.save(commit=False)
            myprof.user=request.user
            myprof.save()
            return redirect('accounts/profile/')
        
    else:
        pr_form=Profile_Form(instance=profile)     
        us_form=User_Form(instance=request.user)

    return render(request,'accounts/edit_profile.html',{'pr_form':pr_form,'us_form':us_form})
    


