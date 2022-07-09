from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'register/register.html',{'form':form})