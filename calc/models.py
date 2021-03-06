from django.db import models

# Create your models here.
class batch(models.Model):
	year=models.CharField(max_length=10, null=True)
	def __str__(self):
		return self.year

class branch(models.Model):
	branch=models.CharField(max_length=50, null=True)
	def __str__(self):
		return self.branch

class subjects(models.Model):
	name = models.CharField(max_length=100, null=True)
	credit = models.IntegerField(default=4)
	year = models.ForeignKey(batch, on_delete=models.CASCADE,null=True)
	branch = models.ForeignKey(branch, on_delete=models.CASCADE,null=True)
	def __str__(self):
		return self.name