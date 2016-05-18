from django.forms import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import TemplateView

from foodplay.forms.paymentform import PaypalForm
from foodplay.forms.paypalsubmit import paypal
from foodplay.models import Products


class Pay(TemplateView):
    template_name = 'pay.html'

    def get(self, request):
        paypalform = PaypalForm()

        html = RequestContext(request, {'form': paypalform})
        return render_to_response("pay.html", html)


        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context

    def post(self, request):
        pro_id = request.GET.get('id', 1)
        prod = Products.objects.get(sku=pro_id)

        temp = get_template("pay.html")
        paypalform = PaypalForm(request.POST)
        html = RequestContext(request, {'form': paypalform})

        if paypalform.is_valid():
            model_instance = paypalform.save(commit=False)
            model_instance.item = prod
            model_instance.save()
            payinfo = model_to_dict(model_instance)
            try:
                d = paypal()

            except Exception as E:
                pass
            html = RequestContext(request, {'form': paypalform, "info": payinfo})

        return render_to_response("pay.html", html)
