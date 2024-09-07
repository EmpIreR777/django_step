from django.urls import path, re_path
from drf_spectacular.views import (
                                SpectacularAPIView,
                                SpectacularRedocView,
                                SpectacularSwaggerView)

from .views import PostList, PostDetail, UserPostList


app_name = 'blog_api'

urlpatterns = [
    path(
        '<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path(
        '', PostList.as_view(), name='post_list'),
    re_path(
        '^user/(?P<username>.+)/$', UserPostList.as_view()),
    path(
        'schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/redoc/', SpectacularRedocView.as_view(url_name='blog_api:schema'), name='redoc'),
    path(
        'schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='blog_api:schema'), name='swagger-ui'),
]
