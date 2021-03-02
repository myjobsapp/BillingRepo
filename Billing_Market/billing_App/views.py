from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def homeview(request):
    # return HttpResponse('This is a HomePage..!!')
    template_name = 'home.html'
    #context = ''
    return render(request, template_name)



