# Generated by Django 3.1b1 on 2020-07-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0016_replicate_interfaces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachine',
            name='local_context_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
