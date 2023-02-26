from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def taskList(request) :
 form = TaskForm()
 tasklist = Task.objects.all()

 if request.method == 'POST' :
  form = TaskForm(request.POST)
  if form.is_valid():
   form.save()
   print('I am here')
   return redirect('task-list')

 context = {'tasks': tasklist, 'form':form}
 return render(request, 'task/task.html', context)

def editTask(request, pk):
 task = Task.objects.get(id = pk)
 form = TaskForm(instance = task)

 if request.method == 'POST':
  form = TaskForm(request.POST, instance=task)
  if form.is_valid():
   form.save()
   return redirect('task-list')

 context = {'form' : form}
 return render(request, 'task/editTask.html', context)

def deleteTask(request, pk) :
 task = Task.objects.get(id = pk)
 
 if request.method == 'POST':
  task.delete()
  return redirect('task-list')

 context = {'task' : task}
 return render(request, 'task/deleteconfirm.html', context)