from django.template.loader import get_template
from django.views.generic import TemplateView

from foodplay.forms.paymentform import PaypalForm


class Pay(TemplateView):
    template_name = 'popcake.html'

    def get(self, request):
        pass
        temp = get_template("pay.html")
        paypalform = PaypalForm()
        temp.render(request, {'form': paypalform})
        return temp


        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
