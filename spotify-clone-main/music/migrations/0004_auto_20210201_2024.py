# Generated by Django 3.1.5 on 2021-02-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20210201_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='casting',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='Album_Title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=10),
        ),
    ]