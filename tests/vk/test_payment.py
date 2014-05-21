# -*- coding: utf-8 -*-
from tests.vk.vk_base_test import VKBaseTest, GET_ITEM_TEST, ORDER_TEST
from social_billing.vk.engine.errors import ItemFormatError, CallbackError, \
    SignatureError, UnknownItemError
from social_billing.vk.engine.handler.vk_order import CHARGEABLE


class PaymentTest(VKBaseTest):

    def setUp(self):
        super(PaymentTest, self).setUp()

    def test_request_info(self):
        self.eq(self.payment.request(self.info_args()),
                self.payment.info('gems', 10))

    def test_request_info_test(self):
        self.eq(self.payment.request(self.info_args(ntype=GET_ITEM_TEST)),
                self.payment.info('gems', 10))

    def test_request_order(self):
        self.eq(self.payment.request(self.order_args()),
                self.payment.order(1, 'uid', 'gems', 10, CHARGEABLE))

    def test_request_order_test(self):
        self.eq(self.payment.request(self.order_args(ntype=ORDER_TEST)),
                self.payment.order(1, 'uid', 'gems', 10, CHARGEABLE))

    def test_request_error_order(self):
        self.eq(self.payment.request(self.order_args('gems10')),
                ItemFormatError().response())

    def test_request_error_wrong_id(self):
        self.eq(self.payment.request(self.order_args('342')),
                UnknownItemError().response())

    def test_request_error_callback(self):
        self.payment.order.callback = self.error_callback
        self.eq(self.payment.request(self.order_args('1')),
                CallbackError().response())

    def test_request_error_sig(self):
        args = self.order_args('gems_10')
        args['sig'] = 'error'
        self.eq(self.payment.request(args),
                SignatureError().response())
