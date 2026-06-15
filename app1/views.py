from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, TaskHistory
from app2.models import register1

# Create your views here.

def home(request):
    user = request.session.get('i_id')
    b = register1.objects.get(id=user)
    a = Task.objects.all()
    return render(request, 'home.html', {'k':a, 'k1':b})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        person = request.POST.get('person')
        email = request.POST.get('email')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        Task.objects.create(title=title, description=description, person=person, email=email, deadline=deadline, status=status)
        return redirect('home')
    return render(request, 'add.html')

def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.person = request.POST.get('person')
        task.email = request.POST.get('email')
        task.deadline = request.POST.get('deadline')
        task.status = request.POST.get('status')
        task.save()
        return redirect('home')

    return render(request, 'update.html', {'task': task})


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    TaskHistory.objects.create(title=task.title, description=task.description, person=task.person, email=task.email, deadline=task.deadline, status=task.status)
    task.delete()
    return redirect('home')


def delete_all_tasks(request):
    Task.objects.all().delete()
    return redirect('home')


#new
def history(request):
    # data = YourModel.objects.filter(is_deleted=True)  # example
    # return render(request, 'history.html', {'data': data})
    k = TaskHistory.objects.all()
    return render(request, 'history.html', {'k':k})

def restore(request, id):
    a = get_object_or_404(TaskHistory, id=id)
    Task.objects.create(title=a.title, description=a.description, person=a.person, email=a.email, deadline=a.deadline, status=a.status)
    a.delete()
    return redirect('history')

def delete_restore(request, id):
    var = TaskHistory.objects.get(id=id)
    var.delete()
    return redirect('history')

def restore_all(request):
    var = TaskHistory.objects.all()
    data = []
    for i in var:
        data.append(
            Task(
                title=i.title,
                description=i.description,
                person=i.person,
                email=i.email,
                deadline=i.deadline,
                status=i.status
            )
        )

    Task.objects.bulk_create(data)
    var.delete()

    return redirect('history')
    # Task.objects.bulk_create(var)
    # var.delete()
    # return redirect('history')

def delete_history(request):
    var = TaskHistory.objects.all()
    var.delete()
    return redirect('history')