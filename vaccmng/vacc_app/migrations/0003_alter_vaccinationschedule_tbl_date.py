# Generated by Django 4.0 on 2022-01-14 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacc_app', '0002_hospital_tbl_vaccinationschedule_tbl_vaccine_tbl_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinationschedule_tbl',
            name='date',
            field=models.DateField(),
        ),
    ]