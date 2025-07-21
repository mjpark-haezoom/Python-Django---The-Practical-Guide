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
여기서 <slug:slug>는 동적 경로(dynamic segment)를 의미함. 
사용자가 /posts/my-first-post 같은 주소에 접근하면,
ex) "my-first-post"가 slug라는 이름의 변수로 추출되어
views.post_detail() 함수에 인자로 전달됩니다.
"""
