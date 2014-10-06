
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def user_main_menu(request):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    the_user = request.user
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    if not user_profile.user_category == "user":
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""
       
    
    group_profile = user_profile.getOrAddGroupProfile()
    messages_list = user_profile.getUnreadMessages()
    
    if action_to_execute == "add_sale_success":
        return HttpResponseRedirect(reverse('insuranceimapp:add_sale_success', args=()))
    if action_to_execute == "logout":
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))

       
    context = {"group_profile":group_profile,"messages_list":messages_list}
    return render(request,'insuranceimapp/user_main_menu.html',context)