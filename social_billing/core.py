# -*- coding: utf8 -*-


class BillingCore(object):

    @staticmethod
    def get_payment(social):
        from social_billing.mm.engine.payment import MMPayment
        from social_billing.vk.engine.payment import VKPayment
        from social_billing.od.engine.payment import ODPayment

        return {'vk': VKPayment, 'mm': MMPayment, 'od': ODPayment}[social]

    @classmethod
    def init(cls, social_name, default_item, *args):
        cls.default_item = default_item
        cls.payment = cls.get_payment(social_name)(*args)