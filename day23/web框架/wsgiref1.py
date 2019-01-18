#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
from wsgiref.simple_server import make_server
from Controller import account
def handle_index():
    f = open('Views/index.html','rb')
    data = f.read()
    f.close()
    return data
    # return ["<h1>Hello,Index</h1>".encode('utf-8'),]

def handle_date():
    return ["<h1>Hello,Date</h1>".encode('utf-8'),]

URL_DICT = {
    '/index': handle_index,
    '/date': handle_date,
}

def RunServer(environ, start_response):
    #environ 客户发来的所有数据
    #start_response 封装要返回客户端的数据，一般是响应头
    start_response('200 OK', [('Content-Type', 'text/html')])
    current_url = environ['PATH_INFO']
    func = None
    if current_url in URL_DICT:
        func = URL_DICT[current_url]
    if func:
        return func()
    else:
        return ['<h1>404!</h1>'.encode('utf-8'),]

    #返回类容
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]


if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()