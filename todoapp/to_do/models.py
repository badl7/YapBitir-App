from django.db import models

# Create your models here.

class ToDo(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    title = models.CharField(max_length= 200)
    created_date = models.DateTimeField(auto_now_add=True)

