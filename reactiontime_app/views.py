from django.shortcuts import render

def start_game(request):
    return render(request, 'game/start.html')

def play_game(request):
    return render(request, 'game/play.html')

def end_game(request):
    score = request.GET.get('score', 0)
    return render(request, 'game/end.html', {'score': score})
