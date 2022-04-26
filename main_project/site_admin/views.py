from django.shortcuts import render,redirect
from django.contrib import messages
from site_admin.models import *
from django.http import JsonResponse


# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=admin_tb.objects.filter(username=username,password=password)
    user=register_tb.objects.filter(username=username,password=password)
    if admin.count()>0:
        request.session['id']=admin[0].id
        return render(request,'adminhome.html',{'data':admin})
    elif user.count()>0:
        request.session['id']=user[0].id
        return render(request,'userhome.html',{'data':user})
    else:
        messages.add_message(request,messages.INFO,"Incorrect username or password")
    return redirect('login')
def addhobby(request):
    return render(request,'addhobby.html')
def addhobbyAction(request):
    hobby=request.POST['hobby']
    hobby=hobby_name_tb(hobbyname=hobby)
    hobby.save()
    messages.add_message(request,messages.INFO,"Added sucessfully")
    return redirect('addhobby')
def register(request):
    hobby=hobby_name_tb.objects.all()
    country=country_tb.objects.all()
    return render(request,'register.html',{'data':country,'data1':hobby})
def getstate(request):
    countryid=request.GET['countryid']
    state=state_tb.objects.filter(countryid=countryid)
    return render(request,'getstate.html',{'data':state})
def registerAction(request):
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    phone=request.POST['phone']
    country=request.POST['country']
    country_obj=country_tb.objects.get(id=country)
    state=request.POST['state']
    state_obj=state_tb.objects.get(id=state)
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    register=register_tb(name=name,gender=gender,dob=dob,address=address,phone=phone,country=country_obj,state=state_obj,securityquestion=securityquestion,answer=answer,username=username+'@mymail.com',password=password)
    register.save()
    hobby=request.POST.getlist('hobby')
    for hid in hobby:
        hobby_obj=hobby_name_tb.objects.get(id=hid)
        hobbys=customer_hobby_tb(hobbyid=hobby_obj,userid=register)
        hobbys.save()   
    messages.add_message(request,messages.INFO,"Registered")
    return redirect('register')
def checkusername(request):
    username=request.GET['username']
    user=register_tb.objects.filter(username=username+'@mymail.com')
    if len(user)>0:
        msg="exists"
    else:
        msg="not exists"
    return JsonResponse({'valid':msg})
def addhobbyfactor(request):
    hobby=hobby_name_tb.objects.all()
    return render(request,'addhobbyfactor.html',{'data':hobby})
def addhobbyfactorAction(request):
    hobby=request.POST['hobby']
    hobby_obj=hobby_name_tb.objects.get(id=hobby)
    factorname=request.POST['factorname']
    h=hobby_factor_tb(hobbyid=hobby_obj,factorname=factorname)
    h.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect("addhobbyfactor")
def addagefactor(request):
    return render(request,'addagefactor.html')
def addagefactorAction(request):
    minimumage=request.POST['minimumage']
    maximumage=request.POST['maximumage']
    factorname=request.POST['factorname']
    agefactor=agefactor_tb(minimumage=minimumage,maximumage=maximumage,factorname=factorname)
    agefactor.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addagefactor')
def addseason(request):
    return render(request,'addseason.html')
def addseasonAction(request):
    seasonname=request.POST['seasonname']
    season=season_tb(seasonname=seasonname)
    season.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addseason')
def addseasonfactor(request):
    season=season_tb.objects.all()
    return render(request,'addseasonfactor.html',{'data':season})
def addseasonfactorAction(request):
    seasonid=request.POST['season']
    seasonid_obj=season_tb.objects.get(id=seasonid)
    factorname=request.POST['factorname']
    addsf=seasonfactor_tb(seasonid=seasonid_obj,factorname=factorname)
    addsf.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addseasonfactor')
def addseasoncountryfactor(request):
    season=season_tb.objects.all()
    country=country_tb.objects.all()
    factor=seasonfactor_tb.objects.all()
    return render(request,'addseasoncountryfactor.html',{'data1':season,'data2':country,'data3':factor})
def addseasoncountryfactorAction(request):
    season=request.POST['season']
    print(season)
    season_obj=season_tb.objects.get(id=season)
    print(season_obj)
    country=request.POST['country']
    country_obj=country_tb.objects.get(id=country)
    state=request.POST['state']
    state_obj=state_tb.objects.get(id=state)
    factor=request.POST['factor']
    factor_obj=seasonfactor_tb.objects.get(id=factor)
    month=request.POST['month']
    seasoncountry=seasoncountry_tb(seasonid=season_obj,countryid=country_obj,stateid=state_obj,factorid=factor_obj,month=month)
    seasoncountry.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addseasoncountryfactor')
def logout(request):
    messages.add_message(request,messages.INFO,"Logged out")
    return render(request,'login.html')
    
    
