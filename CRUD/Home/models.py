from django.db import models

class Entry(models.Model):
	ID=models.CharField(max_length=10,primary_key=True)
	data1=models.CharField(max_length=50)
	data2=models.CharField(max_length=20)
# Create your models here.
