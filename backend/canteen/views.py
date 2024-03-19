from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def Veg(request):
  template = loader.get_template('c1.html')
  return HttpResponse(template.render())

def NVeg(request):
  template = loader.get_template('c2.html')
  return HttpResponse(template.render())