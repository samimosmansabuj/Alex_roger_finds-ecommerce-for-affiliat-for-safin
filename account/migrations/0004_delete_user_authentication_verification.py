# Generated by Django 5.0.4 on 2024-05-29 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_customer_profile_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Authentication_Verification',
        ),
    ]
