# Generated by Django 5.1.1 on 2024-12-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_alter_enrollment_enrollment_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
