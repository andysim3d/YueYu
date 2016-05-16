import paypalrestsdk

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
        payment = paypalrestsdk.Payment(
            paymentinfo,
            api=api_info,
        )

        if not payment.create():
            raise ValueError("payment create error")
        if not payment.execute():
            raise ValueError(payment.error)

    @staticmethod
    def convertpaymentinfo(payment):
        pinfo = dict()
        try:
            pinfo['intent'] = payment.get("intent", "sale")
            pinfo['payer']['payment_method'] = payment.get("payment_method", "paypal")


        except Exception as E:
            raise E
