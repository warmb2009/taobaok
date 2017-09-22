from django.conf.urls import url
from . import views

urlpatterns = [
#    url(r'^ajax/tbadd/', views.insert_tb_info, name = 'insert_tb_info'),
#   url(r'^ajax/otheradd/', views.insert_other_info, name = 'insert_other_info'),
 	#url(r'^ajax/get/', views.insert_tb_info, name = 'insert_tb_info'),

    url(r'^ajax/qqinfotran', views.trans_qqinfo, name = 'insert_tb_info'),#qqbot的数据转发
    url(r'^ajax/tbinfoadd/', views.get_tbinfo, name = 'get_tbinfo'),#tblogin处理完的数据,发送给django
    url(r'^ajax/wxcom/', views.wx_com, name = 'wx_com'),#处理wx发送的命令
]
