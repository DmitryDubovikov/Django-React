from django.urls import path, include

# from rest_framework import routers
from rest_framework_nested import routers

from main.user.views import UserViewSet
from main.post.views import PostViewSet
from main.comment.views import CommentViewSet

from main.auth.views import RegisterViewSet, LoginViewSet, RefreshViewSet

router = routers.SimpleRouter()

router.register(r"auth/register", RegisterViewSet, basename="auth-register")
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

router.register(r"user", UserViewSet, basename="user")

router.register(r"post", PostViewSet, basename="post")

posts_router = routers.NestedSimpleRouter(router, r"post", lookup="post")
posts_router.register(r"comment", CommentViewSet, basename="post-comment")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
