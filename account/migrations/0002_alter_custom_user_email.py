# Generated by Django 5.0.4 on 2024-05-01 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
