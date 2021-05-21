from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^logout/$", views.logout_request, name="logout"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.log_in, name='login'),
]