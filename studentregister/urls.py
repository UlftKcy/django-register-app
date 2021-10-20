from django.urls import path
from .views import home,student_list,student_form,student_update,student_delete

urlpatterns = [
    path('', home, name="home"),
    path('student_list/',student_list , name="student_list"),
    path('student_form/',student_form , name="student_form"),
    path('update/<int:id>/',student_update , name="student_update"),
    path('delete/<int:id>/',student_delete , name="student_delete"),
]