# Generated by Django 4.2.6 on 2023-10-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salagubmaslo', '0004_equipmentsupplementimage_equipmentsupplement'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipmentsupplement',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
