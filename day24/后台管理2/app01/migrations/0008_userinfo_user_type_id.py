# Generated by Django 2.1.3 on 2018-11-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20181124_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_type_id',
            field=models.IntegerField(choices=[(1, '管理员'), (2, '超级用户'), (3, '普通用户'), (4, '游客')], default=1),
        ),
    ]
