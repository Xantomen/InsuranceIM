
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
 

def pushMessagesFromGroupToReceivers(group_profile):
    
    try:

        if group_profile.group_active == "active":

            all_messages_from_group = Message.objects.filter(receiver_groups = group_profile)

            all_messages_not_pushed = all_messages_from_group.exclude(pushed = "pushed")

            for temp_message in all_messages_not_pushed:

                all_receiver_users = temp_message.getReceiverUsers()

                for temp_user in all_receiver_users:
    
                    temp_user.addUnreadMessage(temp_message)

                temp_message.setPushed(True) 

                temp_message.save()

        print "SUCCESS IN PUSHING MESSAGES TO RECEIVERS"
        return True        
    except:
        print "FAILURE IN PUSHING MESSAGES TO RECEIVERS"
        return False
        