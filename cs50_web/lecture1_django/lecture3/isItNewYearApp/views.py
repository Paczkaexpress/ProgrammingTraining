from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    today = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "isnewyear": today.day == 1 and today.month == 1
    })