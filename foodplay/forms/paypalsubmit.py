import paypalrestsdk
from django.forms import model_to_dict

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
    def handler(self, paymentinfo):
        item = paymentinfo.item
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
        return True


    @staticmethod
    def convertpaymentinfo(payment_info, item_info):
        pinfo = dict()
        try:
            pinfo['intent'] = ("sale")
            pinfo['payer'] = {}
            pinfo['payer']['payment_method'] = 'credit_card'
            pinfo['payer']['funding_instruments'] = [model_to_dict(payment_info)]

            pinfo['transactions'] = [{"item_list": item_info}]
        except Exception as E:
            raise E
        return pinfo

    @staticmethod
    def convert_items(item):
        items = model_to_dict(item)
        items['quantity'] = 1
        items['currency'] = "USD"
        item_info = dict()
        item_info['items'] = [items]
        item_info['amount'] = {'total': 1, 'currency': "USD"}
        item_info["description"] = items["description"]
        return item_info
