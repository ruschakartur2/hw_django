# Generated by Django 2.1 on 2020-08-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20200802_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.TextField(default=3),
            preserve_default=False,
        ),
    ]