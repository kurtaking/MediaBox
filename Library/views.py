from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from Library.models import Vinyl, User

from .forms import AddVinylForm

def index(request):
    return render(request, 'Library/index.html')

def user_dashboard(request):
    return render(request, 'Library/user_dashboard.html')

def libraries(request):
    return render(request, 'Library/libraries.html')

def vinyls(request):
    vinyls = Vinyl.objects.order_by('artist', 'year', 'title')

    if request.method == 'POST':
        new_form = AddVinylForm()
        form = AddVinylForm(request.POST)

        if form.is_valid():
            vinyl = form.save()

            return HttpResponseRedirect(request, 'Library/vinyls.html', {
                'vinyls': vinyls,
                'form': new_form,
            })
    else:
        form = AddVinylForm()

    return render(request, 'Library/vinyls.html', {
        'vinyls': vinyls,
        'form': form,
    })

def vinyl_detail(request, id):
    try:
        vinyl = Vinyl.objects.get(id=id)
    except Vinyl.DoesNotExist:
        raise Http404('This vinyl does not exist')
    return render(request, 'Library/vinyl_detail.html', {
        'vinyl': vinyl,
    })


def by_artist(request):
    vinyls = Vinyl.objects.all()
    artists = []
    temp = []

    for vinyl in vinyls:
        temp.append(vinyl)
        if vinyl.artist not in temp:
            artists.append(vinyl)

    for item in artists:
        print(item.artist)


    return render(request, 'Library/vinyls.html')


def movies(request):
    return render(request, 'Library/movies.html')

def video_games(request):
    return render(request, 'Library/video_games.html')

def books(request):
    return render(request, 'Library/books.html')

def settings(request):
    users = User.objects.all()
    context = {'users': users}

    return render(request, 'Library/settings.html', context)
