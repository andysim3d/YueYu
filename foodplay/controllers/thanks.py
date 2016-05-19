from django.views.generic import TemplateView


class Thanks(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        return {}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
