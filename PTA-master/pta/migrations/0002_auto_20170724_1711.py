# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 21:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='dateOf',
            new_name='dateAndTimeOf',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='grade',
        ),
        migrations.AlterField(
            model_name='activity',
            name='date_of',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='homework',
            name='date_assigned',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='date_assigned',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homeworkgrade',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pta.Homework'),
        ),
        migrations.AddField(
            model_name='homeworkgrade',
            name='parentalunit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pta.ParentalUnit'),
        ),
    ]