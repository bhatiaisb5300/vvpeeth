from django.shortcuts import render,redirect
from .models import alumni,gallery,notice_events,staff,committee,our_gems
from django.utils import timezone
from django.contrib.auth.models import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    obj_gallery = reversed(gallery.objects.all()[:6])
    obj_notice = reversed(notice_events.objects.all()[:4])
    return render(request,'home.html',{'gallery':obj_gallery,'notice':obj_notice})

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
        obj.current_employment_status = request.POST['current']
        obj.save()
        return redirect('/')
    return render(request,'alumni.html')

def our_gems_view(request):
    obj_tenth = reversed(our_gems.objects.filter(Class='10th').order_by('Batch','Marks'))
    obj_twelth = reversed(our_gems.objects.filter(Class='12th').order_by('Batch','Marks'))
    return render(request,'our-gems.html',{'tenth':obj_tenth,'twelth':obj_twelth})

@login_required
def gems_form(request):
    if request.method=='POST':
        obj = our_gems()
        obj.Name = request.POST['name']
        obj.Marks = request.POST['marks']
        obj.Photo = request.FILES['photo']
        obj.Batch = request.POST['batch']
        obj.Class = request.POST['class']
        obj.save()
        return render(request,'our_gems_form.html',{'msg':'Entry Added Successfully!'})
    return render(request,'our_gems_form.html')


def staffmembers(request):
    obj = staff.objects.all().order_by('s_no')
    return render(request,'staff-members.html',{'item':obj})

def committeemembers(request):
    obj = committee.objects.all().order_by('s_no')
    return render(request,'committee-members.html',{'item':obj})

def gallery_view(request):
    obj = reversed(gallery.objects.all())
    return render(request,'gallery.html',{'item':obj})

@login_required
def gallery_form(request):
    if request.method=='POST':
        obj = gallery()
        obj.Photo = request.FILES['photo']
        obj.Title = request.POST['title']
        obj.Description = request.POST['Description']
        obj.save()
        return render(request,'gallery_form.html',{'msg':'Photo Added Successfully!'})
    return render(request,'gallery_form.html')

def notice(request):
    obj = reversed(notice_events.objects.all())
    return render(request,'notice.html',{'item':obj})

@login_required
def notice_form(request):
    if request.method=='POST':
        obj = notice_events()
        obj.Photo = request.FILES['photo']
        try:
            obj.File = request.FILES['file']
        except:
            pass
        obj.Title = request.POST['title']
        obj.Description = request.POST['Description']
        obj.save()
        return render(request,'notice_form.html',{'msg':'Entry Added Successfully!'})
    return render(request,'notice_form.html')

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
