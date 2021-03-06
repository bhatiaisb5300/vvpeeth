# Generated by Django 2.1.7 on 2020-03-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alumni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=15)),
                ('Batch', models.CharField(max_length=5)),
                ('Photo', models.FileField(upload_to='alumni/')),
                ('address', models.CharField(max_length=100)),
                ('date_time', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(upload_to='gallery/')),
                ('Title', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='notice_events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Photo', models.ImageField(upload_to='n_e/img')),
                ('File', models.FileField(blank=True, null=True, upload_to='n_e/docs')),
                ('Title', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='our_gems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Marks', models.CharField(max_length=20)),
                ('Photo', models.FileField(upload_to='our_gems/')),
                ('Batch', models.CharField(max_length=5)),
                ('Class', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=50)),
                ('Designation', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
            ],
        ),
    ]
