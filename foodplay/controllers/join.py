from django.views.generic import TemplateView


class Join(TemplateView):
    template_name = 'join.html'

    def get_context_data(self, **kwargs):
        return {}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
