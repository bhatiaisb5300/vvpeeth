# Generated by Django 2.1.7 on 2020-04-04 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vvp', '0003_alumni_current_employment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='Photo',
            field=models.FileField(blank=True, null=True, upload_to='alumni/'),
        ),
    ]
