# Generated by Django 2.2.4 on 2019-09-08 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('dashboard', '0005_userloggedin'),
        ('accounts', '0002_l_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='L_User',
        ),
    ]