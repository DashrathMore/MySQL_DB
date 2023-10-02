from django.db import models

# Create your models here.

class Liabrary(models.Model):
    Section=models.CharField(max_length=100, primary_key=True)

class Book(models.Model):
    Section=models.ForeignKey(Liabrary, on_delete=models.CASCADE)
    Book_name=models.CharField(max_length=100, primary_key=True)
    Auther=models.CharField(max_length=100)