# Generated by Django 4.2.1 on 2023-06-15 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
        ("community", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="board",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="community.board"
            ),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="user",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]