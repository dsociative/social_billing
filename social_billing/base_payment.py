# -*- coding: utf8 -*-
from social_billing.vk.engine.errors import ItemFormatError, UnknownItemError


class BasePayment(object):
    def __init__(self, goods):
        self.mapper = dict(self.make_goods_mapper(goods))

    def make_goods_mapper(self, goods):
        for good, items in goods.iteritems():
            for item_id, item in items.iteritems():
                yield item_id, (good, item['count'])

    def get_name_count(self, item_id):
        if type(item_id) is not int and not item_id.isdigit():
            raise ItemFormatError

        item_id = int(item_id)
        name_count = self.mapper.get(item_id)
        if name_count is None:
            raise UnknownItemError

        name, count = name_count
        return item_id, name, count