from rest_framework.routers import DefaultRouter
from . import views as api_views
from django.urls import path, include
router = DefaultRouter()
router.register("posts", api_views.PostViewSet)
# router.register("info", api_views.UserDetail)
router.register("tags", api_views.TagViewSet)
urlpatterns = [
  path('', include(router.urls))
]