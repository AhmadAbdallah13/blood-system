# Generated by Django 5.1.6 on 2025-02-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_citizen_password_alter_institute_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$rgZmjtQRsUGcoFiEKcRNEN$6vBh5kzAyK5ACfTn81ofkzRjGgBHF6ceCIlNlt2VfwU=', max_length=255),
        ),
        migrations.AlterField(
            model_name='institute',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$870000$a5mryzUqANpxF65k9HKcPu$3rC2kMZ0EeKX1FGaD+IvLD4deT6ABIhwyC/Sz7Tzlck=', max_length=255),
        ),
    ]
