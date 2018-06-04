from django.conf.urls import url
from pages import views

urlpatterns = [
    url(r'^user_list/', views.user_list),
    url(r'^user_list/(?P<page>\d+)/$', views.user_list),
]
