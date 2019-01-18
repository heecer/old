#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
info['stu1101'] = '武藤兰'
print(info)
info['stu1104'] = '武藤兰1'
print(info)
del info['stu1104']
print(info)
info.popitem()
print(info)

for i in info:
    print(i,info[i])
for k,v in info.items():
    print(k,v)

'''
av_catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
av_catalog['大陆']['1024'][1]='可以网络爬取'
print(av_catalog)
print(av_catalog.keys(),av_catalog.values(),end='\n')
av_catalog.setdefault('大陆',{'www':[1,2]})
print(av_catalog)
B = {1:2,3:4}
av_catalog.update(B)
print(av_catalog)
print(av_catalog.items())#转成列表
A=dict.fromkeys([1,2,3,4])
print(A)
'''