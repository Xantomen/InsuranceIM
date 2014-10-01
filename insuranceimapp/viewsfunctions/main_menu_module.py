
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def main_menu(request):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    the_user = request.user
    
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""

    try:
        group_name = request.POST['group_text_field']

    except:
        group_name = ""
        
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    belonging_groups_list = user_profile.getGroupsList()
    
    print action_to_execute
    
    if group_name:
        if action_to_execute == "join_group":
            try:
                group = Group.objects.get(name = group_name)
                group_profile = GroupProfile.objects.get(group = group)
                group_profile.addMember(user_profile)
                user_profile.addGroup(group_profile)
                print "JOINING GROUP"
            except:
                print "NO GROUP CALLED LIKE THAT"
        if action_to_execute == "create_new_group":
            try:
                group = Group(name = group_name)
                group.save()
                group_profile = GroupProfile.objects.get(group = group)
                group_profile.addMember(user_profile)
                user_profile.addGroup(group_profile)
                print "CREATING GROUP"
            except:
                print "COULDN'T CREATE GROUP"
            
    if action_to_execute == "go_to_options_menu":  
        return HttpResponseRedirect(reverse('insuranceimapp:options_menu', args=()))
       
    context = {'belonging_groups_list':belonging_groups_list,"the_user":the_user}
    return render(request,'insuranceimapp/main_menu.html',context)