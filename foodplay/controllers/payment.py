from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import TemplateView

from foodplay.forms.paymentform import PaypalForm


class Pay(TemplateView):
    template_name = 'pay.html'

    @ensure_csrf_cookie
    def get(self, request):
        pass
        c = {}
        c.update(csrf(request))

        temp = get_template("pay.html")
        paypalform = PaypalForm()
        html = RequestContext(request, {'form': paypalform}, c)
        return render_to_response("pay.html", html)


        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
