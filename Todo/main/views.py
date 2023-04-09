from django.shortcuts import render, redirect

from .models import Todo, TodoItems
from .forms import TodoForm, UserCreationForm
from .filters import TodoFilter

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="login")
def home(req):    
    # Todo.objects.get() === where() ---> wait condition
    user = req.user
    filter = TodoFilter()
    todos = Todo.objects.filter(user = user)
    if req.method == "Get":
        result = TodoFilter(req.GET, queryset = todos)
        todos = result.qs
    context = {
        "todos": todos,
        "user": user,
        "filter": filter,
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

    
    
def createUser(req):
    form = UserCreationForm()
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save() 
        else:
            print (form.errors)
        return redirect('/')
    context = {
        "form": form
    }
    return render(req, "signUp.html", context)



def loginUser(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password) # ---> to find this user from database or not
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            return redirect('/')
    context = {
    }
    return render(req, "login.html", context)



def logoutUser(req):
    logout(req)
    return redirect('/')
