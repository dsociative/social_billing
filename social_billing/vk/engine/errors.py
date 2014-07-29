# -*- coding: utf-8 -*-


class BaseBillingException(Exception):

    critical = 1

    def response(self):
        return {'error': {'error_code': self.code, 'error_msg': self.name,
                          'critical': self.critical}}


class SignatureError(BaseBillingException):

    code = 10
    name = 'signature error'


class ItemFormatError(BaseBillingException):

    code = 11
    name = 'item format error'


class UnknownItemError(BaseBillingException):

    code = 20
    name = 'unknown item'


class InvalidCountError(BaseBillingException):

    code = 21
    name = 'invalid count'


class CallbackError(BaseBillingException):

    code = 1
    name = 'callback error'
