from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {'todos': Todo.objects.filter(isDeleted=False), 'form': TodoForm(), 'action': 'create', 'todo': None})

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()
    return render(request, 'index.html', {'form': form})

def update(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'index.html', {'form': form})

def delete(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.isDeleted = True
        todo.save()
        return redirect('index')
    return render(request, 'index.html', {'todo': todo})

def pre_update(request, id):
    todo = Todo.objects.get(id=id)
    return render(request, 'index.html', {'todos': Todo.objects.filter(isDeleted=False), 'form': TodoForm(instance=todo), 'action': 'update', 'todo': todo})
