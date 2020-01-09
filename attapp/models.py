from django.db import models

# Create your models here.
class admin(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)



class sign(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile=models.IntegerField(max_length=10, null=True, blank=True)

class faculty(models.Model):
    Fid=models.IntegerField(primary_key="True")
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)
    DOB=models.DateField()
    Gender=models.CharField(max_length=10)
    Qualification=models.CharField(max_length=10)
    Mobile=models.IntegerField(max_length=10, null=True, blank=True)
    BatchInCharge=models.CharField(max_length=10)
    Email=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)

class student(models.Model):
    Sid=models.IntegerField(primary_key="True")
    AdmNo=models.IntegerField(null=True, blank=True)
    AdmDate=models.DateField(null=True, blank=True)
    Name=models.CharField(max_length=20,null=True, blank=True)
    Address=models.CharField(max_length=40,null=True, blank=True)
    DOB=models.DateField(null=True, blank=True)
    Gender=models.CharField(max_length=10,null=True, blank=True)
    Mobile=models.IntegerField(max_length=10, null=True, blank=True)
    Guardian=models.CharField(max_length=20,null=True, blank=True)
    Batch=models.CharField(max_length=20,null=True, blank=True)
    Email=models.CharField(max_length=20,null=True, blank=True)
    Password=models.CharField(max_length=20,null=True, blank=True)

class fac_attendance(models.Model):
    Date=models.DateField()
    Fid=models.IntegerField()
    status_h1=models.CharField(max_length=20)
    status_h2=models.CharField(max_length=20)
    status_h3=models.CharField(max_length=20)
    status_h4=models.CharField(max_length=20)

class stud_attendance(models.Model):
    Date=models.DateField()
    Sid=models.IntegerField()
    status_h1=models.CharField(max_length=20)
    status_h2=models.CharField(max_length=20)
    status_h3=models.CharField(max_length=20)
    status_h4=models.CharField(max_length=20)
    batch=models.CharField(max_length=10,null=True,blank=True)

class mark(models.Model):
    Sid=models.IntegerField()
    AssessmentNo=models.IntegerField(null=True, blank=True)
    Sub1=models.IntegerField(null=True, blank=True)
    Sub2=models.IntegerField(null=True, blank=True)
    Sub3=models.IntegerField(null=True, blank=True)
    Percentage=models.FloatField(null=True, blank=True)


class leavestu(models.Model):
    Sid=models.IntegerField()
    Fromdate=models.DateField()
    Todate=models.DateField()
    Reason=models.CharField(max_length=40)
    Status=models.CharField(max_length=10)

class leavefac(models.Model):
    Fid=models.IntegerField()
    Fromdate=models.DateField()
    Todate=models.DateField()
    Reason=models.CharField(max_length=40)
    Status=models.CharField(max_length=10)

class timetable(models.Model):
    Day=models.CharField(max_length=10)
    Batch=models.CharField(max_length=10)
    Hour1=models.CharField(max_length=10)
    Hour2=models.CharField(max_length=10)
    Hour3=models.CharField(max_length=10)
    Hour4=models.CharField(max_length=10)

class Meta:
    db_table='admin'
    db_table='sign'
    db_table='faculty'
    db_table='student'
    db_table='fac_attendance'
    db_table='leavestu'
    db_table='leavefac'
    db_table='timetable'
