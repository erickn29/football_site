# Generated by Django 3.2.9 on 2022-02-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20220207_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.TextField(default='*'),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(default='338264', max_length=80),
        ),
    ]