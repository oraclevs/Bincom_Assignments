from django.db import models
from bcrypt import checkpw,gensalt,hashpw
from dotenv import load_dotenv
import os
from django.contrib.auth.models import User
load_dotenv()



class TodoList(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False)
    user = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)

class Todo(models.Model):
    todo = models.CharField(max_length=50, null=False)
    priority = models.CharField(max_length=10, choices=[('High', 'High'), ('Low', 'Low'), ('Normal', 'Normal')])
    tag = models.CharField(max_length=40, null=False)
    completed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)
    todo_list = models.ForeignKey(TodoList, related_name='todos', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='todos', on_delete=models.CASCADE)
    time_created = models.TimeField(auto_now_add=True)
    time_updated = models.TimeField(auto_now=True)
