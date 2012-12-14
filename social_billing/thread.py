# -*- coding: utf-8 -*-
from threading import Thread

from tornado.ioloop import IOLoop

from social_billing.app import application
from social_billing.handler.base_handler import BaseHandler


class BillingThread(Thread):

    def __init__(self, prices, secret, callback, port=8888):
        super(BillingThread, self).__init__()
        BaseHandler.init(prices, secret, callback)
        self.app = application
        self.port = port
        self.loop = IOLoop.instance()

    def run(self):
        self.app.listen(self.port)
        self.loop.start()

    def stop(self):
        self.loop.stop()


if __name__ == '__main__':
    def callback(self, *a):
        print a

    service = BillingThread({'gems': {10: 1, 20: 2}}, 'secretkey', callback)
    service.run()
    print 'started'
