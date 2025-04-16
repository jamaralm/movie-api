import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Genre

@csrf_exempt
def genre_view(request):
    if request.method == 'GET':
        genres_list = Genre.objects.all()
        data = [{'id': genre.id, 'genre_name': genre.name} for genre in genres_list]

        return JsonResponse(data, safe=False)
    
    elif request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        
        return JsonResponse({'id':new_genre.id, 'name': new_genre.name}, status=201)
    
@csrf_exempt
def genre_by_id_view(request,pk):
    genre = get_object_or_404(Genre, id=pk)
    data = {'id': genre.id, 'name': genre.name}

    if request.method == "GET":
        return JsonResponse(data, safe=False, status=200)
    
    elif request.method == "DELETE":
        genre.delete(keep_parents=False)
        return JsonResponse({'id': data['id'], 'name': data['name']}, status=200)
    
    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()

        return JsonResponse({'id':genre.id, 'name': genre.name}, status=200)