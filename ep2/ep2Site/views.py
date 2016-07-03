from django.shortcuts import render

def music_list(request):

    return render(request, 'ep2Site/music_list.html', {})