# Generated by Django 2.1.3 on 2018-11-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='code',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
