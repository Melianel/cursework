# Generated by Django 4.2.4 on 2023-08-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="img",
            field=models.ImageField(
                default="img.jpg", upload_to="image/%Y", verbose_name="Іллюстрація"
            ),
            preserve_default=False,
        ),
    ]