# Generated by Django 2.2.10 on 2020-04-27 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0020_auto_20200409_1653"),
        ("leads", "0011_auto_20200401_0937"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.Company",
            ),
        ),
    ]
