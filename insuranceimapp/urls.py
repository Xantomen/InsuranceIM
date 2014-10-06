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
    url(r'^register_new_group_and_teamlead/$', views.register_new_group_and_teamlead, name='register_new_group_and_teamlead'),
        
    # Note: To access to admin panel, the url is simply /admin
    # Admin already has an authentification mode built in.

    # Main (app_index). Shows the four available modes. Can't access them at the moment
    # ex: /recipeprintoutsapp/
    url(r'^$', views.app_index, name='app_index'),   
    
    #
    # User Main menu (main_menu). Create new Group + TeamLeader
    # ex: /insuranceimapp/superuser_main_menu
    url(r'^superuser_main_menu', views.superuser_main_menu, name='superuser_main_menu'),   

    #
    # Team Leader Main menu (teamlead_main_menu). Shows the main available options: Find Group, New Group, Options
    # ex: /insuranceimapp/main_menu
    url(r'^teamlead_main_menu', views.teamlead_main_menu, name='teamlead_main_menu'),   

    #
    # Team Leader Add Members (to Group) UI (add_members). 
    # Shows a form that can be field to add a single member, with the fields:
    # First Name, First letter of family name, zip code, city, 6 digit code
    # It also has a button "Add Member List from file", that reads from a text file / csv file and
    # adds members to the table.
    # When pressing the button "Save", the program will try to create those Users, returning
    # any warnings or errors if it wasn't possible, stating the reason why.
    # The page also shows a table, in which each user is one line, and let's the leader update the fields or
    # delete members.
    
    # ex: /insuranceimapp/add_members
    url(r'^add_members', views.add_members, name='add_members'),  
    
    
    #
    # Options menu (options_menu). Shows the available options: Logout, Deactivate User, Edit Profile
    # ex: /insuranceimapp/options_menu
    #url(r'^options_menu', views.options_menu, name='options_menu'), 

)