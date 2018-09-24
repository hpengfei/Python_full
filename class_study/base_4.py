#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/24 11:52
# @Author  : hpengfei
# @File    : base_4.py
# @Software: PyCharm


class BaseRequest:

    def __init__(self):
        print('BaseRequest.init')


class RequestHandler(BaseRequest):

    def __init__(self):
        print('RequestHandler.init')
        BaseRequest.__init__(self)

    def server_forever(self):
        print('RequestHandler.server_forever')
        self.process_request()

    def process_request(self):
        print('RequestHandler.process_request')


class Minx:

    def process_request(self):
        print('Minx.process_request')


class Son(Minx, RequestHandler):

    pass


# obj = Son()
# obj.process_request()
# obj.server_forever()
# obj.server_forever()


obj_1 = RequestHandler()
obj_1.server_forever()