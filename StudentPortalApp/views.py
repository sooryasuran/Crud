from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from StudentPortalApp.forms import LoginForm, StudentForm
from StudentPortalApp.models import Student


def homeview(request):
    return render(request,'index.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminhome')
            elif user.is_student:
                return redirect('studentprofile')
        else:
            messages.info(request,'Invalid Credentials')
    return render(request,'login.html')

def studentprofile(request):
    u = request.user
    profile = Student.objects.filter(user_id=u)
    return render(request, 'studentprofile.html', {'profile': profile})


@login_required(login_url='loginview')
def adminview(request):
    return render(request,'adminhome.html')


def logoutview(request):
    logout(request)
    return redirect('loginview')

@login_required(login_url='loginview')
def studentregister(request):
    login_form=LoginForm()
    student_form=StudentForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        student_form = StudentForm(request.POST)
        if login_form.is_valid() and student_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            s = student_form.save(commit=False)
            s.user = user
            s.save()

            return redirect('adminhome')
    return render(request,'studentregister.html',{'login_form':login_form,'student_form':student_form})

