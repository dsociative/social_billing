# -*- coding: utf-8 -*-
from social_billing.base_payment import BasePayment

from social_billing.vk.engine.errors import ItemFormatError, UnknownItemError,\
    InvalidCountError, CallbackError, SignatureError
from social_billing.vk.engine.handler.info import Info
from social_billing.vk.engine.handler.vk_order import VKOrder
from social_billing.vk.engine.signature import Signature


ORDER = 'order_status_change'
GET_ITEM = 'get_item'


class VKPayment(BasePayment):

    def __init__(self, name, goods, secret, callback):
        self.signature = Signature(secret)
        self.info = Info(goods)
        self.order = VKOrder(name, callback)
        super(VKPayment, self).__init__(goods)

    def request(self, args):
        notification_type = args.get('notification_type')
        try:
            if not self.signature.check(args, args.pop('sig')):
                raise SignatureError()

            name, count = self.get_name_count(args['item'])

            if notification_type.startswith(GET_ITEM):
                return self.info(name, count)
            if notification_type.startswith(ORDER):
                return self.order(args['order_id'], args['receiver_id'],
                                  name, count, args['status'])
        except (ItemFormatError, UnknownItemError, InvalidCountError,
                CallbackError, SignatureError) as error:
            return error.response()
