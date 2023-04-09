from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo, TodoItems
from .forms import TodoForm

# Create your views here.


def home(req):
    
    # Todo.objects.get() === where() ---> wait condition
    
    todos = Todo.objects.all()
    message = "my name is montaser mohamed hassan"
    
    context = {
        "message": message,
        "todos": todos
    }
    
    return render(req, 'home.html', context)


def detailed(req, id):
    
    todo = Todo.objects.get(id = id)
    todoitems = todo.todoitems_set.all()
    
    context = {
        "todo": todo,
        "todoitems": todoitems
    }
    
    return render(req, 'detailed.html', context)


def createTodo(req):
    form = TodoForm()
    if req.method == "POST":        
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    
    return render(req, "createTodo.html", context)



def updateTodo(req, pk):
    todo = Todo.objects.get(id = pk)
    form = TodoForm(instance = todo)
    if req.method == "POST":
        form = TodoForm(req.POST, instance = todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(req, "updateTodo.html", context)



def deleteTodo(req, pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('/')
    