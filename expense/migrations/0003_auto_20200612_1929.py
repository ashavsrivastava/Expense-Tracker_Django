# Generated by Django 3.0.5 on 2020-06-12 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20200612_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
