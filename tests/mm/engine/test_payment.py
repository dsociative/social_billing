# -*- coding: utf8 -*-
from tests.mm.mm_base_test import MMBaseTest


class MMPaymentTest(MMBaseTest):

    ok = {'status': 1}
    signature_error = {'status': 0, 'error_code': 700}
    price_error = {'status': 0, 'error_code': 703}

    def test_get_name_count(self):
        self.eq(self.payment.get_name_count('1'), (1, 'gems', 1))
        self.eq(self.payment.get_name_count('2'), (2, 'gems', 3))
        self.eq(self.payment.get_name_count('3'), (3, 'gems', 10))
        self.eq(self.payment.get_name_count('4'), (4, 'gems', 20))

    def test_buy(self):
        for _ in xrange(10):
            self.eq(self.payment.request(self.signed_args()), self.ok)
            self.eq(self.engine.log, [(104, 'gems', 10)])

        self.payment.request((self.signed_args(transaction_id=1)))
        self.eq(
            self.engine.log,
            [(104, 'gems', 10), (104, 'gems', 10)]
        )

    def test_buy_something_else(self):
        self.payment.request(
            (self.signed_args(service_id=10, transaction_id=10,
                              mailiki_price=24))
        )
        self.eq(
            self.engine.log,
            [(104, 'vip', 23)]
        )

    def test_signature_error(self):
        args = self.args()
        args['sig'] = 'errorsignature'
        self.eq(self.payment.request(args), self.signature_error)

    def test_price_error(self):
        self.eq(self.payment.request(self.signed_args(mailiki_price=4)),
                self.price_error)
