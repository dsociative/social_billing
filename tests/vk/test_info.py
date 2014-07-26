# -*- coding: utf-8 -*-
from tests.vk.vk_base_test import VKBaseTest
from social_billing.vk.engine.errors import InvalidCountError, UnknownItemError,\
    ItemFormatError
from social_billing.vk.engine.handler.info import Info


class InfoTest(VKBaseTest):

    def setUp(self):
        super(InfoTest, self).setUp()
        self.info = Info(self.items)
        self.gems = self.info.get_good('gems')

    def test_price(self):
        self.eq(self.info.price(self.gems, 3), 1)
        self.eq(self.info.price(self.gems, 4), 2)

    def test_title(self):
        self.eq(self.info.title('gems', 4), u'20 алмазов')
        self.eq(self.info.title('gems', 3), u'10 алмазов')
        self.eq(self.info.title('gems', 1), u'1 алмаз')
        self.eq(self.info.title('gems', 2), u'3 алмаза')

    def test_info(self):
        self.eq(
            self.info('gems', 3),
            self.info.response(
                {
                    'title': self.info.title('gems', 3),
                    'price': 1,
                    'photo_url': self.items['gems'][3]['image']
                }
            )
        )

    def test_unknown_item(self):
        self.raises(UnknownItemError, self.info.get_good, 'item')

    def test_invalid_count(self):
        self.raises(InvalidCountError, self.info.price, self.gems, 11)
