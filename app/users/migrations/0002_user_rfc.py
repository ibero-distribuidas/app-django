# Generated by Django 4.0.4 on 2022-05-05 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rfc',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
