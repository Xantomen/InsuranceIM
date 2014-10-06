
from insuranceimapp.models import *

from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render, redirect,render_to_response
import json

def add_members(request):
    
    if not request.user.is_authenticated():
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    the_user = request.user
    
    the_group = the_user.groups.all()[0]
    
    user_profile = UserProfile.objects.get(user = the_user)
    
    if not user_profile.user_category == "teamleader":
        
        return HttpResponseRedirect(reverse('insuranceimapp:app_login', args=()))
    
    
    try:
        action_to_execute = request.POST['action_to_execute']

    except:
        action_to_execute = ""
       
    
    try:
        users_dictionary_list = request.POST['users_dictionary_string']
        users_dictionary_list = json.loads(users_dictionary_list)

    except:
        users_dictionary_list = []
        
        
    try:
        users_to_delete = request.POST['users_to_delete']

    except:
        users_to_delete = ""
    
    group_profile = user_profile.getOrAddGroupProfile()
    
    users_list = group_profile.members_list.all()
        
    if action_to_execute == "save_changes":
        
        for user_dictionary in users_dictionary_list:
            
            #Case: If user already existed (user_profile already had a pk)
            
            
            if len(user_dictionary["pk"]):
                
                is_changed = False
                
                temp_user_profile = UserProfile.objects.get(pk = user_dictionary["pk"])
                
                if temp_user_profile.first_name != user_dictionary["first_name"]:
                    
                    temp_user_profile.first_name = user_dictionary["first_name"]
                    is_changed = True
                    
                if temp_user_profile.surname_first_letter != user_dictionary["surname_first_letter"]:
                    
                    temp_user_profile.surname_first_letter = user_dictionary["surname_first_letter"]
                    is_changed = True
                    
                if temp_user_profile.zipcode != user_dictionary["zipcode"]:
                    
                    temp_user_profile.zipcode = user_dictionary["zipcode"]
                    is_changed = True
                    
                if temp_user_profile.city != user_dictionary["city"]:
                    
                    temp_user_profile.city = user_dictionary["city"]
                    is_changed = True
                    
                if temp_user_profile.six_digit_code != user_dictionary["six_digit_code"]:
                    
                    temp_user_profile.six_digit_code = user_dictionary["six_digit_code"]
                    is_changed = True
                
                
                if is_changed:
                    
                    temp_user_profile.save()
            
 
            #Case: If user didn't exist yet (New user, doesn't have a pk)    
            else:
   
                shaped_username = user_dictionary["first_name"] + user_dictionary["surname_first_letter"][:1] + user_dictionary["six_digit_code"][0:1]

                username_exists = User.objects.filter(username = shaped_username)

                if group_profile and user_dictionary["first_name"] and user_dictionary["surname_first_letter"] and user_dictionary["zipcode"] and user_dictionary["city"] and user_dictionary["six_digit_code"] and not len(username_exists):
  
                    user = User.objects.create_user(username = shaped_username, password = user_dictionary["six_digit_code"], email = "notemail@notemail.com")

                    user.is_staff = False
                    user.is_active = True
                    
                    user.first_name = user_dictionary["first_name"]
                    user.last_name = user_dictionary["first_name"]
                    
                    user.groups.add(the_group)
                    
                    user.save()

                    temp_user_profile = UserProfile.objects.get(user = user)
    
                    temp_user_profile.user_category = "user"
                    
                    temp_user_profile.first_name = user_dictionary["first_name"]
                    temp_user_profile.surname_first_letter = user_dictionary["surname_first_letter"]
                    temp_user_profile.zipcode = user_dictionary["zipcode"]
                    temp_user_profile.city = user_dictionary["city"]
                    temp_user_profile.six_digit_code = user_dictionary["six_digit_code"]
                    
                    temp_user_profile.save()
                    
                    temp_user_profile.addGroup(group_profile)
       
                    group_profile.addMember(temp_user_profile)
       
                    error_message = "IT ALL WORKED"
                
                print "USER DIDNT EXIST"
                
        #Deleting users loop:
        
        user_pk_list = users_to_delete.split(",")
        users_delete_list = UserProfile.objects.none()
        
        for user_pk in user_pk_list:
            
            if user_pk:
            
                users_delete_list = users_delete_list | UserProfile.objects.filter(pk = int(user_pk))
        
        for user_delete in users_delete_list:
            
            user_delete.user.delete()
            user_delete.delete()
            
        
        return HttpResponseRedirect(reverse('insuranceimapp:add_members', args=()))
    if action_to_execute == "leaderboard":
        return HttpResponseRedirect(reverse('insuranceimapp:leaderboard', args=()))
    if action_to_execute == "back_to_menu":
        return HttpResponseRedirect(reverse('insuranceimapp:teamlead_main_menu', args=()))

       
    context = {"group_profile":group_profile,"users_list":users_list}
    return render(request,'insuranceimapp/add_members.html',context)