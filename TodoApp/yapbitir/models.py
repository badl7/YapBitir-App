from django.db import models

from datetime import datetime
# Create your models here.

class Yapbitir(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="User")
    title = models.CharField(max_length=100)
    content = models.TextField()
    finished = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    dateline = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title

