from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, HttpResponse, Http404, redirect

def index(request):
    return HttpResponse("<h3>Main page</h3")



CATEGORIES = (
    "action",
    "comedy",
    "tv_shows",
)

def catalog_view(request):
    if request.GET:
        params = request.GET
        id_ = params.get('mov_id')
        print(id_)
    return HttpResponse("<h3>Main page</h3>actions</p>TV shows</p>")


def catalog_detail_view(request, cat):
    if cat not in CATEGORIES:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h3>Main page</h3>{cat}</p>")


def movie_detail_view(request, cat, mov_id):
    return HttpResponse(f"<h3>{cat}</h3>{mov_id}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")