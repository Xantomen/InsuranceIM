
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
import json

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import Context, loader , RequestContext
 
# list of mobile User Agents
mobile_uas = [
    'w3c ','acs-','alav','alca','amoi','audi','avan','benq','bird','blac',
    'blaz','brew','cell','cldc','cmd-','dang','doco','eric','hipt','inno',
    'ipaq','java','jigs','kddi','keji','leno','lg-c','lg-d','lg-g','lge-',
    'maui','maxo','midp','mits','mmef','mobi','mot-','moto','mwbp','nec-',
    'newt','noki','oper','palm','pana','pant','phil','play','port','prox',
    'qwap','sage','sams','sany','sch-','sec-','send','seri','sgh-','shar',
    'sie-','siem','smal','smar','sony','sph-','symb','t-mo','teli','tim-',
    'tosh','tsm-','upg1','upsi','vk-v','voda','wap-','wapa','wapi','wapp',
    'wapr','webc','winw','winw','xda','xda-'
    ]
 
mobile_ua_hints = [ 'SymbianOS', 'Opera Mini', 'iPhone' ]
 
 
def mobileBrowser(request):
    ''' Super simple device detection, returns True for mobile devices '''
 
    mobile_browser = False
    ua = request.META.get('HTTP_USER_AGENT', '').lower()[0:4]
 
    if (ua in mobile_uas):
        mobile_browser = True
    else:
        for hint in mobile_ua_hints:
            if request.META['HTTP_USER_AGENT'].find(hint) > 0:
                mobile_browser = True
 
    return mobile_browser

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
        