from django.shortcuts import render
from app.models import AccessRecord, User

def index(request):
    my_dict = {'greeting': 'Welcome to Second App'}
    return render(request,'app/index.html',context=my_dict)

def records(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = { 'access_records': webpages_list}
    return render(request,'app/records/index.html',context=date_dict)

def users(request): 
    user_list = User.objects.order_by('last_name')
    data_dict = { 'users' : user_list }
    
    return render(request,'app/users/index.html',context=data_dict)
