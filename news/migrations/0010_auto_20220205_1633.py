# Generated by Django 3.2.9 on 2022-02-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20220205_1625'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Milan_news',
        ),
        migrations.AlterField(
            model_name='news',
            name='logo_url',
            field=models.TextField(default='*'),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(default='963912', max_length=80),
        ),
    ]