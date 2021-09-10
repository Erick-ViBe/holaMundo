from django.http import HttpResponse
from django.shortcuts import render
from .models import Task

def home_view(request):
    tasks = Task.objects.all()

    context = {
        'message': 'Tareas por hacer',
        'tasks': tasks,
    }
    return render(request, 'home/index.html', context)


def sum_view(request, num1, num2):
    sum = num1 + num2
    context = {
        'sum': sum
    }
    return render(request, 'home/sum.html', context)


def create_task(request, description):

    new_task = Task.objects.create(description=description, done=False)

    context = {
        'new_task': new_task,
    }
    return render(request, 'home/create_task.html', context)