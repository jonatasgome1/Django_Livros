from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Livro

def obter_livros(request):
    livros = Livro.objects.all()
    data = {'livros': list(livro.to_dict() for livro in livros)}
    return JsonResponse(data)

def obter_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    data = {'livro': livro.to_dict()}
    return JsonResponse(data)
