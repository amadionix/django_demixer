from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Song
from spleeter.separator import Separator
from django.conf import settings

import os
from django.http import FileResponse, Http404, HttpResponse
from django.utils.encoding import smart_str
from zipfile import ZipFile 
import shutil

import regex

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
uploads_path = os.path.join(BASE_DIR, 'uploads')
output_path = os.path.join(uploads_path, 'output')
tmp = os.path.join(uploads_path, 'demixed_track')

name = ""

def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            global name
            new_song = Song(song=request.FILES['select_audio_file'])
            new_song.save()
            unparsed_name = new_song.song.name
            name = new_song.song.name = ''.join(c for c in unparsed_name if ord(c) < 128)

            return render(request, 'select.html')
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form})

def select2(request):
    return render(request, 'process2.html')

def select4(request):
    return render(request, 'process4.html')

def process2(request):
    # separator = Separator('spleeter:2stems')
    # separator.separate_to_file(os.path.join(uploads_path, name), output_path)
    return render(request, 'success.html')

def process4(request):
    separator = Separator('spleeter:4stems')
    separator.separate_to_file(os.path.join(uploads_path, name), output_path)
    return render(request, 'success.html')

def download(request):
    global name
    stripped_name = os.path.splitext(name)[0]
    tmp = os.path.join(uploads_path, stripped_name)
    # shutil.make_archive(tmp, 'zip', os.path.join(output_path, stripped_name))
    # archived_file_path = tmp + '.zip'
    # zip_file = open(archived_file_path, 'rb')

    # obj = Song.objects.get(pk=1)
    # obj.song.delete()

    # return FileResponse(zip_file)
    return FileResponse(os.path.join(uploads_path, name))
