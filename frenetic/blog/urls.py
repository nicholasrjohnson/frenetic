from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('post/<int:pk>/', views.ViewPostView.as_view(), name='viewpost'),
    path('post/<int:pk>/edit/', views.EditPostView.as_view(), name='editpost'),
    path('post/<int:pk>/add', views.AddPostView.as_view, name='addpost'),
    path('post/browse/', views.BrowsePostsView.as_view, name='browse'),
    path('post/<int:post_postNumber>/<int:comment_id>/comment/', views.CommentView.as_view, name='comment'),
    path('<int:post_postNumber>/postsubmitted/', views.PostSubmitted.as_view, name='postsubmitted'),
    path('postedited/', views.PostEdited.as_view, name='postedited')
]
