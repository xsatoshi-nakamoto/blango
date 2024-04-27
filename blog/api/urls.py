from rest_framework.routers import DefaultRouter
from . import views as api_views
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router = DefaultRouter()
router.register("posts", api_views.PostViewSet)
# router.register("info", api_views.UserDetail)
router.register("tags", api_views.TagViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path(
    "posts/by-time/<str:period_name>/",
    api_views.PostViewSet.as_view({"get": "list"}),
    name="posts-by-time",
  ),
  path("jwt/", TokenObtainPairView.as_view(), name="jwt_obtain_pair"),
  path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
]