from django.db import models

# Create your models here.

class Student_Register(models.Model):
    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    email = models.EmailField(max_length=154)
    
    GENDER =(
        ("Female" , "Female"),
        ("Male" , "Male"),
        ("Other" , "Other"),
        ("Prefer Not to" , "Prefer Not to"),
    )
    
    gender = models.CharField(max_length=50, choices=GENDER)
    student_number = models.CharField(max_length=50,blank=True,null=True)
    
    PATH =(
        ("Full Stack Developer", "Full Stack Developer"),
        ("AWS/Devops", "AWS/Devops"),
        ("Data Science", "Data Science"),
        ("Cyber Security", "Cyber Security"),   
    )
    path = models.CharField(max_length=50, choices=PATH)
    
    def __str__ (self):
        return (f"{self.student_number} - {self.full_name}")
