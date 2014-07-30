[![Build Status](https://travis-ci.org/dsociative/social_billing.svg?branch=master)](https://travis-ci.org/dsociative/social_billing)

social_billing
--------------
Web server that handles payments from social networks

Support:
  - [vk.com](http://vk.com/developers.php?oid=-1&p=Payments_API) 
  - [my.mail.ru](http://api.mail.ru/docs/guides/billing/) 
  - [odnoklassniki.ru](http://api.mail.ru/docs/guides/billing/)  

Uses:
  - MongoDB
  - Tornado

Goods Example:
```python
{
        u'gems': {
            1: {
                u'count': 1,
                u'price': 1,
                u'title': u'1 алмаз',
                u'image': u'image_url'
            },
            2: {
                u'count': 3,
                u'price': 1,
                u'title': u'3 алмаза',
                u'image': u'image_url'
            },
            3: {
                u'count': 10,
                u'price': 1,
                u'title': u'10 алмазов',
                u'image': u'image_url'
            },
            4: {
                u'count': 20,
                u'price': 2,
                u'title': u'20 алмазов',
                u'image': u'image_url'
            }
        },
        'vip': {
            10: {
                u'count': 23,
                u'price': 24,
                u'title': u'VIP на 10 дней',
                u'image': u'someimage'
            }
        }
    }
```
