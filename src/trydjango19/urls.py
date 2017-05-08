"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from django.contrib import admin
# from contacts import views as contact_view # this in future
#from posts import views as post_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^posts/$', post_view.posts_home)  # if we use the above import statment, then we can enable this
    url(r'^posts/', include("posts.urls", namespace = 'posts')),
    # url(r'^posts/$', "<app_name>.views.<function_name>"),
    ## here the url for class based views are different and function based views are different
    url(r'^explorer/', include('explorer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
