from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout

from .forms import SignInForm

def signIn(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid:
            form.save()
            # login(request,user)
            return redirect('user:login')
    return render(request,'user/signin.html',{'form':form})

@login_required
def userLogout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request,'user/logout.html')
