

from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse, redirect
from pip._internal.utils import datetime

from .forms import storeForm
from .models import store


# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("hello user")
            return redirect('finalproapp1:page')
        else:
            messages.info(request, "invalid user")
            print("invalid")
            return redirect('finalproapp1:login')
    else:
        return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('finalproapp1:register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.is_staff = True
                user.save();
                print("user registered")
                return redirect('finalproapp1:login')
        else:
            messages.info(request, "password not matching")
            return redirect('finalproapp1:register')
            print("password not matching")
        return redirect('/')

    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    if logout:
        messages.info(request, "Logged out")
        return redirect('finalproapp1:home')
    return redirect('finalproapp1:form')


# def page2(request):
#     return render(request, 'page2.html')


def page(request):
    return render(request, 'page1.html')


def formView(request):
    # form = storeForm()
    form=store.objects.all()
    if request.method == 'POST':

       if form.is_valid():
          return redirect('/')

    return render(request,'form.html',{'form':form})

def saveData(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        department = request.POST.get('slct1')
        course = request.POST.get('slct2')
        purpose = request.POST.get('purpose')
        materials=request.POST.getlist('option')
        save=store(name=name,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,purpose=purpose,department=department,course=course,materials=materials)
        save.save()
        messages.info(request, "Order Confirmed")
        return redirect('finalproapp1:saveData')


    return render(request,'form.html')
# def submit(request):
#
#     return redirect('finalproapp1:submit')