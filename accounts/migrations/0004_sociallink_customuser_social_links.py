# Generated by Django 4.1.7 on 2023-03-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_customuser_contact_email_customuser_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="SocialLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                ("url", models.URLField(verbose_name="url")),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="social_links",
            field=models.ManyToManyField(blank=True, to="accounts.sociallink"),
        ),
    ]