from django.views.generic import TemplateView


class Cheese(TemplateView):
    template_name = 'cheese-cake.html'

    def get_context_data(self, **kwargs):
        return {}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
