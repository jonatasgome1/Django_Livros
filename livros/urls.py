from django.urls import path
from .views import obter_livros, obter_livro

urlpatterns = [
    path('livros/', obter_livros, name='obter_livros'),
    path('livros/<int:livro_id>/', obter_livro, name='obter_livro'),
]
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('livros.urls')),
]
