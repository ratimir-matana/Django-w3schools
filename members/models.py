from django.db import models

# Create your models here.

# Creating a class in models means creating a new table in database. Table name will be the name of the class.
# Class members or variables define table fields. Table is created through Django ORM (Object Relation Mapping)

class Member(models.Model):
   firstname = models.CharField(max_length=255)
   lastname = models.CharField(max_length=255)
   phone = models.IntegerField(null=True)
   joined_date = models.DateField(null=True)


   # String representation function, variable1 and variable2 are string type (CharField), they are defined in class in models.py
   def __str__(self):
      return f"{self.firstname} {self.lastname}"

