# Generated by Django 2.1.3 on 2018-11-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181124_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
