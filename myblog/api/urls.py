from django.conf.urls import include,url
from . import views


urlpatterns = [

    url(r'^posts/$', views.post_lists),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_detail),
]
