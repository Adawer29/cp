# Generated by Django 2.1.2 on 2018-10-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0010_auto_20181019_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_image',
            field=models.ImageField(upload_to='question_image/'),
        ),
    ]
