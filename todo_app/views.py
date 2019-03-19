from django.shortcuts import render,redirect
from dateutil import parser
from .models import Todo


def todo_redirect(request):
    return redirect('/todo/')


def todo_list(request):
    context = {}
    context['all_status'] = ['In Progress','Pending','Completed']
    return render(request, 'todo/index.html', context)


def create(request):
	task_date = parser.parse(request.POST['task_date'])
	title=request.POST['title']
	description=request.POST['description']
	status=request.POST['status']
	todo = Todo(title=title,description=description,status=status,task_date=task_date)
	todo.save()
	return redirect('/todo/')

def read(request):
	todo_list = Todo.objects.filter(is_delete=False).order_by('-modified_at')
	context = {'todo_list': todo_list}
	return render(request, 'todo/result.html', context)

def edit(request, id):
	context = {}
	context['all_status'] = ['In Progress','Pending','Completed']
	todo = Todo.objects.get(id=id)
	context['todo'] = todo
	task_date = todo.task_date
	parsed_date = task_date.strftime('%Y-%m-%dT%H:%M')
	context['parsed_date']=parsed_date
	return render(request, 'todo/edit.html', context)


def update(request, id):
	todo = Todo.objects.get(id=id)
	todo.title = request.POST['title']
	todo.description = request.POST['description']
	todo.status = request.POST['status']
	todo.task_date = request.POST['task_date']
	todo.save()
	return redirect('/todo/')


def delete(request, id):
	todo = Todo.objects.get(id=id)
	todo.is_delete = True
	todo.save()
	return redirect('/todo/')