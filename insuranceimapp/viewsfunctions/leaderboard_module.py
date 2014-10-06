
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def add_members(request):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    the_user = request.user
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    if not user_profile.user_category == "teamleader":
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""
       
    
    group_profile = user_profile.getOrAddGroupProfile()
    
    
    if action_to_execute == "add_members":
        return HttpResponseRedirect(reverse('insuranceimapp:add_members', args=()))
    if action_to_execute == "leaderboard":
        return HttpResponseRedirect(reverse('insuranceimapp:leaderboard', args=()))
    if action_to_execute == "logout":
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))

       
    context = {"group_profile":group_profile}
    return render(request,'insuranceimapp/teamlead_main_menu.html',context)