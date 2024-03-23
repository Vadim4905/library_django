from django.db import models

# Create your models here.

class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn =models.CharField(max_length=100,primary_key=True)
    available =models.BooleanField()
    
    class Meta:
        ordering = ['author']
        index_together = [['isbn']]