from django.urls import include, path, re_path
from .import views



app_name = 'Todo'


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('todo/',views.todopage,name='todo_page'),
    path('logout/',views.logoutUser,name='logout'),
    path('todo/save/',views.saveTodo,name='save_todo'),
    path('get_it/',views.get_csrf_token,name='get_it'),
    path('get_todos/',views.get_todos,name='get_todos'),
    path('delete_todo/',views.delete_todo,name='delete_todo'),
    path('mark_completed/',views.mark_completed,name='mark_completed')
]
