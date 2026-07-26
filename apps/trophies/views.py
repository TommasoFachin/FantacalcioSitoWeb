from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Count, Q

User = get_user_model()

def trophy_list(request):
    # Annotiamo il conteggio specifico per ogni tipo di trofeo
    users_stats = User.objects.annotate(
        total_trophies=Count('trophies'),
        scudetti=Count('trophies', filter=Q(trophies__title='Scudetto')),
        coppe_italia=Count('trophies', filter=Q(trophies__title='Coppa Italia')),
        supercoppe=Count('trophies', filter=Q(trophies__title='Supercoppa')),
    ).order_by('-scudetti', '-coppe_italia', '-supercoppe')

    # Se il database è ancora vuoto (o c'è solo l'admin), mostriamo 10 squadre fittizie come richiesto
    show_placeholders = users_stats.count() <= 1
    placeholders = [f"Squadra {i}" for i in range(1, 11)] if show_placeholders else []

    return render(request, 'trophies/trophy_list.html', {
        'users': users_stats,
        'show_placeholders': show_placeholders,
        'placeholders': placeholders
    })