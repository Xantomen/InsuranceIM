
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def superuser_main_menu(request):
    
    if not request.user.is_authenticated() or not request.user.is_superuser:
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    the_user = request.user
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""
       
    if action_to_execute == "register_new_group_button":

        return HttpResponseRedirect(reverse('insuranceimapp:register_new_group_and_teamlead', args=()))
    if action_to_execute == "logout":
      
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))

 
    return render(request,'insuranceimapp/superuser_main_menu.html')