# Generated by Django 4.1.5 on 2023-04-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_employeestatus_leaves'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Incomplete', 'Incomplete'), ('Complete', 'Complete')], default='Incomplete', max_length=10),
        ),
    ]
