# Generated by Django 3.1.7 on 2021-03-03 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cave', '0004_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default='str', max_length=300),
        ),
    ]
