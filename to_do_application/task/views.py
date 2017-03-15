from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import RequestContext

from task.forms import ItemForm
from task.models import Item

import datetime


@login_required
def save_item_task(request):
    if request.method == 'GET':
        form = ItemForm()
    else:
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render_to_response("success_task.html", RequestContext(request))

    return render(request, 'new_task.html', {'form' : form})


@login_required
def edit_item_task(request, id):
    item_record = Item.objects.get(item_id=id)
    if request.method == 'GET':
        form = ItemForm(instance=item_record)
    else:
        form = ItemForm(request.POST, instance=item_record)
        if form.is_valid():
            form.save(commit=True)
        return render_to_response("success_task.html", RequestContext(request))
    return render(request, 'new_task.html', {'form' : form})


@login_required
def show_todo_list(request):
    results = Item.objects.all()

    return render(request, 'list_task.html', {'results' : results})
