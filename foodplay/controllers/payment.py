from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView

from foodplay.forms.paymentform import PaypalForm


class Pay(TemplateView):
    template_name = 'pay.html'

    def get(self, request):
        pass
        temp = get_template("pay.html")
        paypalform = PaypalForm()
        html = temp.render(Context({'form': paypalform}))
        return HttpResponse(temp)


        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
