#This is the enersectapp urls file

from django.conf.urls import patterns, url

from insuranceimapp import views

urlpatterns = patterns('',

    # Maintenance Screen
    # ex: recipeprintoutsapp/maintenance_screen
    #url(r'^maintenance_screen/$', views.maintenance_screen, name='maintenance_screen'),

    #Log In View when not authentificated
    #return redirect('/login/' % request.path)
    #ex: /recipeprintoutsapp/login/
    url(r'^login/$', views.app_login, name='app_login'),
    
    #Log In View when not authentificated
    #return redirect('/login/' % request.path)
    #ex: /recipeprintoutsapp/login/
    url(r'^login/register_new_user/$', views.register_new_user, name='register_new_user'),
        
    # Note: To access to admin panel, the url is simply /admin
    # Admin already has an authentification mode built in.

    # Main (app_index). Shows the four available modes. Can't access them at the moment
    # ex: /recipeprintoutsapp/
    url(r'^$', views.app_index, name='app_index'),   
    
    #
    # Main menu (main_menu). Shows the main available options: Find Group, New Group, Options
    # ex: /insuranceimapp/main_menu
    url(r'^main_menu', views.main_menu, name='main_menu'),   


    #
    # Options menu (options_menu). Shows the available options: Logout, Deactivate User, Edit Profile
    # ex: /insuranceimapp/options_menu
    url(r'^options_menu', views.options_menu, name='options_menu'), 

)