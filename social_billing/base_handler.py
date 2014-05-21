# -*- coding: utf8 -*-
from social_billing.vk.engine.errors import UnknownItemError, InvalidCountError


class BaseHandler(object):
    def __init__(self, goods):
        self.goods = goods

    def get_good(self, name):
        item = self.goods.get(name)
        if item is None:
            raise UnknownItemError()
        return item

    def get_item(self, good, count):
        item = good['prices'].get(count)

        if item is None:
            raise InvalidCountError()
        else:
            return item

    def price(self, good, count):
        return self.get_item(good, count)['price']

    def title(self, name, count):
        return self.get_item(self.get_good(name), count)['title']

    def image(self, item):
        return item.get('image', '')