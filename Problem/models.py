from django.db import models

class Problem(models.Model):
    statement=models.TextField()
    input = models.TextField()
    output = models.TextField()
    title = models.TextField()
    difficulty = models.CharField(max_length=30,default="Easy")
    datatype = models.CharField(max_length=20,default='int')
    color = models.CharField(max_length=20,default="green")