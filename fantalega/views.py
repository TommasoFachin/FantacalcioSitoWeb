from django.shortcuts import render
import openpyxl
import os
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'home.html')

def storia(request):
    return render(request, 'history.html')

def chi_siamo(request):
    # Recupera tutti gli utenti tranne 'admin' e le loro squadre associate
    managers = User.objects.exclude(username='admin').prefetch_related('teams').order_by('username')
    context = {'managers': managers}
    return render(request, 'ChiSiamo.html', context)

def rose_home(request):
    # In futuro, potresti generare questa lista dinamicamente
    # scansionando i file presenti nella cartella.
    seasons = [
        {'id': '2025-2026', 'name': '2025/2026'},
        # Aggiungi qui altre stagioni quando avrai i file
        # {'id': '2024-2025', 'name': '2024/2025'},
    ]
    context = {'seasons': seasons}
    return render(request, 'rose_home.html', context)

def regolamento(request):
    return render(request, 'rulebook_placeholder.html')

def rose(request, year):
    # Passiamo l'anno al template per poterlo mostrare nel titolo
    context = {'error': None, 'teams': {}, 'season_year': year.replace('-', '/')}

    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'fantalega', f'Rose_fantalega_{year}.xlsx'
        )

        wb = openpyxl.load_workbook(file_path)
        sheet = wb.active

        teams = {}
        current_team = None
        slide_finished = False  # <--- serve per ignorare la seconda slide

        for row in sheet.iter_rows(values_only=True):

            # Rimuove colonne vuote
            row = [cell for cell in row if cell is not None]

            # Se la slide 1 è finita, smetti di leggere
            if slide_finished:
                break

            # Se la riga è vuota → ignora
            if len(row) == 0:
                continue

            # Se la riga contiene solo il nome squadra
            # Se la riga contiene solo una cella → potrebbe essere un nome squadra
            if len(row) == 1:
                nome = row[0].strip()

                # IGNORA righe che NON sono nomi squadra
                if (
                    "rose lega" in nome.lower() or
                    "fantalega" in nome.lower() or
                    "ruolo" in nome.lower() or
                    "calciatore" in nome.lower() or
                    "squadra" in nome.lower() or
                    "costo" in nome.lower() or
                    nome.strip() == ""
                ):
                    continue

                # Se è un nome squadra valido → crea il team
                current_team = nome
                teams[current_team] = []
                continue


                # Se è una riga tipo "Ruolo | Calciatore | Squadra / Costo"
                # significa che è iniziata la seconda slide → STOP
                if current_team.lower().startswith("ruolo"):
                    slide_finished = True
                    continue

                teams[current_team] = []
                continue

            # Se la riga contiene almeno 3 colonne (ruolo, calciatore, squadra/costo)
            if len(row) >= 3 and current_team is not None:
                ruolo = row[0]
                calciatore = row[1]
                squadra = row[2]
                costo = row[3]

                teams[current_team].append({
                    "ruolo": ruolo,
                    "calciatore": calciatore,
                    "squadra": squadra,
                    "costo": row[3]
                })

        context["teams"] = teams

    except FileNotFoundError:
        context["error"] = (
            f"Il file delle rose per la stagione {year} non è stato trovato."
        )

    except Exception as e:
        context["error"] = f"Errore durante la lettura del file: {e}"

    return render(request, 'rose.html', context)
