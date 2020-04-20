from django.urls import path
# class base view imported...
from .views import PostListView, PostDetailListView,PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailListView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view()),

    path('about/', views.about, name='blog-about'),
]
