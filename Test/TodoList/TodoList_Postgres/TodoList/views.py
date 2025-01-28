from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Todo,TodoList
from django.http import JsonResponse

def home(request):
    return redirect(to='login/')

# auth views
def registerUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'TodoList/auth.html')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            login(request, user)
            return redirect('Todo:todo_page')

    return render(request, 'TodoList/auth.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('Todo:todo_page')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'TodoList/login.html')

    return render(request, 'TodoList/login.html')


@login_required
def todopage(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'TodoList/todo.html',{'username':request.user,'todo_lists':todo_lists})


def logoutUser(request):
    if request.method == "POST":
        logout(request)
        return redirect(to='/')



#  todo views
from django.middleware.csrf import get_token

@login_required
def saveTodo(request):
    if request.method == "POST":
        todo = request.POST['todo']
        priority = request.POST['priority']
        tag = request.POST['tag']
        todo_list_id = createTodoList(request)
        user_todo = Todo()
        user_todo.user = request.user
        user_todo.todo = todo
        user_todo.priority = priority
        user_todo.tag = tag
        user_todo.todo_list = todo_list_id
        user_todo.save()
        return redirect('Todo:todo_page')


def createTodoList(request):
    todo_list = TodoList.objects.get(name="Today")
    if not todo_list:
        todo_list.name = "Today"
        todo_list.user = request.user
        todo_list.save()
    return todo_list

@login_required
def delete_todo(request):
    if request.method == "POST":
        todo_id = request.POST['todo_id']
        Todo.objects.filter(id=todo_id).delete()
        return JsonResponse({"success":True})

@login_required
def mark_completed(request):
    if request.method == "POST":
        completed = request.POST['completed'].lower() == 'true'
        todo_id = request.POST['todo_id']
        print(completed)
        Todo.objects.filter(id=todo_id).update(completed=completed)
        return JsonResponse({"success": True})

@login_required
def get_todos(request):
    todos = Todo.objects.filter(user=request.user).order_by("-time_created")
    todos_list = list(todos.values())
    return JsonResponse(todos_list, safe=False)


@login_required
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({"td": csrf_token})

