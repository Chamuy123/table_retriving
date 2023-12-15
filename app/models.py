from django.db import models

# Create your models here.
class Course(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname

class Student(models.Model):
    sid=models.IntegerField()
    sname=models.CharField(max_length=100)
    sph=models.IntegerField()
    email=models.EmailField(default="stundent@gmail.com")
    cid=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.sname