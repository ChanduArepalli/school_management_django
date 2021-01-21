from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=15)
    admin_no = models.IntegerField()
    section_name = models.CharField(max_length=15)
    attendance = models.BooleanField()
    class_teacher = models.CharField(max_length=15)
    class_name = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=15)

    def __str__(self):
        return self.name