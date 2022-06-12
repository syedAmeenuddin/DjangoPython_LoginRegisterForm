from django.shortcuts import redirect, render
from .models import lotteryimages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    if request.method == "POST":
        userid = request.POST['mobilenumber']
        password = request.POST['password']
        registeruser = User.objects.create_user(userid,'NULL',password)
        registeruser.save()
        return redirect('signin')
    return render(request, 'lib/register.html')
def signin(request):
    if request.method == "POST":
        userid = request.POST['mobilenumber']
        password = request.POST['password']
        user = authenticate(username=userid, password=password)
        if user is not None:
            login(request,user)
            Lotteryimages = lotteryimages.objects.all()
            return render(request, 'lib/win.html',{'lotteryimages':Lotteryimages})
        else:
            return redirect('register')
    return render(request, 'lib/signin.html')
def bankcard(request):
    return render(request, 'lib/manage_bankcard.html')
