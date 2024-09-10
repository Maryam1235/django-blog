from typing import Any
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import Feed,User,Comment
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse

class Login(LoginView):
    template_name="login.html"
    fields=["username","password"]
    success_url=reverse_lazy("home")
    
class Register(CreateView):
    model=User
    template_name="register.html"
    fields=["first_name","last_name","email","phone_number","username","password"]
    login_url=reverse_lazy("login")
    success_url=reverse_lazy("home")

class Logout(LogoutView):
    next_page=reverse_lazy("home")
    
class Home(ListView):
    model = Feed
    template_name = "index.html"
    
class CreateFeed(LoginRequiredMixin,CreateView):
    model = Feed
    fields=["text","image"]
    template_name = "create_post.html"
    success_url = reverse_lazy("home")
    login_url=reverse_lazy("login")
    
    def form_valid(self, form):
        """ Associate post with the current logged in user as its author"""
        
        # get the id of current logged in user
        user_id = self.request.user.id
        
        # retrieve the user with this id
        user = User.objects.get(id=user_id)
        
        # add author to the post
        form.instance.author = user
        
        # form.instance.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)
    
class FeedDetailedView(DetailView):
    model=Feed
    template_name="feed_detail.html"
    def  get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        feed_id=self.kwargs["pk"]
        context["comments"] = Comment.objects.filter(feed=feed_id)
        return context

class CreateComment(LoginRequiredMixin,CreateView):
    model=Comment
    fields=["text","feed"]
    template_name="feed_detail.html"
    success_url=reverse_lazy("home")
    login_url=reverse_lazy("login")
    
    def form_valid(self, form):
        """ Associate comment with the current logged in user as its author"""

        # get the id of current logged in user
        user_id = self.request.user.id

        # retrieve the user with this id
        user = User.objects.get(id=user_id)

        # add author to the post
        form.instance.author = user

        # form.instance.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feed"] = Feed.objects.get(id=self.kwargs["pk"])
        return context
    

class UpdateFeed(LoginRequiredMixin, UpdateView):
    model = Feed
    fields = ['text', 'image']
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        """Ensure that only the author can update the post."""
        return self.model.objects.filter(author=self.request.user)

class DeleteFeed(LoginRequiredMixin, DeleteView):
    model = Feed
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def get_queryset(self):
        """Ensure that only the author can delete the post."""
        return self.model.objects.filter(author=self.request.user)
    

    
