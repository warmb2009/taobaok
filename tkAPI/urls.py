from django.conf.urls import url, include

from . import views
from . import models

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
#    url(r'^ajax/tbadd/', views.insert_tb_info, name = 'insert_tb_info'),
#   url(r'^ajax/otheradd/', views.insert_other_info, name = 'insert_other_info'),
 	#url(r'^ajax/get/', views.insert_tb_info, name = 'insert_tb_info'),


#    url(r'^ajax/tbinfoadd/', views.get_tbinfo, name = 'get_tbinfo'),#tblogin处理完的数据,发送给django
#    url(r'^ajax/wxcom/', views.wx_com, name = 'wx_com'),#处理wx发送的命令
#    url(r'^tkapi/$', views.item_list),
#    url('r^snippets/(?P<pk>)')
    
    url(r'^ajax/qqinfotran', views.trans_qqinfo, name = 'trans_qqinfo'),#qqbot的数据转发
#    url(r'tkapi/$', views.ItemList.as_view()),
#    url(r'tkapis/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
#    url(r'tkapis/$', views.ItemDetail.as_view()),
    url(r'tkapis/$', views.ItemDetailByTime.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)
