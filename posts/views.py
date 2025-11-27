from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment

def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(parent=None)

    if request.method == "POST":
        if request.user.is_authenticated:
            content = request.POST.get('content')
            parent_id = request.POST.get('parent_id')
            parent_comment = None
            if parent_id:
                parent_comment = Comment.objects.get(id=parent_id)
            if content:
                Comment.objects.create(post=post, author=request.user, content=content, parent=parent_comment)
                return redirect('posts:post_detail', pk=post.pk)
        else:
            return redirect('accounts:login')

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        Post.objects.create(
            title=title,
            content=content,
            author=request.user,
            image=image,
            video=video
        )
        return redirect('posts:home')
    return render(request, 'posts/post_create.html')

@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('posts:home')

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect('posts:home')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    if request.user == comment.author:
        comment.delete()
    return redirect('posts:post_detail', pk=post_pk)
