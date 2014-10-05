
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def register_new_group_and_teamlead(request):

  
    the_user = request.user;
    
    groups_list = Group.objects.exclude(name = "AdminGroup")
    
    if not the_user.is_superuser:
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    error_message= "NO ERROR"
    
    if request.POST:

        try:
            group_name = request.POST['group_name']
            print "Debug01"
            username = request.POST['username']
            print "Debug02"
            email = request.POST['email']
            print "Debug03"
            password = request.POST['password'].encode('ascii','replace')
            print "Debug04"
            repeat_password = request.POST['repeat_password'].encode('ascii','replace')
            print "Debug05"
            
            username_exists = User.objects.filter(username = username)
            print "Debug06"
            if group_name and password and email and password == repeat_password and not len(username_exists):
                print "Debug07"
                group, group_name_exists = Group.objects.get_or_create(name = group_name)
                print "Debug08"
                group_profile = GroupProfile.objects.get(group = group)
                print "Debug09"
                user = User.objects.create_user(username = username, password = repeat_password, email = email)
                #user.username = username
                #user.set_password(repeat_password)
                print "Debug10"
                user.is_staff = False
                user.is_active = True
                user.groups.add(group)
                print "Debug11"
                user.save()
                print "Debug12"
                user_profile = UserProfile.objects.get(user = user)
                user_profile.user_category = "teamleader"
                print "Debug13"
                user_profile.addGroup(group_profile)
                print "Debug14"
                group_profile.addMember(user_profile)
                print "Debug15"
                #user_profile.save()
                error_message = "IT ALL WORKED"    
                
            else:
                error_message = "ERROR IN INPUT"    
            
        except:
            error_message = "ERROR IN TRY BLOCK"
    
    print error_message
    context = {"groups_list":groups_list}
    return render(request,'insuranceimapp/register_new_group_and_teamlead.html',context)
    