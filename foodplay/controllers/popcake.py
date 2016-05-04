from django.views.generic import TemplateView


class Popcake(TemplateView):
    template_name = 'popcake.html'

    def get_context_data(self, **kwargs):
        return {}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
