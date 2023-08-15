# Generated by Django 4.2.4 on 2023-08-15 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0004_alter_comments_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор коментаря",
            ),
        ),
    ]
