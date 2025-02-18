# Generated by Django 5.1.6 on 2025-02-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('national_id', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('blood_type', models.CharField(max_length=5)),
                ('city', models.CharField(choices=[('Shmesani', 'Shmesani'), ('Khalda', 'Khalda'), ('Makka Street', 'Makka Street')], max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('institute_type', models.CharField(choices=[('Hospital', 'Hospital'), ('Blood Bank', 'Blood Bank'), ('Clinic', 'Clinic')], max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('city', models.CharField(choices=[('Shmesani', 'Shmesani'), ('Khalda', 'Khalda'), ('Makka Street', 'Makka Street')], max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
