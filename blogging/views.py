from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from blogging.models import Post

def list_view(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    
    if request.method == "POST":
        if request.POST.get("vote") == "Yes":
            post.score += 1
        else:
            post.score -= 1
        post.save()
        
    context = {'post': post}
    return render(request, 'posting/detail.html', context)