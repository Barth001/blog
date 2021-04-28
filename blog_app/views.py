from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .models import Comment, Post
from .form import CommentForm
from django.urls import reverse_lazy
# Create your views here.

class CreatePost(CreateView):
    model = Post
    template_name = "post.html"
    fields = ["title", "author", "body"]


class UpdatePost(UpdateView):
    model = Post
    template_name = "edit.html"
    fields = ["title", "body"]


class DeletePost(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")

def home(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'home.html', context)

def detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            return redirect('detail', pk)
    else:
        form = CommentForm()
    context = {'post': post, 'form':form}
    return render(request, 'detail.html', context)
