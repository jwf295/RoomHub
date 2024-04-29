# Generated by Django 5.0.2 on 2024-04-29 21:01

import api.models
import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.CharField(
                        default="None",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=100, null=True)),
                ("last_name", models.CharField(blank=True, max_length=100, null=True)),
                ("bio", models.TextField(blank=True, max_length=500, null=True)),
                ("age", models.IntegerField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("school", models.CharField(blank=True, max_length=255, null=True)),
                ("pets", models.BooleanField(default=False)),
                ("allergies", models.TextField(blank=True, max_length=500, null=True)),
                ("budget", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "sleep_schedule",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        default="profiles/default.png",
                        upload_to=api.models.uploadProfilePicture,
                    ),
                ),
            ],
            options={
                "ordering": ["last_name"],
            },
        ),
        migrations.CreateModel(
            name="Listing",
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
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, unique=True
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.IntegerField(default=0)),
                ("location", models.CharField(default="", max_length=255)),
                ("available_from", models.DateField(default=datetime.date.today)),
                ("duration", models.CharField(blank=True, max_length=100, null=True)),
                ("preferences", models.TextField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                ("sqft", models.IntegerField(default=0)),
                ("bedrooms", models.IntegerField(default=0)),
                ("bathrooms", models.IntegerField(default=0)),
                ("amenities", models.JSONField(blank=True, null=True)),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="listings",
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Fav",
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
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fav",
                        to=settings.AUTH_USER_MODEL,
                        to_field="username",
                    ),
                ),
                (
                    "created_at",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.listing",
                        to_field="created_at",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("username", models.CharField(blank=True, max_length=100, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                (
                    "created_at",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.listing",
                        to_field="created_at",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ListingPhoto",
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
                    "image",
                    models.ImageField(
                        default="listings/default.jpg",
                        upload_to=api.models.uploadListingImage,
                    ),
                ),
                (
                    "created_at",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.listing",
                        to_field="created_at",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="received_messages",
                        to="api.userprofile",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sent_messages",
                        to="api.userprofile",
                    ),
                ),
            ],
        ),
    ]
