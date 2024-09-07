from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path(
        'api/', include('blog_api.urls', namespace='blog_api')),
    path(
        'api-auth/', include('rest_framework.urls')),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path(
        'admin/', admin.site.urls),
    path(
        '', include('blog.urls', namespace='blog')),
    path(
        'sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path(
        'accounts/', include('accounts.urls')),
    path(
        'accounts/', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
