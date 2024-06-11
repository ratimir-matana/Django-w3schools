# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

# Create your views here.


# # Note: The name of the view function does not have to be the same as the application. 
# # I call it 'members' because I think it fits well in this context.

# def members(request):
#     # Simple example how to send a HTTP response (Hello world! message) back to the browser.
#     return HttpResponse("Hello world!")

# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

def members(request):
   club_members = Member.objects.all().values()      
   template = loader.get_template('all_members.html')    
   context = {
       'club_members': club_members,                    
   }
   return HttpResponse(template.render(context, request))


def details(request, id):        
   club_member = Member.objects.get(id=id)    
   template = loader.get_template('details.html')    
   context = {
       'club_member': club_member,                    
   }
   return HttpResponse(template.render(context, request))


def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())


def testing(request): 
   club_members = Member.objects.all().values()        
   template = loader.get_template('template.html')     
   context = {
       'fruits': ['Apple', 'Banana', 'Cherry'],
       'firstname': 'Linus',
       'club_members': club_members,
       'greeting': 1,
       
   }
   return HttpResponse(template.render(context, request))


