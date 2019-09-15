from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from blogging.models import Post

def list_view(request):
    # published = Post.objects.exclude(published_date__exact=None)
    # posts = published.order_by('-published_date')
    # context = {'posts': posts}
    # return render(request, 'list.html', context)

    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html")
    
    # context = {'posts': Post.objects.all()}
    # return render(request, 'blogging/list.html', context)

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

def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs:\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")