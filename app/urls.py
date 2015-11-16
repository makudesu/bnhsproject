from django.conf.urls import url

from .views import CustomUserUpdate 

urlpatterns = [
    url(r'(?P<slug>[\w\-]+)/update/$', CustomUserUpdate.as_view(), name='update'),
]
