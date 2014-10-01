
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def options_menu(request):
    
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    the_user = request.user
    
    try:
        action_to_execute = request.POST['action_to_execute']
    except:
        action_to_execute = ""
        
    belonging_groups_list = the_user.groups.all()
    
    if action_to_execute == "join_group":
        print "JOINING GROUP"
    if action_to_execute == "create_new_group":
        print "CREATING GROUP"
    if action_to_execute == "go_to_options_menu":
        print "GO TO OPTIONS"   
        
       
    context = {"the_user":the_user}
    return render(request,'insuranceimapp/options_menu.html',context)