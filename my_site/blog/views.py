from datetime import date

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Post
from .forms import CommentForm


# 3개의 뷰

class StartingPageView(ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"
    ordering = ["-date"]


class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post
    
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        stored_posts = request.session.get("stored_posts")
        
        context = {
            "post": post,
            "post_tag": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}
        
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
            
        return render(request, "blog/stored-posts.html", context)
    
    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)
        request.session["stored_posts"] = stored_posts # 저장
        return HttpResponseRedirect("/")


# def starting_point (request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     # SQL 구문으로 바꿔서 모든 데이터를 가져오지 않고 일부 부분만 가져옴. 장고에서 -index는 지원하지 않음.
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.post = identified_post
#             comment.save()
#             return redirect("post-detail-page", slug=slug)

#     else:
#         comment_form = CommentForm()

#     return render(request, "blog/post-detail.html", {
#                 "post": identified_post,
#                 "post_tags" : identified_post.tags.all(),
#                 "comments" : identified_post.comments.all(), # 연결된 댓글들
#                 "comment_form": comment_form
#             })

# def read_later(request):
#     stored_posts = request.session.get("stored_posts") # 저장된 게시물 id 리스트

#     context = {}

#     if stored_posts is None or len(stored_posts) == 0:
#         context["posts"] = []
#         context["has_posts"] = False
#     else:
#         posts = Post.objects.filter(id__in=stored_posts) # id를 기준으로 Post 객체를 불러옴
#         context["posts"] = posts
#         context["has_posts"] = True

#     return render(request, "blog/stored-posts.html", context)

"""
URLConf(urls.py)에서 받은 slug 문자열이 post_detail() 함수의 두 번째 인자로 들어옴.
"""
