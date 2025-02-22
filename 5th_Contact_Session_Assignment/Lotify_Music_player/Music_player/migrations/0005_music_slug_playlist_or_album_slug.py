# Generated by Django 5.1.5 on 2025-01-26 20:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music_player', '0004_playlist_or_album_play_list_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='slug',
            field=models.SlugField(default=uuid.UUID('4a4119c0-d3e3-4790-abcc-afb92d236d1e'), editable=False),
        ),
        migrations.AddField(
            model_name='playlist_or_album',
            name='slug',
            field=models.SlugField(default=uuid.UUID('4a4119c0-d3e3-4790-abcc-afb92d236d1e'), editable=False),
        ),
    ]
