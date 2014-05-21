# -*- coding: utf8 -*-
from social_billing.vk.engine.errors import ItemFormatError, UnknownItemError


class BasePayment(object):
    def __init__(self, goods):
        self.mapper = dict(self.make_goods_mapper(goods))

    def make_goods_mapper(self, goods):
        for good, items in goods.iteritems():
            for count, item in items['prices'].iteritems():
                yield item['id'], (good, count)

    def get_name_count(self, item_id):
        if type(item_id) is not int and not item_id.isdigit():
            raise ItemFormatError

        name_count = self.mapper.get(int(item_id))
        if name_count is None:
            raise UnknownItemError

        return name_count