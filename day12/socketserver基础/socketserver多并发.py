#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):


        while True:

            try:
                self.data = self.request.recv(1024).strip()
                print("{}:{} wrote:".format(self.client_address[0], self.client_address[1]))
                print(self.data.decode())
                msg = input('>>:').strip().encode('utf-8')
                self.request.send(msg)
                # print("{} wrote:".format(self.client_address[0]))
                # if not self.data:
                #     print('客户端断开')
                #     break
            except ConnectionResetError as e:
                print('客户端断开')
                break
        self.request.close()
if __name__ == "__main__":
    HOST, PORT = "localhost", 7000
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)    #Threading,多线程处理
    # server = socketserver.ForkingTCPServer((HOST, PORT), MyTCPHandler)    #Forking,多进程处理
    server.serve_forever()