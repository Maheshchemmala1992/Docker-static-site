# Generated by Django 2.2.6 on 2022-01-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='day_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='hours_worked',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='minutes_worked',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]