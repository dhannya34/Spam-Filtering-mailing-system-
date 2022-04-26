from django.shortcuts import render,redirect
from site_admin.models import *
from site_user.models import *
import datetime
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def compose(request):
    return render(request,'compose.html')
def composeAction(request):
    senderid=request.session['id']
    senderid_obj=register_tb.objects.get(id=senderid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    recieverid=request.POST['recieverid']
    recieverid_obj=register_tb.objects.get(username=recieverid)
    compose=message_tb(senderid=senderid_obj,subject=subject,message=message,date=date,time=time,recieverid=recieverid_obj)
    compose.save()
    messages.add_message(request,messages.INFO,"Message sent")
    return redirect('compose')
def viewmessage(request):
    uid=request.session['id']
    print(uid)
    status=['pending','deleted by reciever']
    message=message_tb.objects.filter(senderid=uid,status__in=status)
    return render(request,'viewmessage.html',{'data':message})
def delete(request,uid):
    message=message_tb.objects.filter(id=uid)
    status=message[0].status
    if status == 'deleted by reciever':
        messages=message_tb.objects.filter(id=uid).delete()
    else:
        messages=message_tb.objects.filter(id=uid).update(status="deleted by sender")
    return redirect('viewmessage')        
        
    
    delete=message_tb.objects.filter(id=uid).delete()
    return redirect('viewmessage')
def inbox(request):
    senderid=request.session['id']
    status=['deleted by sender','pending']
    
    agefactor=customiseagefactor_tb.objects.filter(userid=senderid)
    print("factor",agefactor)
    for factor in agefactor:
        msg=message_tb.objects.filter(recieverid=senderid,filter_status='pending',message__icontains=factor.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(useridd=senderid).values('contactidd')).update(filter_status="filtered")
   

    
    hobbyfactor=customisehobbyfactor_tb.objects.filter(userid=senderid)
    print("hobbyfactor",hobbyfactor)
    for hobby in hobbyfactor:
        msg=message_tb.objects.filter(recieverid=senderid,filter_status='pending',message__icontains=hobby.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(useridd=senderid).values('contactidd')).update(filter_status="filtered")
   

    seasoncountryfactor=customiseseasoncountry_tb.objects.filter(userid=senderid)
    print("seasoncf",seasoncountryfactor)
    for seasoncountry in seasoncountryfactor:
        f=seasoncountry.factorid.factorname
        print("fact",f)
        print(seasoncountry)
        msg=message_tb.objects.filter(recieverid=senderid,filter_status='pending',message__icontains=seasoncountry.factorid.factorname).exclude(senderid__in=blacklist_tb.objects.filter(useridd=senderid).values('contactidd')).update(filter_status="filtered")



    contact=contact_tb.objects.filter(userid=senderid)
    for c in contact:
        msg=message_tb.objects.filter(recieverid=senderid,filter_status='pending',senderid=c.contactid).update(filter_status="filtered")
    messages=message_tb.objects.filter(recieverid=senderid,status__in=status,filter_status="filtered").exclude(id__in=trash_tb.objects.filter(recieverid=senderid).values('messageid_id'))
    return render(request,'inbox.html',{'data':messages})
def forward(request,uid):
    forward=message_tb.objects.filter(id=uid)
    return render(request,'forward.html',{'data':forward})
def forwardAction(request):
    senderid=request.session['id']
    senderid_obj=register_tb.objects.get(id=senderid)
    recieverid=request.POST['recieverid']
    recieverid_obj=register_tb.objects.get(username=recieverid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    mess=message_tb(senderid=senderid_obj,recieverid=recieverid_obj,subject=subject,message=message,date=date,time=time)
    mess.save()
    messages.add_message(request,messages.INFO,"Forwarded")
    return redirect('inbox')
def reply(request,uid):
    reply=message_tb.objects.filter(id=uid)
    return render(request,'reply.html',{'data':reply})
def replyAction(request):
    senderid=request.session['id']
    senderid_obj=register_tb.objects.get(id=senderid)
    recieverid=request.POST['senderid']
    recieverid_obj=register_tb.objects.get(username=recieverid)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    mess=message_tb(senderid=senderid_obj,recieverid=recieverid_obj,subject=subject,message=message,date=date,time=time)
    mess.save()
    messages.add_message(request,messages.INFO,"Replied")
    return redirect('inbox')
def inboxAction(request):
    uid=request.session['id']
    uid_obj=register_tb.objects.get(id=uid)
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    checkbox=request.POST.getlist('checkbox')
    for messageid in checkbox:
        message_obj=message_tb.objects.get(id=messageid)
        
        inbox=trash_tb(recieverid=uid_obj,date=date,time=time,messageid=message_obj)
        inbox.save()
    return redirect('inbox')
def viewtrash(request):
    uid=request.session['id']
    trash=trash_tb.objects.filter(recieverid=uid)
    return render(request,'viewtrash.html',{'data':trash})
def deletet(request,uid):
    trash=trash_tb.objects.filter(id=uid)
    s=message_tb.objects.filter(id=trash[0].messageid_id)
    status=s[0].status
    if status == "deleted by sender":
        x=message_tb.objects.filter(id=trash[0].messageid_id).delete()
    else:
        message=message_tb.objects.filter(id=trash[0].messageid_id).update(status="deleted by reciever")
    trash.delete()    
    print(s)
    return redirect('viewtrash')
def addcontact(request):
    return render(request,'addcontact.html')
def addcontactAction(request):
    userid=request.session['id']
    userid_obj=register_tb.objects.get(id=userid)
    contact=request.POST['contact']
    contact_obj=register_tb.objects.get(username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    add=contact_tb(contactid=contact_obj,userid=userid_obj,name=name,date=date,time=time,remarks=remarks)
    add.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('addcontact')
def contactcheck(request):
    contact=request.GET['contact']
    user=register_tb.objects.filter(username=contact)
    if len(user)>0:
        msg="exists"
    else:
        msg="not exists"
    return JsonResponse({'valid':msg})
def viewcontact(request):
    uid=request.session['id']
    contact=contact_tb.objects.filter(userid=uid)
    return render(request,'viewcontact.html',{'data':contact})
def blacklist(request):
    return render(request,'blacklist.html')
def blacklistAction(request):
    userid=request.session['id']
    userid_obj=register_tb.objects.get(id=userid)
    contact=request.POST['contact']
    contact_obj=register_tb.objects.get(username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    add=blacklist_tb(contactidd=contact_obj,useridd=userid_obj,name=name,date=date,time=time,remarks=remarks)
    add.save()
    messages.add_message(request,messages.INFO,"Added")
    return redirect('blacklist')
def viewblacklist(request):
    uid=request.session['id']
    blacklist=blacklist_tb.objects.filter(useridd=uid)
    return render(request,'viewblacklist.html',{'data':blacklist})

def deletec(request,uid):
    contact=contact_tb.objects.filter(id=uid).delete()
    return redirect('viewcontact')
def deleteb(request,uid):
    blacklist=blacklist_tb.objects.filter(id=uid).delete()
    return redirect('viewblacklist')
def addtoblacklist(request,uid):
    contact=contact_tb.objects.filter(id=uid)
    name=contact[0].name
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    remarks=contact[0].remarks
    contactid=contact[0].contactid
    userid=contact[0].userid
    addtobl=blacklist_tb(name=name,date=date,time=time,remarks=remarks,contactidd=contactid,useridd=userid)
    addtobl.save()
    delete=contact_tb.objects.filter(id=uid).delete()
    messages.add_message(request,messages.INFO,"Added to blacklist")
    return redirect('viewcontact')
def customisehobbyfactor(request):
    uid=request.session['id']
  
    hobby=customer_hobby_tb.objects.filter(userid=uid)
   
    return render(request,'customisehobbyfactor.html',{'data':hobby})
    
def getfactor(request):
    hobbyid=request.GET['hobbyid']
    print("hobbyid",hobbyid)

    factor=hobby_factor_tb.objects.filter(hobbyid=hobbyid)
    print(factor)
    return render(request,'getfactor.html',{'data':factor})
def customisehobbyfactorAction(request):
    userid=request.session['id']
    userid_obj=register_tb.objects.get(id=userid)
    print("1",userid_obj)
    factorid=request.POST['factor']
    print("2",factorid)
    factorid_obj=hobby_factor_tb.objects.get(id=factorid)
    hobbyid=request.POST['hobby']
    print("3",hobbyid)
    hobbyid_obj=hobby_name_tb.objects.get(id=hobbyid)
    print("4",hobbyid_obj)
    chf=customisehobbyfactor_tb(factorid=factorid_obj,userid=userid_obj,hobbyid=hobbyid_obj)
    chf.save()
    messages.add_message(request,messages.INFO,"Submitted")
    return redirect('customisehobbyfactor')
def customiseagefactor(request):
    userid=request.session['id']
    userdetails=register_tb.objects.filter(id=userid)
    dob=userdetails[0].dob
    year=dob.split('-')
    y=year[0]
    print(y)
    
    date=datetime.date.today()
    currentyear=date.year
    age=currentyear-int(y)
    print(age)
    agefactor=agefactor_tb.objects.filter(minimumage__lte=age,maximumage__gte=age)
    print(agefactor)
    return render(request,'customiseagefactor.html',{'data':agefactor})
def customiseagefactorAction(request):
    userid=request.session['id']
    userid_obj=register_tb.objects.get(id=userid)
    factorid=request.POST['factor']
    factorid_obj=hobby_factor_tb.objects.get(id=factorid)
    caf=customiseagefactor_tb(userid=userid_obj,factorid=factorid_obj)
    caf.save()
    messages.add_message(request,messages.INFO,"ADDED")
    return redirect('customiseagefactor')

def customiseseasoncountry(request):
    userid=request.session['id']
    userdetails=register_tb.objects.filter(id=userid)
    country=userdetails[0].country
    state=userdetails[0].state
    date=datetime.date.today()
    currentmonth=date.month
    customiseseasoncountry=seasoncountry_tb.objects.filter(countryid=country,stateid=state,month=currentmonth)
    return render(request,'customiseseasoncountry.html',{'data':customiseseasoncountry})
def customiseseasoncountryAction(request):
    userid=request.session['id']
    userid_obj=register_tb.objects.get(id=userid)
    factorid=request.POST['factor']
    factorid_obj=seasonfactor_tb.objects.get(id=factorid)
    caf=customiseseasoncountry_tb(userid=userid_obj,factorid=factorid_obj)
    caf.save()
    messages.add_message(request,messages.INFO,"ADDED")
    return redirect('customiseseasoncountry')
def updateProfile(request):
    uid=request.session['id']
    user=register_tb.objects.filter(id=uid)
    country=country_tb.objects.all()
    hobby=hobby_name_tb.objects.all()
    customerhobby=customer_hobby_tb.objects.filter(userid=uid)
    return render(request,'updateProfile.html',{'data1':user,'data2':country,'data3':hobby,'data4':customerhobby})
def updateProfileAction(request):
    uid=request.session['id']
    uid_obj=register_tb.objects.get(id=uid)
    name=request.POST['name']
    gender=request.POST['gender']
    dob=request.POST['dob']
    address=request.POST['address']
    phone=request.POST['phone']
    country=request.POST['country']
    print(country)
    country_obj=country_tb.objects.get(id=country)
    print(country_obj)
    state=request.POST['state']
    print(state)
    state_obj=state_tb.objects.get(id=state)
    print(state_obj)
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    delete=customer_hobby_tb.objects.filter(userid=uid_obj).delete()
    register=register_tb.objects.filter(id=uid).update(name=name,gender=gender,dob=dob,address=address,phone=phone,country=country_obj,state=state_obj,securityquestion=securityquestion,answer=answer,username=username,password=password)
    hobby=request.POST.getlist('hobby')
    print(hobby)
    for hid in hobby:
        hobby_obj=hobby_name_tb.objects.get(id=hid)
        print("hobby",hobby_obj)
        hobbys=customer_hobby_tb(hobbyid=hobby_obj,userid=uid_obj)
        hobbys.save()
    messages.add_message(request,messages.INFO,"Updated")
    return redirect('updateProfile')
def logout(request):
    request.session.flush()
    messages.add_message(request,messages.INFO,"Logged out")
    return render(request,'login.html')
def forgotpassword(request):
    return render(request,'forgotpassword.html')
def forgotAction(request):
    username=request.POST['username']
    print(username)
    user=register_tb.objects.filter(username=username)
    print(user)
    country=country_tb.objects.all()
    if user.count()>0:
        return render(request,'forgotAction.html',{'data':user,'data1':country})
    else:
        messages.add_message(request,messages.INFO,"Username doesn't match")
    return redirect('forgotpassword')
def forgotpassAction(request):
    country=request.POST['country']
    state=request.POST['state']
    dob=request.POST['dob']
    securityquestion=request.POST['securityquestion']
    answer=request.POST['answer']
    user=register_tb.objects.filter(country=country,state=state,dob=dob,securityquestion=securityquestion,answer=answer)
    if user.count()>0:
        return render(request,'confirmationpassword.html',{'data':user})
    else:
        messages.add_message(request,messages.INFO,"It doesnt match")
        return redirect('forgotpassword')
    
def confirmationpasswordAction(request):
    username=request.POST['username']
    newpassword=request.POST['newpassword']
    confpassword=request.POST['confirmationpassword']
    username_obj=register_tb.objects.filter(username=username)
    if newpassword == confpassword:
        user=register_tb.objects.filter(username=username).update(password=newpassword)
        messages.add_message(request,messages.INFO,"Password successfully reset")
        return redirect('login')
    else:
        messages.add_message(request,messages.INFO,"Entered password and confirmation password doesnt match")
        return render(request,'confirmationpassword.html',{'data':username_obj})
    
def recievercheck(request):
    reciever=request.GET['reciever']
    user=register_tb.objects.filter(username=reciever)
    if len(user)>0:
        msg="exists"
    else:
        msg="not exists"
    return JsonResponse({'valid':msg})

    

