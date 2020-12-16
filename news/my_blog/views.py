from django.shortcuts import render, get_object_or_404
from .models import My_Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Show_blog(ListView):
    model = My_Blog
    context_object_name = 'My_Blog'
    template_name = 'my_blog/all_blog.html'
    ordering = ['-date']
    paginate_by = 4


class BlogDetailView(DetailView):
    model = My_Blog
    context_object_name = 'post'


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = My_Blog
    fields = ['title', 'description', 'date', 'time']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class blogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = My_Blog
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by:
            return True
        return False


class New_blog_create(CreateView, LoginRequiredMixin):
    model = My_Blog
    fields = ['title', 'description', 'date', 'time']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
