# Generated by Django 3.2 on 2022-08-29 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=50)),
                ('courseName', models.CharField(max_length=200)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
