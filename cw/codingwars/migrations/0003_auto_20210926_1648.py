# Generated by Django 3.2.7 on 2021-09-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codingwars', '0002_subjectnames'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uroki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urok_name', models.CharField(db_index=True, max_length=300)),
                ('urok_description', models.CharField(max_length=1000)),
                ('urok_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='subjectnames',
            name='urok',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='codingwars.uroki'),
        ),
    ]
