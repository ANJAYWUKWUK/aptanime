# aptanimelistweb/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models  # Add this import statement    

class List(models.Model):
     judul = models.CharField(max_length=300)
     gambar = models.ImageField(upload_to='imgs/',null=True)
     detail = models.TextField()
     add_time = models.DateTimeField(auto_now_add=True)
    

     class Meta:
         verbose_name_plural = 'list'


     def _str_(self):
        return self.judul