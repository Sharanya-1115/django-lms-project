from django.db import models

# Create your models here.
class studentDetails(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    mobile_number=models.BigIntegerField()
    section=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)

class member(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    JobDoes=models.CharField(max_length=100)
    salary=models.DecimalField(max_digits=20,decimal_places=4)
