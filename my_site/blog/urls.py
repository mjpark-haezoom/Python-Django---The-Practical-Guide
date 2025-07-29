from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import StartingPageView, AllPostsView, SinglePostView, ReadLaterView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"), 
    path("posts", views.AllPostsView.as_view(), name="posts-page"), 
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"), # dynamic segment (angle bracket), parameter name -> /posts/my-first-post
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
Q. Slug?
"""
