# Generated by Django 3.2.8 on 2022-02-17 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problem', '0002_problem_datatype'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='difficulty',
            field=models.CharField(default='Easy', max_length=30),
        ),
    ]
