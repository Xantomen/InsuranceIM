import datetime
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User,Group
from django.db.models.signals import post_save


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
    
    def setContent(self,content):
        if content:
            self.content = content
    
    def setPushed(self,state):
        if state == True:
           self.pushed = 'pushed'
        else:
           self.pushed = 'not_pushed'
           
    def setSender(self,sender):
        if sender:
            self.sender = sender
    
    def addReceiverUser(self,receiver):
        if receiver:
            self.receiver_users.add(receiver)
    
    def addReceiverGroup(self,receiver):
        if receiver:
            self.receiver_groups.add(receiver)
      
class Report(models.Model):  
    action = models.CharField(max_length=63,default='')
    subaction = models.CharField(max_length=63,default='')
    description = models.CharField(max_length=255,default='')
    user_responsible = models.ForeignKey(User, null=True, blank=True, default=None)
    users_affected = models.ManyToManyField(User,related_name='users_affected', null=True, blank=True, default=None)
    groups_affected = models.ManyToManyField(Group,related_name='groups_affected', null=True, blank=True, default=None)
    messages_affected = models.ManyToManyField(Message,related_name='groups_affected', null=True, blank=True, default=None)
    
    def __str__(self):  
          return self.description     
      
    def setAction(self,action):
        if action:
            self.action = action
            
    def setSubAction(self,subaction):
        if subaction:
            self.subaction = subaction
            
    def setDescription(self,description):
        if description:
            self.description = description
            
    def setUserResponsible(self,user_responsible):
        if user_responsible:
            self.user_responsible = user_responsible
            
    def addUserAffected(self,user_affected):
        if user_affected:
            self.users_affected.add(user_affected)
            
    def addGroupAffected(self,group_affected):
        if group_affected:
            self.groups_affected.add(group_affected)
        
    def addMessageAffected(self,message_affected):
        if message_affected:
            self.messages_affected.add(message_affected)
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
    #groups_list = models.ManyToManyField('GroupProfile',related_name='groups_list', null=True, blank=True, default=None)
    #user_company = models.ForeignKey(Group,null=True,blank=True)
    #modifiedsourcepdfs_categorization_tool = models.ManyToManyField(SourcePdf,related_name='sourcepdfs_modified_categorization_tool', null=True, blank=True, default=None)
    
    
    #other fields here
    
    def __str__(self):  
          return "%s's profile" % self.user 
   
    def setPhonenumberPrefix(self,phonenumber_prefix):
        if phonenumber_prefix:
            self.phonenumber_prefix = phonenumber_prefix
            
    def setPhonenumber(self,phonenumber):
        if phonenumber:
            self.phonenumber = phonenumber
            
    def setPushed(self,state):
        if state == True:
           self.user_active = 'active'
        else:
           self.user_active = 'not_active'
           
    def addContact(self,contact):
        if contact:
            self.contacts_list.add(contact)
            
    def addUnreadMessage(self,message):
        if message:
            self.unread_messages.add(message)
            
    def addReadMessage(self,message):
        if message:
            self.read_messages.add(message)
            
    def addGroup(self,group):
        if message:
            self.groups_list.add(group)
    
    
     
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        
        profile, created = UserProfile.objects.get_or_create(user=instance)  

        
post_save.connect(create_user_profile, sender=User)



class GroupProfile(models.Model):  
    group = models.OneToOneField(Group)
    group_active = models.CharField(max_length=31,default='active')
    members_list = models.ManyToManyField(User,related_name='members_list', null=True, blank=True, default=None)
    
    
    def __str__(self):  
          return "%s's profile" % self.group
      
    def setActive(self,state):
        if state == True:
           self.group_active = 'active'
        else:
           self.group_active = 'not_active'
      
    def addMember(self,member):
        if member:
            self.members_list.add(member)

     
def create_group_profile(sender, instance, created, **kwargs):  
    if created:  
        
        profile, created = GroupProfile.objects.get_or_create(group=instance)  

        
post_save.connect(create_group_profile, sender=Group)

