#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(123)
        u = self.get_argument('user')
        p = self.get_argument('pwd')
        e = self.get_argument('email')
        if u == 'python' and p =='123' and e == 'python@python':
            self.write('OK')
        else:
            self.write('失败')
        self.write("GET")
    def post(self):
        u = self.get_argument('user')
        p = self.get_argument('pwd')
        print('='*5+'POST'+'='*5)
        print(u,p)
        self.write('POST')

application = tornado.web.Application([
    (r"/index", MainHandler),])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()