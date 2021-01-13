from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from todo.models import Task
# Create your views here.

def todohome(request):
	all_items=Task.objects.all()
	return render(request,"todo_templates/index.html",{'items':all_items})

def addtask(request):
	task=request.POST['task']
	Task(task=task).save()
	return HttpResponseRedirect('/todo/')

def deletetask(request,item_id):
	item=Task.objects.get(id=item_id)
	item.delete()
	return HttpResponseRedirect("/todo/")

