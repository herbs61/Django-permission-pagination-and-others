from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.


def movie_list(request):
    movie_objects = Movies.objects.all()
    
    movie_name = request.GET.get('movie_name')
    
    #Seach bar
    if movie_name != '' and movie_name is not None:
        #The name__icontains make it much flexible it doesn't only take the exact movie_name but also if one letter is part of it also produces it
        movie_objects = movie_objects.filter(name__icontains=movie_name)
    
    # Pagination
    paginator = Paginator(movie_objects,4)
    page = request.GET.get('page')
    movie_objects = paginator.get_page(page)
    
    return render(request,'newapp/movie_list.html',{'movie_objects':movie_objects})
    