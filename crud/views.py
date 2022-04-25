from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def home(request):
    details = Details.objects.all()
    return render(request, "crud_templates/index.html", {"details":details})


def add_details(request):
    if request.method == 'POST':
        item = Details()
        item.roll = request.POST.get('rn')
        item.name = request.POST.get('name')
        item.age = request.POST.get('age')
        item.save()
        return redirect('/')
    return render(request,"crud_templates/add_details.html")


def edit(request, roll):
    item = Details.objects.get(roll=roll)
    Details.objects.get(roll=roll).delete()
    return render(request, "crud_templates/edit.html", {"item": item})


def delete(request, roll):
    Details.objects.get(roll=roll).delete()
    return redirect('/')