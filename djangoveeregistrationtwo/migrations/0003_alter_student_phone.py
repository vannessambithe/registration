# Generated by Django 4.1.7 on 2023-03-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoveeregistrationtwo', '0002_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
