from django.shortcuts import render
import pandas as pd
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def storia(request):
    return render(request, 'history.html')

def regolamento(request):
    return render(request, 'rulebook_placeholder.html')

def rose(request):
    context = {'error': None, 'rose_per_anno': {}}
    try:
        # Costruisce il percorso del file in modo sicuro
        file_path = os.path.join(settings.BASE_DIR, 'fantalega', 'Rose_fantalega(1).xlsx')
        
        # Legge il file Excel
        df = pd.read_excel(file_path)

        # Raggruppa i dati per Anno e poi per Fantallenatore
        # Il risultato sarà un dizionario tipo: {2023: {'Allenatore1': ['GiocatoreA', 'GiocatoreB'], 'Allenatore2': [...]}}
        grouped = df.groupby(['Anno', 'Fantallenatore'])['Giocatore'].apply(list)
        
        rose_per_anno = {}
        for (anno, allenatore), giocatori in grouped.items():
            if anno not in rose_per_anno:
                rose_per_anno[anno] = {}
            rose_per_anno[anno][allenatore] = giocatori
        
        # Ordina gli anni in ordine decrescente
        context['rose_per_anno'] = dict(sorted(rose_per_anno.items(), reverse=True))

    except FileNotFoundError:
        context['error'] = "Il file 'Rose_fantalega(1).xlsx' non è stato trovato. Assicurati che sia nella cartella 'fantalega/fantalega/'."
    except Exception as e:
        context['error'] = f"Si è verificato un errore durante la lettura del file: {e}"
        
    return render(request, 'rose.html', context)