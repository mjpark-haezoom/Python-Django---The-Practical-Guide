from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_point, name="starting-page"), 
    path("posts", views.posts, name="posts-page"), 
    path("posts/<slug:slug>", views.post_detail, 
         name="post-detail-page") # dynamic segment (angle bracket), parameter name -> /posts/my-first-post
] 

"""
Q. Slug?
"""
