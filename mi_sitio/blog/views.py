from django.shortcuts import render, redirect
from .models import Post # Importamos los posts de la base de datos
from .forms import PostForm
from django.contrib.auth.decorators import login_required # <-- Importamos el decorador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def lista_posts(request):
    # Traemos todos los objetos de la tabla Post
    posts = Post.objects.all().order_by('-fecha_publicacion') 
    
    # Pasamos los posts a la plantilla mediante un diccionario llamado 'context'
    return render(request, 'blog/lista_posts.html', {'posts': posts})


@login_required # <-- Esto protege la vista
def nuevo_post(request):
    if request.method == "POST":
        # El formulario recibe los datos que el usuario escribió
        form = PostForm(request.POST)
        if form.is_valid():
            # Guarda el post en la base de datos de manera segura
            post = form.save(commit=False)
            post.save()
            # Redirige al usuario de vuelta a la lista de posts
            return redirect('lista_posts')
    else:
        # Si no es POST, se crea el formulario vacío listo para llenar
        form = PostForm()
        
    return render(request, 'blog/nuevo_post.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('lista_posts')
    else:
        form = UserCreationForm();
    return render(request, 'blog/registro.html',{'form':form})

