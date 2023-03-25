# Generated by Django 4.1.7 on 2023-03-25 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0004_sociallink_customuser_social_links"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="social_links",
        ),
        migrations.AddField(
            model_name="sociallink",
            name="user",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="social_links",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]