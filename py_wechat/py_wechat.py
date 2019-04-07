from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests


bot = Bot()

# linux执行登陆请调用下面的这句
bot = Bot(console_qr=2,cache_path="botoo.pkl")


def send_news():
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.groups().search(u'人资部的小可爱')[0]
        my_friend.send(u"hhhh,这个太有趣了")
        


if __name__ == "__main__":
    send_news()
