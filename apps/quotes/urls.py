from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^login$', views.login),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    url(r'^add$', views.add),
    url(r'^favorite/(?P<quote_id>\d+)$', views.favorite),
    url(r'^remove/(?P<quote_id>\d+)$', views.remove),
    url(r'^user_page/(?P<id>\d+)$', views.user_page),
    url(r'^logout', views.logout),
]