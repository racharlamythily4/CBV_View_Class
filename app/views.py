from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
#function based views for string

def fbv_string(request):
    return HttpResponse('This is fbv_string data')

#class based views for string

class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is cbv_string data')
    
#fbv for rendering the html page

def fbv_page(request):
    return render(request,'fbv_page.html')

#cbv for rendering the html page
class cbv_page(View):
    def get(self,request):
        return render(request,'cbv_page.html')
    
#rendering fbv_page by form 

def insert_by_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is Inserted')
    return render(request,'insert_by_fbv.html',d)

#rendering cbv_page by form

class insert_by_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'insert_by_cbv.html',d)
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is Inserted')