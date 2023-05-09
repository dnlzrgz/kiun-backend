# Generated by Django 4.2 on 2023-04-11 13:52

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_tags_alter_project_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(location=""),
                upload_to="projects",
            ),
        ),
    ]