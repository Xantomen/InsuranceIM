
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
import json

from insuranceimapp.viewsfunctions import common_functions_module

def add_sale_success(request):
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    the_user = request.user
    
    the_group = the_user.groups.all()[0]
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    if not user_profile.user_category == "user":
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""
       
    
    try:
        product_name = request.POST['product_name']
    except:
        product_name = ""
    
    try:
        product_value = request.POST['product_value']
    except:
        product_value = ""

    
    group_profile = user_profile.getOrAddGroupProfile()
    
    users_list = group_profile.getMembersList()
    
    
        
    if action_to_execute == "send_message":
        
        try:
            new_message = Message()
            new_message.save()
            
            new_message.setProductName(product_name)
            new_message.setProductValue(product_value)
            new_message.setSender(user_profile)
            new_message.addReceiverGroup(group_profile)
            
            #Comment this line to exclude the sender user from the receivers
            users_in_group_except_myself = group_profile.getMembersList()
            
            
            #Uncomment this line to exclude the sender user from the receivers
            #users_in_group_except_myself = users_in_group_except_myself.exclude(user = user_profile.user)
            
            for temp_user_profile in users_in_group_except_myself:
                
                new_message.addReceiverUser(temp_user_profile)
            
                
            if common_functions_module.pushMessagesFromGroupToReceivers(group_profile):
            
                new_message.setPushed(True) 

                new_message.save()
        
            print "SUCCESFULLY ADDING SALE SUCCESS"
            return HttpResponseRedirect(reverse('insuranceimapp:user_main_menu', args=()))
        except:
            print "FAILURE IN ADDING SALE SUCCESS"
            return HttpResponseRedirect(reverse('insuranceimapp:add_sale_success', args=()))
        
    if action_to_execute == "back_to_menu":
        return HttpResponseRedirect(reverse('insuranceimapp:user_main_menu', args=()))

       
    context = {"group_profile":group_profile}
    return render(request,'insuranceimapp/add_sale_success.html',context)