from django.db import models


# Create your models here.

class message_tb(models.Model):
    senderid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='sendername')
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    recieverid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='recievername')
    status=models.CharField(max_length=20,default="pending")
    filter_status=models.CharField(max_length=20,default="pending")
class trash_tb(models.Model):
    messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    recieverid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE)

class contact_tb(models.Model):
    contactid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='contactid')
    userid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='userid')
    name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)
class blacklist_tb(models.Model):
    contactidd=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='contactidd')
    useridd=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE,related_name='useridd')
    name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    remarks=models.CharField(max_length=20)

class customisehobbyfactor_tb(models.Model):
    userid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE)
    hobbyid=models.ForeignKey('site_admin.hobby_name_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey('site_admin.hobby_factor_tb',on_delete=models.CASCADE)
class customiseagefactor_tb(models.Model):
    userid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey('site_admin.hobby_factor_tb',on_delete=models.CASCADE)
class customiseseasoncountry_tb(models.Model):
    userid=models.ForeignKey('site_admin.register_tb',on_delete=models.CASCADE)
    factorid=models.ForeignKey('site_admin.seasonfactor_tb',on_delete=models.CASCADE)
