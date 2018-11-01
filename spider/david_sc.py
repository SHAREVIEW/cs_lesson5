
# !/usr/bin/env python
#-*- coding:utf-8 -*-



import requests
from lxml import etree

#登陆地址 - 用于获取登陆session 及其他页面地址
loginUrl = 'https://eip.dediprog.com/dediprog/login.php'

#定义 headers - 模拟正常请求
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',}

# 登陆信息  -- 用户名 / 密码
data = {'txUserID': 'david.lee','txPwd': 'David123'}

#实例化session -- 用于后边面登陆
session = requests.session()
session.post(loginUrl, headers=headers, data=data)

# 左侧菜单地址： 'https://eip.dediprog.com/dediprog/leftmenu.php'
leftMenuUrl = 'https://eip.dediprog.com/dediprog/leftmenu.php'
laft_html = session.get(leftMenuUrl, headers=headers)

# 获取左侧菜单中 所有a 标签的 href 属性
etree_html = etree.HTML(laft_html.text)
allUriList = etree_html.xpath('//*[@id="menu"]/li/ul/li/a/@href')

#遍历地址 写入文件 -- 替换php后缀为html
indexHtml = 'https://eip.dediprog.com/dediprog/'
for uri in allUriList:
    if 'http' in uri :
        continue
    else:
        page_url = indexHtml + uri
        if '/' in uri:
            uri = str(uri).split('/')[1]
        if str(uri).split('.')[1] == 'php':
            filename = "{}.html".format(str(uri).split('.')[0])
        else:
            filename = uri

        print(page_url)
        page_html = session.get(page_url, headers=headers)
        if page_html.status_code == 404:
            continue
        with open(filename, 'wb') as page:
            page.write(page_html.content)
            #page.write(page_html.text)
