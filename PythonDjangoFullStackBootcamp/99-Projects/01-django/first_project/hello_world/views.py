from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    my_dict = {'greeting': 'Good afternoon, good evening, and good night'}
    return render(request,'hello_world/index.html',context=my_dict)
