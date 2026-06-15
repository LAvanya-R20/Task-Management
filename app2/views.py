from django.shortcuts import render, redirect
from .models import register1 as RegisterModel

# Create your views here.

def register1(request):
    if request.method == 'POST':
        a = request.POST['u']
        b = request.POST['e']
        c = request.POST['m']
        d = request.POST['p']
        RegisterModel.objects.create(username=a, email=b, mobile=c, password=d)
        return redirect('l')
    return render(request, 'register.html')

def login1(request):
    col = RegisterModel.objects.all()
    if request.method == 'POST':
        a=request.POST['u']
        b=request.POST['p']
        for i in col:
            if (i.username==a or i.mobile==a or i.email==a) and (i.password==b):
                if i:
                    request.session['i_id'] = i.id
                return redirect('home')
        else:
            return render(request, 'login.html',{'error':"Invalid credentials"})
    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('l')