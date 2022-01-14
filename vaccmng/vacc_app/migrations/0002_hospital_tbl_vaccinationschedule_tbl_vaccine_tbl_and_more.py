# Generated by Django 4.0 on 2022-01-03 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacc_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('e_mail', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationSchedule_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=20)),
                ('vaccine_type', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('approval_status', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('child_name', models.CharField(max_length=20)),
                ('child_age', models.IntegerField()),
                ('child_gender', models.CharField(max_length=20)),
                ('recent_vaccinations', models.CharField(max_length=20)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.login_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCard_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.user_tbl')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine', to='vacc_app.vaccine_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=20)),
                ('login_id', models.CharField(max_length=20)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.hospital_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('complaint', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('reply', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.user_tbl')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment_TBL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.CharField(max_length=20)),
                ('status', models.IntegerField()),
                ('vaccinated', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.vaccine_tbl')),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacc_app.user_tbl')),
            ],
        ),
    ]
