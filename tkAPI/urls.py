from django.conf.urls import url, include

from . import views
from . import models

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^ajax/qqinfotran', views.trans_qqinfo, name='trans_qqinfo'),  # qqbot的数据转发
    url(r'tkapis/$', views.ItemDetailByID.as_view()),
    url(r'tkapis/create/', views.ItemCreate.as_view()),
    url(r'tkapis/update/(?P<item_id>\d+)/$', views.ItemUpdate.as_view()),
    url(r'tkapis/(?P<itemid>[a-z0-9]+)/$', views.ItemDetailByID.as_view())
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
