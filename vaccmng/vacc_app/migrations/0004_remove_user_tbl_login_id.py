# Generated by Django 4.0 on 2022-02-02 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacc_app', '0003_remove_nurse_tbl_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_tbl',
            name='login_id',
        ),
    ]
