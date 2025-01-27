from django.db import models
from django.forms import ValidationError
import magic
import uuid


# validate the incoming audio file
def validate_audio_file(file):
    mime = magic.Magic(mime=True)
    file_mime_type = mime.from_buffer(file.read())
    if not file_mime_type.startswith('audio/'):
        raise ValidationError(
            'Invalid file type. Only audio files are allowed.')


uid = uuid.uuid4()
class Music(models.Model):
    slug = models.SlugField(default=uid, editable=False)
    music_icons = models.ImageField(blank=False)
    music_title = models.CharField(max_length=100, null=False)
    audio_file = models.FileField(null=False, validators=[validate_audio_file])
    artist_name = models.CharField(max_length=100, null=False)
    albumName_or_playlistName = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class PlayList_or_Album(models.Model):
    slug = models.SlugField(default=uid, editable=False)
    PlayList_or_AlbumName = models.CharField(max_length=100, null=False)
    play_list_cover_image = models.ImageField(blank=False)
    songs = models.ManyToManyField(
        Music, related_name='playlists_or_albums')
    artist_name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        matching_songs = Music.objects.filter(
            albumName_or_playlistName=self.PlayList_or_AlbumName)
        self.songs.set(matching_songs)

