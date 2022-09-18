from django.shortcuts import render

from posts.models import Post, Model


def main(request):
    posts = Post.objects.all()
    models = Model.objects.all()

    data = {
        'posts': posts,
        'model': models
    }

    return render(request, 'main.html', context=data)

