from django.shortcuts import render

# Create your views here.
import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def show_todo_list(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)