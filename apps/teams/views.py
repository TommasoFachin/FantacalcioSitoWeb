from django.http import HttpResponse
from .models import Team

def team_list(request):
    teams = Team.objects.all()
    if not teams:
        return HttpResponse("Nessuna squadra presente.")
    teams_names = ', '.join([team.name for team in teams])
    return HttpResponse(f"Lista squadre: {teams_names}")

def team_detail(request, team_id):
    try:
        team = Team.objects.get(pk=team_id)
        return HttpResponse(f"Dettagli squadra {team.id}: {team.name}, proprietario {team.owner.username}")
    except Team.DoesNotExist:
        return HttpResponse(f"Squadra con id {team_id} non trovata.", status=404)