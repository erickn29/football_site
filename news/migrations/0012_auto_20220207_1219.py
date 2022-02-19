# Generated by Django 3.2.9 on 2022-02-07 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20220207_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='*', max_length=160)),
                ('coach', models.CharField(default='*', max_length=160)),
                ('players', models.TextField(default='*')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.CharField(default='477622', max_length=80),
        ),
    ]