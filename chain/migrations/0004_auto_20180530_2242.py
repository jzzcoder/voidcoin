# Generated by Django 2.0.5 on 2018-05-30 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0003_auto_20180530_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blockaccount',
            old_name='identify',
            new_name='alias',
        ),
    ]
