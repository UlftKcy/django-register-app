# Generated by Django 3.2.8 on 2021-10-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentregister', '0002_alter_student_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_register',
            name='path',
            field=models.CharField(choices=[('Full Stack Developer', 'Full Stack Developer'), ('AWS/Devops', 'AWS/Devops'), ('Data Science', 'Data Science'), ('Cyber Security', 'Cyber Security')], max_length=50),
        ),
    ]
