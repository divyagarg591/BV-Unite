# Generated by Django 3.1.7 on 2021-04-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_anouncement_anc_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anouncement',
            name='anc_img',
        ),
    ]
