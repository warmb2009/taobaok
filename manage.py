#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
#from wxpy import *
#from tkAPI import BotValue
#from tkAPI.tbk.TbkItemConvert import *

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taobaok.settings")

    from django.core.management import execute_from_command_line

    '''
    bot = Bot(console_qr = True, cache_path = "/home/jeroen/wxpy.pkl")

    # 自动接受新的好友请求
    @bot.register(msg_types=FRIENDS)
    def auto_accept_friends(msg):
        # 接受好友请求
        new_friend = msg.card.accept()
        # 向新的好友发送消息
        new_friend.send('哈哈，我自动接受了你的好友请求')

    print(bot)
    BotValue.set_value(bot)

    #登陆淘宝联盟
    print('登陆淘宝联盟')
    tk = TbkItemConvertCommodity()
    BotValue.set_tk_value(tk)

    #存储pid
    pid = 'mm_40512286_19754960_68174640'
    BotValue.set_pid(pid)
    '''
    execute_from_command_line(sys.argv)
