# Generated by Django 3.2.14 on 2022-08-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_user_otptime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='otptime',
            field=models.CharField(default='125708', max_length=100),
        ),
    ]
