import paypalrestsdk
from django.forms import model_to_dict

from foodplay.models import Items

api_info = paypalrestsdk.Api(
    {
        'mode': 'sandbox',
        'client_id': 'AXeecVutojevH0oYa1hqFNJphCLOQ17dhli0NmfAgl5Ht1MGXcyNyiAFonumAs-WkizD1hgLest6AObF',
        'client_secret': 'EFEgqp_V-eIERryCPpdDo_veoMTn8btHkz2RybeuOUqNSpE5JKPPeOToqvmwRV_hRyqJ_bM0WgRcgfuN',
    }
)


class paypal(object):
    def __init__(self):
        self.api = api_info

    # payment info is a dict, with detail informations

    # create payment, and execute
    def handler(self, paymentinfo, item):
        item_info = paypal.convert_items(item)
        pinfo = paypal.convertpaymentinfo(paymentinfo, item_info)
        payment = paypalrestsdk.Payment(
            pinfo,
            api=api_info,
        )

        if not payment.create():
            raise ValueError("payment create error")
        if not payment.execute():
            raise ValueError(payment.error)

    @staticmethod
    def convertpaymentinfo(payment_info, item_info):
        pinfo = dict()
        try:
            pinfo['intent'] = ("sale")
            pinfo['payer'] = {}
            pinfo['payer']['payment_method'] = 'credit_card'
            pinfo['payer']['funding_instruments'] = payment_info

            pinfo['transactions'] = [{"item_list": item_info}]
        except Exception as E:
            raise E
        return pinfo

    @staticmethod
    def convert_items(item):
        item_id = item.get('id', 1)
        ite = Items.objects.get(sku=item_id)
        item_info = model_to_dict(ite)
        items_info = dict()
        items_info['item_list'] = {item_info}
        items_info['amount'] = {'total': item_info['price'], "currency": "USD"}
        items_info['description'] = item_info['description']
        return items_info
