# Generated by Django 3.2.14 on 2022-08-19 08:39

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Influencer', '0005_alter_influencer_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='follow',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), default=None, max_length=66, null=True, size=6),
        ),
    ]
