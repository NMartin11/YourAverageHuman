from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, NameForm


# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_index.html', {'posts': posts})


def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form2 = NameForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        form2 = NameForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'form2': form2})
