from django import  forms
from django.forms import fields
from .models import Student_Register


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student_Register
        fields = "__all__"
        labels = {"full_name": "Full Name","mobile":"Mobile","email":"Email","gender":"Gender","student_number":"Student Number","path":"Path"}