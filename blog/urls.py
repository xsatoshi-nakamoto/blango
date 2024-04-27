from django.urls import path, include
from . import views
import debug_toolbar
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .api import views as api_views
router = DefaultRouter()
router.register("posts", api_views.PostViewSet)
router.register("addresses", api_views.UserDetail)
router.register("tags", api_views.TagViewSet)


urlpatterns = [
    path('', views.index, name='post_list'),  # URL for listing blog posts
    path("post/<slug>/", views.post_detail, name="blog-post-detail"),
    path("ip/", views.get_ip),
    path('api/', include(router.urls)),
]

# if settings.DEBUG:
#   urlpatterns += [
#       path("__debug__/", include("debug_toolbar.urls")),
#   ]

# Question 2: Configure the router

