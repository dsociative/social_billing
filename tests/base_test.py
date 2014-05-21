# -*- coding: utf8 -*-
from ztest import ZTest


class Engine(object):
    """
    Mock object for testing callback
    """

    def __init__(self):
        self.log = []

    def callback(self, receiver_id, name, count):
        self.log.append((receiver_id, name, count))
        return True


class BaseTest(ZTest):
    items = {
        u'gems': {
            u'prices': {
                1: {
                    u'id': 1,
                    u'price': 1,
                    u'title': u'1 алмаз'
                },
                3: {
                    u'id': 2,
                    u'price': 1,
                    u'title': u'3 алмаза'
                },
                10: {
                    u'id': 3,
                    u'price': 1,
                    u'title': u'10 алмазов'
                },
                20: {
                    u'id': 4,
                    u'price': 2,
                    u'title': u'20 алмазов'
                }
            },
            u'image': u'image_url'
        },
        'vip': {
            'prices': {
                23: {
                    u'id': 10,
                    u'price': 24,
                    u'title': u'VIP на 10 дней'
                }
            },
            u'image': u'someimage'
        }
    }

    engine = Engine()

    def sign(self, args):
        args['sig'] = self.payment.signature.md5(args)
        return args

    def setUp(self):
        super(BaseTest, self).setUp()
        self.engine.log = []
