# Generated by Django 4.2.4 on 2023-08-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Заголовок запису"),
                ),
                ("description", models.TextField(verbose_name="Текст запису")),
                (
                    "author",
                    models.CharField(max_length=100, verbose_name="Ім'я автора"),
                ),
                ("date", models.DateField(verbose_name="Дата публікації")),
            ],
            options={
                "verbose_name": "Запис",
                "verbose_name_plural": "Запиcи",
            },
        ),
    ]