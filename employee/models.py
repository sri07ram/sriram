from django.db import models
"""Name
Email
Phone
Department (linked via ForeignKey)
Job title
Date of joining"""
class Employee(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField()
    phone=models.CharField(max_length=12)
    dept=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    doj=models.CharField(max_length=10)
    company=models.CharField(max_length=100,null=True)

