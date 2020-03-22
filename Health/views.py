from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html") 
def hom(request):
    return render(request, "index_2.html")     
def measles_prevention(request):
    return render(request,"measles_prev.html")
def measles_cure(request):
    return render(request,"measles_cure.html") 
def food_pos(request):
    return render(request,"foodpos_prev.html")
def chickenpox_prev(request):
    return render(request,"chickenpox_prev.html")
     