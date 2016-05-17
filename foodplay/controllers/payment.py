from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import TemplateView

from foodplay.forms.paymentform import PaypalForm


class Pay(TemplateView):
    template_name = 'pay.html'

    def get(self, request):
        pass
        temp = get_template("pay.html")
        paypalform = PaypalForm()
        html = RequestContext(request, {'form': paypalform})
        return render_to_response("pay.html", html)


        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
