from django.shortcuts import render
import calendar
# Create your views here.
def home(request):
    return render(request,'Home.html',{})