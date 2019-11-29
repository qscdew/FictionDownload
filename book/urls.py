"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from homepage import views
from django.views.generic.base import RedirectView
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from book.sitemap import BlogSitemap
import homepage.models
import homepage.forms

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
# 配置全局404页面
hander404 = 'myblog.views.page_not_found'
sitemaps = {
    'static': BlogSitemap,
}
# 配置全局505页面
hander505 = 'myblog.views.page_errors'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.index,name='index'),
    url(r'^booklist/', views.booklist,name='booklist'),
    url(r'^books/(?P<book_id>\d+)/$',views.book,name='book'),
    url(r'^book/read/(?P<book_id>\d+)/$',views.read,name='read'),
    url(r'^writers/(?P<writer_id>\d+)/$',views.writer,name='writer'),
    url(r'^newbook/', views.newbook,name='newbook'),
    url(r'^xz/(?P<book_name>\S+)/$',views.file_down,name='down'),
    url(r'^down/(?P<book_name>\S+)/$',views.zip_down,name='zipdown'),
    url(r'^web/(?P<web_name>\S+)/$',views.web_view,name='webview'),
    url(r'^newwriter/', views.newwriter,name='newwriter'),
    url(r'^users/', include('users.urls', namespace='users')), 
    url(r'^favicon\.ico$', favicon_view),
    url(r'^bbs/', views.newliuyan,name='liuyan'),
    url(r'^jielong/', views.jielong,name='jielong'),
    url(r'^myn/', views.myn,name='myn'),
    
 url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    url(r'^v/(?P<video_name>\S+)/$',views.video,name='v'),
    url(r'^jwc/', views.jwc,name='jwc'),

    
    
]
