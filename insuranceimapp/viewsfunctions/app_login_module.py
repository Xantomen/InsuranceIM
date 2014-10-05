
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def app_login(request):
  
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user_profile = UserProfile.objects.get(user = user)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse('insuranceimapp:superuser_main_menu', args=()))
                if user_profile.user_category == "user":
                    login(request, user)
                    #return HttpResponseRedirect('enersectapp:main')
                    return HttpResponseRedirect(reverse('insuranceimapp:main_menu', args=()))
                    #return reverse('enersectapp:main', args=())
                elif user_profile.user_category == "teamleader":
                    login(request, user)
                    return HttpResponseRedirect(reverse('insuranceimapp:teamlead_main_menu', args=()))
                
    return render_to_response('insuranceimapp/app_login.html', context_instance=RequestContext(request))