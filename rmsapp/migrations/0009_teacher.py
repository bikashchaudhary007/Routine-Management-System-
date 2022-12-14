# Generated by Django 3.2 on 2022-08-30 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmsapp', '0008_rename_course_unit_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherID', models.CharField(max_length=50)),
                ('teacherName', models.CharField(max_length=200)),
                ('teacherLevel', models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6')], max_length=50, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmsapp.course')),
            ],
        ),
    ]
