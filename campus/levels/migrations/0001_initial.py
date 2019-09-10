# Generated by Django 2.2.2 on 2019-09-10 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('answer', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_image', models.ImageField(upload_to='levels/')),
                ('text', models.TextField(blank=True, max_length=100)),
                ('question_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques', to='levels.Answer')),
            ],
        ),
    ]
