from django.db import models

# Create your models here.

class Student(models.Model):
	roll_no=models.IntegerField()
	name=models.CharField(max_length=25)
	email=models.CharField(max_length=30)
	cont=models.IntegerField()

	def __str__(self):
		return self.email

