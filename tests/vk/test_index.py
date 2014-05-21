# -*- coding: utf-8 -*-
import json
from urllib import urlencode
from tornado.testing import AsyncHTTPTestCase
from social_billing.vk.engine.payment import GET_ITEM
from social_billing.web.app import application
from tests.vk.vk_base_test import VKBaseTest
from social_billing.vk.engine.errors import InvalidCountError, UnknownItemError, \
    ItemFormatError
from social_billing.vk.engine.handler.vk_order import CHARGEABLE


class IndexTest(AsyncHTTPTestCase, VKBaseTest):

    def get_app(self, *args, **kwargs):
        return application

    def post(self, args):
        self.http_client.fetch(self.get_url('/'), self.stop, method='POST',
                               body=urlencode(args))
        response = self.wait()
        return json.loads(response.body)

    def test_post_get_info(self):
        self.eq(
            self.post(self.info_args(4)),
            self.payment.info('gems', 20)
        )

    def test_post_get_info_test(self):
        self.eq(self.post(self.info_args(4, ntype=GET_ITEM + '_test')),
                self.payment.info('gems', 20))

    def test_post_order(self):
        self.eq(self.post(self.order_args()),
                self.payment.order('1', 'uid', 'gems', 20, CHARGEABLE))

    def test_errors(self):
        self.eq(
            self.post(self.info_args(item='gems_no')),
            ItemFormatError().response()
        )
        self.eq(
            self.post(self.info_args(item='55')),
            UnknownItemError().response()
        )
