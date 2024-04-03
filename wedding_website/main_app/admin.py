from django.contrib import admin
from .models import TodoItem, RsvpEntry

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(RsvpEntry)