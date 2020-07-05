from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Noticia
from .forms import PostForm
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

#JuKaMaSa
# Create your views here.

def index(request):
    postsDestaque = Noticia.objects.filter(destaque=True)
    posts = Noticia.objects.filter(published_date__lte=timezone.now(), destaque=False).order_by('published_date')
    return render(request, 'aluno/index.html', {'posts': posts, 'posts_destaque': postsDestaque })

def user(request):
    return render(request, 'aluno/user.html', {})

def post_list(request):
    posts = Noticia.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'aluno/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    return render(request, 'aluno/post_detail.html', {'post': post})
    
def post_new(request):
    if not request.user.has_perm('aluno.add_noticia'):
        raise PermissionDenied
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'aluno/post_edit.html', {'form': form})
    
def post_edit(request, pk):
    if not request.user.has_perm('aluno.change_noticia'):
        raise PermissionDenied
    post = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'aluno/post_edit.html', {'form': form})
    
def post_remove(request, pk):
    if not request.user.has_perm('aluno.delete_noticia'):
        raise PermissionDenied
    post = get_object_or_404(Noticia, pk=pk)
    post.delete()
    return redirect('post_list')    
    
    