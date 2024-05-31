from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.
def home(request,year,month):
    name="Gulim"
    # convert name to number
    month=month.capitalize()
    month_number=list(calendar.month_name).index(month)
    month_number=int(month_number)
    #current year
    now=datetime.now()
    current_year=now.year
    # get current time
    time=now.strftime('%I:%M %p')
    # create Calendar
    cal=HTMLCalendar().formatmonth(year,month_number)
    return render(request,'Home.html',
                  {
                      "name":name,
                      "year":year,
                      "month":month,
                      "month_number":month_number,
                      "cal":cal,
                      "current_year":current_year,
                      "time":time,
                  }
                  )