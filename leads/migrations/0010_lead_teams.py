# Generated by Django 2.2.4 on 2019-09-17 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teams", "0003_auto_20190909_1621"),
        ("leads", "0009_lead_created_from_site"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="teams",
            field=models.ManyToManyField(related_name="lead_teams", to="teams.Teams"),
        ),
    ]
