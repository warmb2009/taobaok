from rest_framework import serializers
from tkAPI.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id',
                  'item_id',
                  'item_type',
                  'item_category',
                  'item_url',
                  'item_reserve_price',
                  'item_price',
                  'item_volume',
                  'item_seller_id',
                  'item_model',
                  'coupon_amount',
                  'coupon_start_fee',
                  'coupon_remain_count',
                  'coupon_total_count',
                  'coupon_start_time',
                  'coupon_end_time',
                  'item_coupon',
                  'item_title',
                  'item_content',
                  'item_cat_name',
                  'item_cat_leaf_name',
                  'item_image',
                  'item_location',
                  'item_if_active',
                  'item_add_time')


