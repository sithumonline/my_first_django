from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed')
    search_fields = ('title',)
    list_filter = ('completed',)
    ordering = ('-id',)
admin.site.register(Todo, TodoAdmin)

