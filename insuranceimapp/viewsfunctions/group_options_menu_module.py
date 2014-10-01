
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def group_options_menu(request,group_name):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    the_user = request.user
    
    group = Group.objects.get(name = group_name)
    group_profile = GroupProfile.objects.get(group = group)
    
    user_profile = UserProfile.objects.get(user = the_user)

    is_user_in_group = group_profile.members_list.filter(user = the_user)
    #If the user isn't part of the group, he shouldn't have access to it, and is returned
    #to the main menu instead    
    if len(is_user_in_group) == 0:
        
        return HttpResponseRedirect(reverse('insuranceimapp:main_menu', args=()))
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""

    try:
        chosen_username = request.POST['chosen_username']

    except:
        chosen_username = ""
        
    try:
        message_to_send = request.POST['message_to_send']

    except:
        message_to_send = ""
        
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    belonging_users_list = group_profile.getMembersList().exclude(user = the_user)
    
    if group_name:
        if action_to_execute == "send_message_to_user":
            try:
                '''group = Group.objects.get(name = group_name)
                group_profile = GroupProfile.objects.get(group = group)
                group_profile.addMember(user_profile)
                user_profile.addGroup(group_profile)'''
                print "SENDING MESSAGE TO USER"
            except:
                print "CANT SEND MESSAGE TO USER"
        if action_to_execute == "unsubscribe_from_group":
            try:
                '''group = Group(name = group_name)
                group.save()
                group_profile = GroupProfile.objects.get(group = group)
                group_profile.addMember(user_profile)
                user_profile.addGroup(group_profile)'''
                print "UNSUBSCRIBED FROM GROUP"
            except:
                print "COULDN'T UNSUBSCRIBE GROUP"
        
           
    if action_to_execute == "back_to_main_menu":  
        print "RETURNING TO MAIN MENU"
        return HttpResponseRedirect(reverse('insuranceimapp:main_menu', args=()))
       
    context = {'belonging_users_list':belonging_users_list,"the_user":the_user,"group_name":group_name}
    return render(request,'insuranceimapp/group_options_menu.html',context)