from django.shortcuts import render
from posts.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})

def post(request, post_id):
    return render(request, 'posts/post.html', {'post_id':post_id})
