# Generated by Django 4.2 on 2024-07-23 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0005_alter_ticketanswer_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
