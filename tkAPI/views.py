from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from tkAPI.models import *

import requests
import datetime 

from tkAPI.models import Item
from tkAPI.serializers import ItemSerializer
from rest_framework import generics, permissions
# from rest_framework
# class ItemResource()

'''
API
'''


# 获取列表 [失效]
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


# 获取详情 [失效]
class ItemDetail(generics.ListCreateAPIView):
    model = Item
    queryset = Item.objects.order_by('id')[0:9]
    serializer_class = ItemSerializer
    permission_classes = [  
        permissions.AllowAny  
    ]  


# 传入数据,获取数据 [计划改为　只获取的接口]
class ItemDetailByID(generics.ListAPIView):
    lookup_url_kwarg = 'itemid'
    model = Item
    serializer_class = ItemSerializer
    lookup_field = 'item_id'

    # 获取数据
    def get_queryset(self):
        if self.kwargs:
            print(self.kwargs['itemid'])            
            gt_item_id = self.kwargs['itemid']
            now = datetime.datetime.now()
            today = datetime.datetime(now.year, now.month, now.day, 0, 0, 0)
            yestoday = datetime.datetime(now.year, now.month, now.day-1, 0, 0, 0)

            if gt_item_id == '0':  # return the last item
                queryset = Item.objects.filter(item_add_time__gt=today)
                return queryset
            elif gt_item_id == '1111':  # return last 10 items
                queryset = Item.objects.order_by('-id')[:10]
                return queryset
            elif gt_item_id == '01':  # return todays items, for custom first open usage
                queryset = Item.objects.filter(item_add_time__gt=today).order_by('-item_add_time')
                return queryset
            elif gt_item_id == '02':
                queryset = Item.objects.all()/order_by('-item_add_time')
            # get item by item_id
            queryset = Item.objects.filter(item_id=gt_item_id)
            return queryset


# 创建Item数据接口
class ItemCreate(generics.CreateAPIView):
    lookup_url_kwarg = 'item_id'
    lookup_field = 'item_id'
    model = Item
    serializer_class = ItemSerializer


# 更新Item数据接口
class ItemUpdate(generics.UpdateAPIView):
    queryset = Item.objects.all()
    lookup_url_kwarg = 'item_id'
    lookup_field = 'item_id'
    model = Item
    serializer_class = ItemSerializer


'''
    def create(self, request, *args, **kwargs):
        mymodel = None
        item_id = request.data.get("item_id")

        if item_id:
            mymodel = self.get_object(item_id)

            if mymodel:
                return self.update(request, *args, **kwargs)
            else:
                return self.create(request, *args, **kwargs)

'''

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
