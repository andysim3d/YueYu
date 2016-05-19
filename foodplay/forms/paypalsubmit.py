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
        self.Error = None

    # payment info is a dict, with detail informations

    # create payment, and execute
    def handler(self, paymentinfo):
        payment = paypalrestsdk.Payment(
            paymentinfo,
            api=api_info,
        )

        if not payment.create():
            self.Error = payment.error
            raise ValueError(payment.error)
        return True

    def getError(self):
        if self.Error is None:
            return "nothing"
        return self.Error


    @staticmethod
    def convertpaymentinfo(payment_info, item_info):
        pinfo = dict()
        try:
            card_info_raw = model_to_dict(payment_info)
            card_info = {
                'cvv2':card_info_raw['cvv2'],
                'expire_month' : card_info_raw['expire_month'],
                'expire_year' : card_info_raw['expire_year'],
                'last_name': card_info_raw['last_name'],
                'first_name': card_info_raw['first_name'],
                'number': card_info_raw['number'],
                'type': card_info_raw['type'],
            }
            pinfo['intent'] = ("sale")
            pinfo['payer'] = {}
            pinfo['payer']['payment_method'] = 'credit_card'
            pinfo['payer']['funding_instruments'] = [{"credit_card": card_info}]

            pinfo['transactions'] = [item_info]
        except Exception as E:
            raise E
        return pinfo

    @staticmethod
    def convert_items(item):
        items = model_to_dict(item)
        # items['quantity'] = 1
        # items['currency'] = "USD"
        item_info = dict()

        # item_info['items'] = [items]
        item_info['amount'] = {'total': int(items.get("price", 1)), 'currency': "USD"}
        item_info["description"] = items["description"]
        return item_info


#
d = {
        'intent': 'sale',
          'payer': {
              'funding_instruments': [{
                      'credit_card': {
                          'cvv2': 874,
                          'expire_month': 11,
                          'expire_year': 2018,
                          'first_name': 'Joe',
                          'last_name': 'Shopper',
                          'number': '4446283280247004',
                          'type': 'visa'}
        }],
              'payment_method': 'credit_card'},
 'transactions': [{
        'amount': {   'currency': 'USD',
                      'total': 12},
        'description': 'popcake decoration kit'}]}


# {
#   "intent": "sale",
#   "payer": {
#     "payment_method": "credit_card",
#     "funding_instruments": [{
#       "credit_card":{
#         "type": "visa",
#         "number": "4446283280247004",
#         "expire_month": "11",
#         "expire_year": "2018",
#         "cvv2": "874",
#         "first_name": "Joe",
#         "last_name": "Shopper" }}]},
#   "transactions": [{
#     "amount": {
#       "total": "12",
#       "currency": "USD" },
#     "description": "creating a direct payment with credit card" }]}