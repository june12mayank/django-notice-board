from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoTtem
# Create your views here.

def todoView(request):
	all_todo_items=TodoTtem.objects.all()
	return render(request, 'todo.html',
		{'all_items':all_todo_items})

def addTodo(request):
	new_item= TodoTtem(content=request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/todo/')
	#create a new todo all_items
	#save
	#redirect browser to /todo/

def deleteTodo(request,todo_id):
	TodoTtem.objects.get(id=todo_id).delete()
	return HttpResponseRedirect('/todo/')