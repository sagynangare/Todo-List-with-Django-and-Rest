from django.contrib import admin
from .models import TodoTask, User,Profile

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(TodoTask)
