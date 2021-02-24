from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('<int:pk>/viewpost/', views.ViewPostView.as_view(), name='viewpost'),
    path('<int:pk>/editpost/', views.EditPostView.as_view(), name='editpost'),
    path('browse/', views.BrowsePostsView.as_view, name='browse'),
    path('<int:post_postNumber>/<int:comment_id>/comment/', views.CommentView.as_view, name='comment'),
    path('addpost/', views.AddPostView.as_view, name='addpost'),
    path('<int:post_postNumber>/postsubmitted/', views.PostSubmitted.as_view, name='postsubmitted'),
    path('postedited/', views.PostEdited.as_view, name='postedited')
]
