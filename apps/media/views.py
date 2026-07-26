from django.shortcuts import render
from .models import Media

def media_list(request):
    immagini = Media.objects.all().order_by('-uploaded_at')
    return render(request, 'galleria.html', {'immagini': immagini})