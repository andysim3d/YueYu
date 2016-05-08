from django.views.generic import TemplateView


class Flower(TemplateView):
    template_name = 'flowers-cookies.html'

    def get_context_data(self, **kwargs):
        return {}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
