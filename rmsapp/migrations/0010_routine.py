# Generated by Django 3.2 on 2022-08-30 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rmsapp', '0009_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekdays', models.CharField(choices=[('Sun', 'Sun'), ('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat')], max_length=50, null=True)),
                ('startTime', models.CharField(max_length=50, null=True)),
                ('endTime', models.CharField(max_length=50, null=True)),
                ('level', models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6')], max_length=50, null=True)),
                ('semester', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI')], max_length=50, null=True)),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmsapp.teacher')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmsapp.unit')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rmsapp.academicyear')),
            ],
        ),
    ]