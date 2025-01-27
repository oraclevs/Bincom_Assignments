from django.shortcuts import render
from . import models
# Create your views here.


def index(request):
    return render(request, 'Music_player/landingpage.html')

def dashboard(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = models.PlayList_or_Album.objects.filter(
            PlayList_or_AlbumName__icontains=query)
    if results:
        print(results.all(),"results")
    playlists = models.PlayList_or_Album.objects.all()
    print(playlists,"playlists")
    return render(request, 'Music_player/dashboard.html',{'playlists':playlists,'results':results})


def play_music(request, slug):
    playlist = models.PlayList_or_Album.objects.filter(slug=slug).first()
    if not playlist:
        return render(request, 'Music_player/404.html')
    return render(request, 'Music_player/dashboard_playmusic.html', {'playlist': playlist})

