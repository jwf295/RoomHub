# Generated by Django 5.0.2 on 2024-04-30 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
