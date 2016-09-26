#!/usr/bin/env python
# encoding: utf-8


"""
@version: 0.01
@author: xdxd
@license: Apache Licence 
@contact: 646901834@qq.com
@site: http://www.xdxd.love
@software: PyCharm
@file: get.py
@time: 16/9/26 上午9:06
"""

import requests
from bs4 import BeautifulSoup
from sender import Mail
import time



# config

newesttitle = 'test'
smtp_user = '11111@qq.com'
smtp_pass = '22222'
sendto = '333333@qq.com'




def send_mail(smtp_user, smtp_pass, subject='test', body='test', sendto=sendto, smtp_server='smtp.qq.com',
              smtp_port=465):
    mail = Mail(smtp_server, port=smtp_port, username=smtp_user, password=smtp_pass, use_tls=False, use_ssl=True,
                debug_level=None)
    mail.send_message(subject, fromaddr=smtp_user, to=sendto, body=body)





def getnewesttitle():
    url = 'http://www.xxxxxx.net/forum.php?mod=forumdisplay&fid=33&filter=author&orderby=dateline'
    headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text)
    newest = soup.find('span',class_='by')
    return newest.parent.text




def filter(title):
    keywords = [u'快递',u'种球',u'生石花',u'PP',u'屁屁',u'玉露',u'12',u'十二',u'树莓',u'月季',u'浙江',u'上海',u'江苏']
    for keyword in keywords:
        if keyword in title.strip():
            return True
        else:
            pass
    return False






if __name__ == '__main__':
    # getnewtitle()
    # send_mail(smtp_user, smtp_pass, 'yyyy', 'uuu')
    newesttitle = getnewesttitle()
    while True:
        try:
            thenexttitle = getnewesttitle()
            print('monitoring')
            print newesttitle.encode('utf-8')
            print thenexttitle.encode('utf-8')
            if thenexttitle != newesttitle:
                newesttitle = thenexttitle

                send_mail(smtp_user, smtp_pass, thenexttitle.strip(), thenexttitle.strip())
            else:
                pass
        except RuntimeError:
            print(RuntimeError)
        time.sleep(1)



