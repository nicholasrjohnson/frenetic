from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Profile, User, Author, CommentAuthor, Post, Comment

class IndexView():
    template_name = 'blog/index.html'
    
class LoginView():
    template_name = 'blog/login.html'

class BrowseView():
    template_name = 'blog/browse.html'

class RegisterView():
    template_name = 'blog/register.html'

class ViewPostView():
    template_name = 'blog/viewpost.html'

class EditPostView():
    template_name = 'blog/edit.html'

class CommentView():
    template_name = 'blog/comment.html' 

