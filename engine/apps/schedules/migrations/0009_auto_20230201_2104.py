# Generated by Django 3.2.16 on 2023-02-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0008_auto_20221201_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='customoncallshift',
            name='last_modified',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='customoncallshift',
            name='sequence',
            field=models.IntegerField(default=None, null=True),
        ),
    ]