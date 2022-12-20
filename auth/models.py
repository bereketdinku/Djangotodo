from django.db import models

# Create your models here.
class todolist(models.Model):
    username = models.CharField(max_length=100)
    password= models.CharField(min_length=8)

    def __str__(self):
        return self.username,self.password