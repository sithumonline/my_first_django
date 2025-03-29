from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
