from django.db import models

#用户表
class users(models.Model):
        #微信名字
        wx_name = models.CharField(max_length = 80)
        #微信ID
        wx_id = models.CharField(max_length = 80)
        
#商品信息表
class items(models.Model):
        #商品ID
        item_id = models.CharField(max_length = 80)
        #商品链接
        item_url = models.CharField(max_length = 300)
        #商品优惠券链接
        item_coupon = models.CharField(max_length = 300)
        #商品标题
        item_title = models.CharField(max_length = 80)
        #商品内容文案
        item_content = models.CharField(max_length = 300)
        #商品图片
        item_image = models.CharField(max_length = 300)
        #是否到期
        item_if_active = models.BooleanField()
        
#订阅表-自动即时发布订阅
class subscription(models.Model):
        #一对一外键,与用户表相对
        user_id = models.OneToOneField('users')
        #是否订阅
        if_subscription = models.BooleanField()
