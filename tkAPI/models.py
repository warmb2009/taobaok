from django.db import models


# 用户表
class WXUser(models.Model):
    # 微信名字
    wx_name = models.CharField(max_length=80)
    # 微信ID
    wx_id = models.CharField(max_length=80)


# 商品种类(普通商品, 大牌商品)
class ItemType(models.Model):
    # 商品种类ID
    item_type_id = models.CharField(max_length=80, unique=True, default='0')
    # 商品种类名称
    item_type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.item_type_name


# 商品分类(家具, 数码, 食品等等)
class ItemCategory(models.Model):
    # 商品分类ID
    item_cate_id = models.CharField(max_length=80, unique=True, default='0')
    # 商品分类名称
    item_cate_name = models.CharField(max_length=30)

    def __str__(self):
        return self.item_cate_name


# 优惠券信息表
class Coupon(models.Model):
    # 优惠券id
    coupon_id = models.IntegerField(unique=True)
    # 优惠券 优惠金额
    coupon_amount = models.IntegerField()
    # 优惠券 满减条件
    coupon_start_fee = models.IntegerField()
    # 优惠券 剩余数量
    coupon_remain_count = models.IntegerField()
    # 优惠券 总量
    coupon_total_count = models.IntegerField()
    # 优惠券 优惠开始时间
    coupon_start_time = models.IntegerField()
    # 优惠券 优惠结束时间
    coupon_end_time = models.IntegerField()

    item = models.ForeignKey('Item', on_delete=models.CASCADE,)

    def __str__(self):
        return self.coupon_amount

    class Meta:
        ordering = ('coupon_id', )


# 商品信息表
class Item(models.Model):
    # 商品ID
    item_id = models.CharField(max_length=80, unique=True, default='0')
    # 商品种类
    item_type = models.ForeignKey(ItemType, default='0', on_delete=models.CASCADE,)
    # 商品类别
    item_category = models.ForeignKey(ItemCategory, default='0', on_delete=models.CASCADE, )
    # 商品链接
    item_url = models.CharField(max_length=300)
    # 商品上架价格
    item_reserve_price = models.CharField(max_length=300, default='0')
    # 商品价格
    item_price = models.CharField(max_length=300, default='0')
    # 优惠券 优惠金额
    coupon_amount = models.CharField(max_length=300, default='0')
    # 优惠券 满减条件
    coupon_start_fee = models.CharField(max_length=300, default='0')
    # 优惠券 剩余数量
    coupon_remain_count = models.CharField(max_length=300, default='0')
    # 优惠券 总量
    coupon_total_count = models.CharField(max_length=300, default='0')
    # 优惠券 优惠开始时间
    coupon_start_time = models.CharField(max_length=300, default='0')
    # 优惠券 优惠结束时间
    coupon_end_time = models.CharField(max_length=300, default='0')
    # 商品优惠券链接
    item_coupon = models.CharField(max_length=300)
    # 商品标题
    item_title = models.CharField(max_length=300)
    # 商品内容文案
    item_content = models.CharField(max_length=300)
    # 商品图片
    item_image = models.CharField(max_length=300)
    # 淘口令
    item_model = models.CharField(max_length=300, default='null')
    # 产地
    item_location = models.CharField(max_length=300, default='null')
    # 分类名字
    item_cat_name = models.CharField(max_length=300, default='null')
    # 二级分类名字
    item_cat_leaf_name = models.CharField(max_length=300, default='null')
    # 是否到期
    item_if_active = models.BooleanField(default=True)

    # 时间戳
    item_add_time = models.DateTimeField(auto_now=True)

    # 销量
    item_volume = models.CharField(max_length=300, default='null')

    # seller id
    item_seller_id = models.CharField(max_length=300, default='null')

    # 在Python3中用 __str__ 代替 __unicode__
    def __str__(self):
        return self.item_title

    class Meta:
        ordering = ('id', )

        
# 订阅表-自动即时发布订阅
class Subscription(models.Model):
    # 一对一外键,与用户表相对
    user_id = models.OneToOneField('WXUser', on_delete=models.CASCADE,)
    # 是否订阅
    if_subscription = models.BooleanField()
