# Generated by Django 5.1.1 on 2024-12-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_rename_course_opted_trainer_courses_opted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='enrollment_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
