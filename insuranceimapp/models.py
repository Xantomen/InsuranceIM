import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save

from tzlocal import get_localzone

local_tz = get_localzone()

#Table to organise the different possible views/interfaces (in case there are different tools)

class UserInterfaceType(models.Model):
    name = models.CharField(max_length=255,default='')
    redirection_url = models.CharField(max_length=255,default='')
    def __unicode__(self):
        return self.name
    
    
    
    
class Message(models.Model):  
    content = models.CharField(max_length=63,default='')
    pushed = models.CharField(max_length=15,default='not_pushed')
    sender = models.ForeignKey(User, null=True, blank=True, default=None)
    receiver_users = models.ManyToManyField(User,related_name='receiver_users', null=True, blank=True, default=None)
    receiver_groups = models.ManyToManyField(Group,related_name='receiver_groups', null=True, blank=True, default=None)
    
    
    def __str__(self):  
          return self.content 
      
class Report(models.Model):  
    action = models.CharField(max_length=63,default='')
    subaction = models.CharField(max_length=63,default='')
    description = models.CharField(max_length=255,default='')
    user_responsible = models.ForeignKey(User, null=True, blank=True, default=None)
    users_affected = models.ManyToManyField(User,related_name='users_affected', null=True, blank=True, default=None)
    groups_affected = models.ManyToManyField(Group,related_name='groups_affected', null=True, blank=True, default=None)
    messages_affected = models.ManyToManyField(Message,related_name='groups_affected', null=True, blank=True, default=None)
    
    def __str__(self):  
          return self.content     
#
#
### UserProfile and GroupProfile, to extend the User and Group tables. This are created each time a Group or User is created.    

class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    phonenumber_prefix = models.CharField(max_length=7,default='')
    phonenumber = models.CharField(max_length=31,default='')
    user_active = models.CharField(max_length=31,default='active')
    contacts_list = models.ManyToManyField(User,related_name='contacts_list', null=True, blank=True, default=None)
    unread_messages = models.ManyToManyField(Message,related_name='unread_messages', null=True, blank=True, default=None)
    read_messages = models.ManyToManyField(Message,related_name='read_messages', null=True, blank=True, default=None)
    #user_company = models.ForeignKey(Group,null=True,blank=True)
    #modifiedsourcepdfs_categorization_tool = models.ManyToManyField(SourcePdf,related_name='sourcepdfs_modified_categorization_tool', null=True, blank=True, default=None)
    
    
    #other fields here

    
    def __str__(self):  
          return "%s's profile" % self.user 
   
    
    
     
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        
        profile, created = UserProfile.objects.get_or_create(user=instance)  

        
post_save.connect(create_user_profile, sender=User)



class GroupProfile(models.Model):  
    group = models.OneToOneField(Group)
    group_active = models.CharField(max_length=31,default='active')
    members_list = models.ManyToManyField(User,related_name='members_list', null=True, blank=True, default=None)
    #unique_lot_number_list = models.ManyToManyField(LotNumber,related_name='lot_number_list', null=True, blank=True, default=None)
    
    
    def __str__(self):  
          return "%s's profile" % self.group 

     
def create_group_profile(sender, instance, created, **kwargs):  
    if created:  
        
        profile, created = GroupProfile.objects.get_or_create(group=instance)  

        
post_save.connect(create_group_profile, sender=Group)

