# Generated by Django 3.2.3 on 2021-05-18 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sequence_flattener', '0003_sequence_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sequence',
            name='result',
        ),
    ]