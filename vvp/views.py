from django.shortcuts import render,redirect
from .models import alumni
from django.utils import timezone
from django.contrib.auth.models import auth
from django.contrib.auth import logout


# Create your views here.
def index(request):
    return render(request,'home.html')

def alumni(request):
    if request.method=='POST':
        obj = alumni()
        obj.First_name = request.POST['fname']
        obj.Last_name = request.POST['lname']
        obj.Email = request.POST['email']
        obj.Phone = request.POST['phone']
        obj.Batch = request.POST['batch']
        obj.Photo = request.FILES['photo']
        obj.address = request.POST['add1'] + ' ' + request.POST['add2'] + ' ' + request.POST['city'] + ' ' + request.POST['state'] + ' ' + request.POST['zipcode']
        obj.date_time = timezone.now()
        obj.save()
        return redirect('/')
    return render(request,'alumni.html')

def our_gems(request):
    return render(request,'our-gems.html')

def staffmembers(request):
    return render(request,'staff-members.html')

def committeemembers(request):
    return render(request,'committee-members.html')
    
def gallery(request):
    return render(request,'gallery.html')

def notice(request):
    return render(request,'notice.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user != None:
            auth.login(request,user)
            return redirect('/')
        else:
            dict = {'msg': 'Invalid Credentials'}
            return render(request,'login.html',dict)
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'login.html',dict={'msg':'Logged Out Successfully!'})
