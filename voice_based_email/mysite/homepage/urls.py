from django.conf.urls import url, include
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.login_view, name="login"),
    url(r'^compose/$', views.compose_view, name="compose"),
    url(r'^inbox/$', views.inbox_view, name="inbox"),
    url(r'^sent/$', views.sent_view, name="sent"),
    url(r'^trash/$', views.trash_view, name="trash"),
    url(r'^options/$', views.options_view, name="options")
   
]
