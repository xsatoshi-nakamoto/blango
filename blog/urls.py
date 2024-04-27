from django.urls import path, include
from . import views
import debug_toolbar
from django.conf import settings


urlpatterns = [
    path('', views.index, name='post_list'),  # URL for listing blog posts
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path("ip/", views.get_ip),
]

# if settings.DEBUG:
#   urlpatterns += [
#       path("__debug__/", include("debug_toolbar.urls")),
#   ]
