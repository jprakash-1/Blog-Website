from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

# When writing code in it. If we wan tot insert html file try second way 

#
# Here by doing this we are passing data to the html file as imput you can say. . . . . .
#   

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request , 'blog/home.html',context)    


# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False 
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'

    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')




def about(request):
    return render(request , 'blog/about.html')







 
# blog - > templates - > blog - > templates.html
# 
# app folder then templates folder then blog folder then several templates and html files .


 

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>')

# Random data here . . . . . .. 

# post = [
#     {
#         'author' : 'John',
#         'title' : 'Blog 1',
#         'content': 'blog post 1 content',
#         'date' : 'August 27 , 2019'
#     },
#     {
#         'author' : 'Johnny',
#         'title' : 'Blog 2',
#         'content': 'blog post 2 content',
#         'date' : 'August 30 , 2019'
#     }
# ]
