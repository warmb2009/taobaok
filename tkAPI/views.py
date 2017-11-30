from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from tkAPI.models import *

import requests

from tkAPI.models import Item
from tkAPI.serializers import ItemSerializer
from rest_framework import generics, permissions

'''
API
'''
# 获取列表
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# 获取详情
class ItemDetail(generics.ListCreateAPIView):
    model = Item
    queryset = Item.objects.order_by('id')[0:9]
    serializer_class = ItemSerializer
    permission_classes = [  
        permissions.AllowAny  
    ]  

class ItemDetailByTime(generics.ListCreateAPIView):
    model = Item
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        time = self.request.query_params.get('time')
        count = len(self.request.query_params)
        print(count)
        print(self.request.query_params)
        print(time)
        if time:
            print('比较时间')
            querystr = 'item_addtime > ' + time
            queryset = Item.objects.extra(select={'is_recent' : querystr})
        return queryset
    
'''
转发服务
'''
url = 'http://127.0.0.1:8081/ajax/tbadd/'

# post提交数据
def postInfo(name, content, sender):
    data = {'name': name, 'content': content, 'sender': sender}
    r = requests.post(url, data = data)
    
# 转发QQ信息,将qqbot发送的数据转发给tblogin server 8081端口
def trans_qqinfo(request):
    name = request.POST.get('name')
    content = request.POST.get('content')
    sender = request.POST.get('sender')

    postInfo(name, content, sender)
    return HttpResponse('success', content_type='application/json')
