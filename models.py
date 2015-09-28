
from django.db import models
from django.contrib import admin


# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=150)
    body=models.TextField()
    time=models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display = {'title','body','time'}
    admin.site.register(BlogPost)


class Profesor(models.Model):
    nombre=models.CharField(max_length=150)
    apeUno=models.CharField(max_length=150)
    apeDos=models.CharField(max_length=150)
    
