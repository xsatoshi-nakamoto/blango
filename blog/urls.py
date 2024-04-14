from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post_list'),  # URL for listing blog posts
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
]