from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    context = {'index_text': "Welcome Index Page.", }
    return render(request, 'index.html')


@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()

            messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)

        return render(request, 'todolist.html', {'all_tasks': all_tasks})


@login_required(login_url='login')
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, ("You are Not Authorized!"))

    return redirect('todolist')


@login_required(login_url='login')
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        if task.owner == request.user:
            form = TaskForm(request.POST or None, instance=task)
            if form.is_valid():
                form.save()
                messages.success(request, ('Task is edited successfully!'))
            return redirect('todolist')
        else:
            messages.error(request, ("You are Not Authorized!"))
            return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        if task_obj.owner == request.user:
            return render(request, 'edit.html', {'task_obj': task_obj})
        else:
            messages.error(request, ("You are Not Authorized!"))
            return redirect('todolist')

@login_required(login_url='login')
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = True
        task.save()
    else:
        messages.error(request, ("You are Not Authorized!"))

    return redirect('todolist')


@login_required(login_url='login')
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.done = False
        task.save()
    else:
        messages.error(request, ("You are Not Authorized!"))
    return redirect('todolist')