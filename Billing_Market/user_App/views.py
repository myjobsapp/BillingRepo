from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.http import is_safe_url

from .models import User
from .form import RegisterForm, UserAdminCreationForm, UserAdminChangeForm, LoginForm
from django.shortcuts import render, redirect
import logging

from django.views.generic import CreateView, FormView

logger=logging.getLogger(__name__)

# Create your views here.
'''
def registerView(request):
    if request.method=='POST':
        print('Hii')
        form=UserCreationForm(request.POST)
        print('post')
        if form.is_valid():
            print('valid')
            form.save()
            return HttpResponse("User Added")

        else:
            print('sds')
            return render(request,'account/register.html',{'form':form})
    else:
        form=UserCreationForm()
        return render(request, 'account/register.html', {'form': form})

def loginView(request):


    if request.method=='POST':
        n=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=n,password=p)
        if user is not None:
            login(request,user)
            return HttpResponse('Logged in')
        else:
            messages.error(request,'Enter valid Uname or pw')
            return render(request,'account/login.html')
    else:
        return render(request, 'account/login.html')

def logoutView(request):
    logout(request)
    return HttpResponse('LOgged out')

def signup(request):
    if request.method=='POST':
        if request.POST['password']==request.POST['passwordagain']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'account/register.html',{'error':'user already exist'})
            except user.DoesNotExist:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                auth.login(request,user)
                return HttpResponse('Registered')
        else:
            return render(request,'account/register.html',{'error':'Password didnt matched'})
    else:
        return render(request, 'account/register.html')



def demoView(request):
    var1=int(input('Enter No'))

    logging.info('Addition')
    if var1 is not int():
        logger.error("PLx enter interger")

    return render(request,'account/var.html',{'v':var1})
'''

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'user_App/register.html'
    success_url = '/ua/login/'
    context_object_name = 'form'

def loginView(request):
    if request.method == 'POST':
        n=request.POST.get('email')
        p=request.POST.get('password')
        user=authenticate(username=n,password=p)
        if user is not None:
            login(request,user)
            print('logged in')
            return HttpResponse('Logged in')
        else:
            messages.error(request,'Enter valid Uname or pw')
            return render(request,'user_App/login.html')
    else:
        return render(request, 'user_App/login.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'user_App/login.html')


def logoutView(request):
    logout(request)
    return HttpResponse('logged out successfully')

'''
class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'account/login.html'

    def form_valid(self, form):
        request=self.request
        next= request.GET.get('next')
        next_post=request.POST.get('next')
        redirect_path =next or next_post or None
        email =form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        user =authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            if is_safe_url(redirect_path ,request.get_host()):
                return redirect(redirect_path)
            else:
                return HttpResponse('Logged IN')
                #return redirect('/')
        return super(LoginView, self).form_invalid(form)

'''

