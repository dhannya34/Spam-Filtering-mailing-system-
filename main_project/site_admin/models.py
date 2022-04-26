from django.db import models

# Create your models here.

class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class hobby_name_tb(models.Model):
    hobbyname=models.CharField(max_length=20)
class country_tb(models.Model):
    country=models.CharField(max_length=20)
class state_tb(models.Model):
    state=models.CharField(max_length=20)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
class register_tb(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    country=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    state=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    securityquestion=models.CharField(max_length=20)
    answer=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class customer_hobby_tb(models.Model):
    hobbyid=models.ForeignKey('site_admin.hobby_name_tb',on_delete=models.CASCADE)
    userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
class hobby_factor_tb(models.Model):
    hobbyid=models.ForeignKey(hobby_name_tb,on_delete=models.CASCADE)
    factorname=models.CharField(max_length=20)
class agefactor_tb(models.Model):
    minimumage=models.IntegerField(default=2)
    maximumage=models.IntegerField()
    factorname=models.CharField(max_length=20)
class season_tb(models.Model):
    seasonname=models.CharField(max_length=20)
class seasonfactor_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    factorname=models.CharField(max_length=20)
class seasoncountry_tb(models.Model):
    seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    stateid=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    factorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    month=models.CharField(max_length=20)
    
    
    
    
