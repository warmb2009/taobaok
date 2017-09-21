from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import items
import requests

#从QQ群发送的内容中获取信息
@csrf_exempt
def insert_tb_info(request):
    itemid = request.POST.get('itemid')
    title = request.POST.get('title')
    price = request.POST.get('price')
    coupon = request.POST.get('coupon')
    commodity = request.POST.get('commodity')
    content = request.POST.get('content')
    
    if coupon is '' or commodity is '':
        print('coupon is not true')
        return HttpResponse('error!!', content_type='application/json')
    else:
        de = models.items.objects.get(item_id = itemid)
        if de is None:
            item = items(item_id = itemid, item_title = title, item_coupon = coupon, item_url = commodity, item_content = content)
            item.save()
        else:
            return HttpResponse('error, exist itemid', content_type='application/json')
        return HttpResponse('success', content_type='application/json')
    
url = 'http://127.0.0.1:8080/ajax/tbadd/'

# post提交数据
def postInfo(name, content, sender):
    data = {'name': name, 'content': content, 'sender', sender}
    r = requests.post(url, data = data)
    
# 转发QQ信息,将qqbot发送的信息原封不动的转发给tblogin server 端口8081
def trans_qqinfo(request):
    name = request.POST.get()
    content = request.POST.get()
    sender = request.POST.get()

    postInfo(name, content, sender)


# tblogin将qq信息处理完毕后,发送给此server 用于商品信息存储
def get_tbinfo(request):
    itemid = request.POST.get('itemid')
    title = request.POST.get('title')
    price = request.POST.get('price')
    coupon = request.POST.get('coupon')
    commodity = request.POST.get('commodity')
    content = request.POST.get('content')

    
    if coupon is '' or commodity is '':
        print('coupon is not true')
        return HttpResponse('error!!', content_type='application/json')
    else:
        de = models.items.objects.get(item_id = itemid)
        if de is None:
            item = items(item_id = itemid, item_title = title, item_coupon = coupon, item_url = commodity, item_content = content)
            item.save()
        else:
            return HttpResponse('error, exist itemid', content_type='application/json')
        return HttpResponse('success', content_type='application/json')
    
    return

# 接受微信用户发送的命令,并执行命令,将结果发回wx server
def wx_com(request):
    
    return
