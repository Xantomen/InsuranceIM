
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response

def register_new_user(request):
  
    the_user = request.user;
    
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password'].encode('ascii','replace')
        repeat_password = request.POST['repeat_password'].encode('ascii','replace')

        username_exists = User.objects.filter(username = username)

        print "PASSWORD -> "+ str(password)
        print "RETYPE PASSWORD -> "+ str(repeat_password)
        print "USERNAME -> "+ str(username)
        print "EMAIL -> "+ str(email)
        print "USER EXISTS? -> "+ str(username_exists)

        if password and email and password == repeat_password and not len(username_exists):
        
            user = User.objects.create_user(username = username, password = repeat_password, email = email)
            #user.username = username
            #user.set_password(repeat_password)
            user.is_staff = False
            user.is_active = True
            user.save()
            
            #user_profile = UserProfile.objects.get(user = user)
            #user_profile.save()
        
            return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
        else:
            return HttpResponseRedirect(reverse('insuranceimapp:register_new_user', args=()))
    else:
        return render(request,'insuranceimapp/register_new_user.html')