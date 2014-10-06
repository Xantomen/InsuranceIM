from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

from django.shortcuts import get_object_or_404, render, redirect,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.views import generic
from django.utils import timezone


from insuranceimapp.viewsfunctions import (app_index_module,app_login_module,register_new_group_and_teamlead_module,
                                           superuser_main_menu_module,teamlead_main_menu_module,
                                           options_menu_module,user_main_menu_module,add_sale_success_module,
                                           add_members_module,leaderboard_module)

from insuranceimapp.models import *

def maintenance_screen(request):
  
    return render(request,'insuranceimapp/maintenance_screen.html',context)

def app_login(request):
  
    return app_login_module.app_login(request)

def register_new_group_and_teamlead(request):

    return register_new_group_and_teamlead_module.register_new_group_and_teamlead(request)
    
def app_index(request):
    
    return app_index_module.app_index(request)

def superuser_main_menu(request):
    
    return superuser_main_menu_module.superuser_main_menu(request)

def teamlead_main_menu(request):
    
    return teamlead_main_menu_module.teamlead_main_menu(request)

def user_main_menu(request):
    
    return user_main_menu_module.user_main_menu(request)

def add_members(request):
    
    return add_members_module.add_members(request)

def add_sale_success(request):
    
    return add_sale_success_module.add_sale_success(request)

def leaderboard(request):
    
    return leaderboard_module.leaderboard(request)


def options_menu(request):
    
    return options_menu_module.options_menu(request)
    