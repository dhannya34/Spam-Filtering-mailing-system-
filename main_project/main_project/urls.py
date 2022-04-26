"""main_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from site_admin import views as adminview
from site_user import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',adminview.index,name='index'),
    url(r'^login/$',adminview.login,name='login'),
    url(r'^loginAction/$',adminview.loginAction,name='loginAction'),
    url(r'^addhobby/$',adminview.addhobby,name='addhobby'),
    url(r'^addhobbyAction/$',adminview.addhobbyAction,name='addhobbyAction'),
    url(r'^register/$',adminview.register,name='register'),
    url(r'^getstate/$',adminview.getstate,name='getstate'),
    url(r'^registerAction/$',adminview.registerAction,name='registerAction'),
    url(r'^checkusername/$',adminview.checkusername,name='checkusername'),
    url(r'^addhobbyfactor/$',adminview.addhobbyfactor,name='addhobbyfactor'),
    url(r'^addhobbyfactorAction/$',adminview.addhobbyfactorAction,name='addhobbyfactorAction'),
    url(r'^addagefactor/$',adminview.addagefactor,name='addagefactor'),
    url(r'^addagefactorAction/$',adminview.addagefactorAction,name='addagefactorAction'),
    url(r'^addseason/$',adminview.addseason,name='addseason'),
    url(r'^addseasonAction/$',adminview.addseasonAction,name='addseasonAction'),
    url(r'^addseasonfactor/$',adminview.addseasonfactor,name='addseasonfactor'),
    url(r'^addseasonfactorAction/$',adminview.addseasonfactorAction,name='addseasonfactorAction'),
    url(r'^addseasoncountryfactor/$',adminview.addseasoncountryfactor,name='addseasoncountryfactor'),
    url(r'^addseasoncountryfactorAction/$',adminview.addseasoncountryfactorAction,name='addseasoncountryfactorAction'),
    url(r'^compose/$',userview.compose,name='compose'),
    url(r'^composeAction/$',userview.composeAction,name='composeAction'),
    url(r'^viewmessage/$',userview.viewmessage,name='viewmessage'),
    url(r'^delete/(?P<uid>\d+)/$',userview.delete,name='delete'),
    url(r'^inbox/$',userview.inbox,name='inbox'),
    url(r'^forward/(?P<uid>\d+)/$',userview.forward,name='forward'),
    url(r'^forwardAction/$',userview.forwardAction,name='forwardAction'),
    url(r'^reply/(?P<uid>\d+)/$',userview.reply,name='reply'),
    url(r'^replyAction/$',userview.replyAction,name='replyAction'),
    url(r'^inboxAction/$',userview.inboxAction,name='inboxAction'),
    url(r'^viewtrashr/$',userview.viewtrash,name='viewtrash'),
    url(r'^deletet/(?P<uid>\d+)/$',userview.deletet,name='deletet'),
    url(r'^addcontact/$',userview.addcontact,name='addcontact'),
    url(r'^addcontactAction/$',userview.addcontactAction,name='addcontactAction'),
    url(r'^contactcheck/$',userview.contactcheck,name='contactcheck'),
    url(r'^viewcontact/$',userview.viewcontact,name='viewcontact'),
    url(r'^blacklist/$',userview.blacklist,name='blacklist'),
    url(r'^blacklistAction/$',userview.blacklistAction,name='blacklistAction'),
    url(r'^viewblacklist/$',userview.viewblacklist,name='viewblacklist'),
    url(r'^deletec/(?P<uid>\d+)/$',userview.deletec,name='deletec'),
    url(r'^deleteb/(?P<uid>\d+)/$',userview.deleteb,name='deleteb'),
    url(r'^addtoblacklist/(?P<uid>\d+)/$',userview.addtoblacklist,name='addtoblacklist'),
    url(r'^customisehobbyfactor/$',userview.customisehobbyfactor,name='customisehobbyfactor'),
    url(r'^getfactor/$',userview.getfactor,name='getfactor'),
    url(r'^customisehobbyfactorAction/$',userview.customisehobbyfactorAction,name='customisehobbyfactorAction'),
    url(r'^customiseagefactor/$',userview.customiseagefactor,name='customiseagefactor'),
    url(r'^customiseagefactorAction/$',userview.customiseagefactorAction,name='customiseagefactorAction'),
    url(r'^customiseseasoncountry/$',userview.customiseseasoncountry,name='customiseseasoncountry'),
    url(r'^customiseseasoncountryAction/$',userview.customiseseasoncountryAction,name='customiseseasoncountryAction'),
    url(r'^updateProfile/$',userview.updateProfile,name='updateProfile'),
    url(r'^updateProfileAction/$',userview.updateProfileAction,name='updateProfileAction'),
    url(r'^logout/$',userview.logout,name='logout'),
    url(r'^forgotpassword/$',userview.forgotpassword,name='forgotpassword'),
    url(r'^forgotAction/$',userview.forgotAction,name='forgotAction'),
    url(r'^forgotpassAction/$',userview.forgotpassAction,name='forgotpassAction'),
    url(r'^confirmationpasswordAction/$',userview.confirmationpasswordAction,name='confirmationpasswordAction'),
    url(r'^logout/$',adminview.logout,name='logout'),
    url(r'^recievercheck/$',userview.recievercheck,name='recievercheck'),
]
