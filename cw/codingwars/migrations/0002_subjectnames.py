# Generated by Django 3.2.7 on 2021-09-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codingwars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectNames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=300)),
                ('subject_description', models.TextField()),
            ],
        ),
    ]