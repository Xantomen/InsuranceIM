
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
import json

def pushMessagesToReceivers(group_profile):
    
    try:
        if group_profile.group_active == "active":
            
            all_messages_from_group = Message.objects.filter(receiver_groups = group_profile)
            all_messages_not_pushed = all_messages_from_group.exclude("pushed")
            
            for message in all_messages_not_pushed:
                
                all_receiver_users = message.receiver_users.all()
                
                for temp_user in all_receiver_users:
                    
                    temp_user.unread_messages.add(message)
                    
                message.pushed = "pushed"
                message.save()
        print "SUCCESS IN PUSHING MESSAGES TO RECEIVERS"        
    except:
        print "FAILURE IN PUSHING MESSAGES TO RECEIVERS"
        