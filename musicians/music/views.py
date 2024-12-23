from django.shortcuts import render, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

# List View
def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musician_list.html', {'musicians': musicians})

#Edit Musician
def musician_edit(request, musician_id):
    musician = Musician.objects.get(pk=musician_id)
    form = MusicianForm(instance=musician)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    return render(request, 'musician_form.html', {'form': form})

# Edit Album
def album_edit(request, album_id):
    album = Album.objects.get(pk=album_id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_list')
    return render(request, 'album.html', {'form': form})

# Delete
def delete_item(request, item_id):
    musician = Musician.objects.get(pk=item_id)
    musician.delete()
    return redirect('musician_list')
