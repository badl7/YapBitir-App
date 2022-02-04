from django.db import models

from datetime import datetime
# Create your models here.

class Yapbitir(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="User")
    title = models.CharField(max_length=100, verbose_name="Liste Adı")
    content = models.TextField(verbose_name="YapBtirler")
    finished = models.BooleanField(default=True,verbose_name="Tamamlandı")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulan Tarihi")
    dateline = models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Yapbitir,on_delete= models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length= 50 ,verbose_name="İsim")
    comment_content = models.CharField(max_length= 200, verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']