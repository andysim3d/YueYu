from django.views.generic import TemplateView
from foodplay.models import Blog
from django.template.loader import get_template
from django.forms.models import model_to_dict
from django.http import  HttpResponse
from django.template import Context



class Facebook(TemplateView):
    template_name = 'facebook.html'

    def get_context_data(self, **kwargs):
        return {}
