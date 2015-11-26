from django.conf.urls import url

from .views import CustomUserUpdate, CustomUserDetail, CustomUserList

urlpatterns = [
    url(r'^profile/(?P<slug>[\w\-]+)/$', CustomUserDetail.as_view(), name='detail'),
    url(r'(?P<slug>[\w\-]+)/update/$', CustomUserUpdate.as_view(), name='update'),
    url(r'^profile/$', CustomUserList.as_view(), name='profile'),
]
