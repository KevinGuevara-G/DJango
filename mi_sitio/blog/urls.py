from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('post/nuevo/', views.nuevo_post, name='nuevo_post'),
    path('registro/', views.registro, name='registro')
]