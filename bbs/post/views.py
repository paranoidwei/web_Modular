from math import ceil

from django.shortcuts import render, redirect

from post.models import Post


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request, 'create.html')


def edit(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(id=post_id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'post': post})


def read(request):
    post_id = int(request.GET.get('post_id'))
    try:
        post = Post.objects.get(id=post_id)
        return render(request, 'read.html', {'post': post})
    except Post.DoesNotExist:
        return redirect('/')

def post_list(request):
    page = int(request.GET.get('page', 1))  # 当前页码，默认为 1

    per_page = 5
    # 计算总页数
    total = Post.objects.count()
    pages = ceil(total / per_page)

    # 取出本页需要现实的文章
    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.all()[start:end]
    return render(request, 'post_list.html', {'posts': posts, 'pages': range(pages)})

def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})