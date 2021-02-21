from django.shortcuts import render

# Create your views here.

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
    template_name = 'blog/viewpost.html'
