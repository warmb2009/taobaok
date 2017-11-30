from django.db import models

#用户表
class WXUser(models.Model):
    #微信名字
    wx_name = models.CharField(max_length = 80)
    #微信ID
    wx_id = models.CharField(max_length = 80)
        
#商品信息表
class Item(models.Model):
    # 商品ID
    item_id = models.CharField(max_length = 80, unique = True, default = '0')
    # 商品链接
    item_url = models.CharField(max_length = 300)
    # 商品优惠券链接
    item_coupon = models.CharField(max_length = 300)
    # 商品标题
    item_title = models.CharField(max_length = 80)
    # 商品内容文案
    item_content = models.CharField(max_length = 300)
    # 商品图片
    item_image = models.CharField(max_length = 300)
    # 淘口令
    item_model = models.CharField(max_length = 300, default = 'null')
    # 产地
    item_location = models.CharField(max_length = 300, default = 'null')
    # 是否到期
    item_if_active = models.BooleanField()

    # 时间戳
    item_addtime = models.DateTimeField(auto_now_add = True)
    def __str__(self):# 在Python3中用 __str__ 代替 __unicode__
        return self.item_title

    class Meta:
        ordering = ('id', )

#订阅表-自动即时发布订阅
class Subscription(models.Model):
    #一对一外键,与用户表相对
    user_id = models.OneToOneField('WXUser')
    #是否订阅
    if_subscription = models.BooleanField()
    
