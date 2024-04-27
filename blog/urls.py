from django.urls import path, include
from . import views

from django.conf import settings



urlpatterns = [
    path('', views.index, name='post_list'),  # URL for listing blog posts
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path("ip/", views.get_ip),

]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         path("__debug__/", include("debug_toolbar.urls")),
#     ]

# Question 2: Configure the router

