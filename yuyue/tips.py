from django.views.generic import TemplateView


class Tips(TemplateView):
    template_name = 'tips.html'

    def get_context_data(self, **kwargs):
        return {"ele": ["static/img/home/3.pic.png",
                        "static/img/home/17.pic.png",
                        "static/img/home/19.pic.png",
                        "static/img/home/20.pic.png"]}
        # def get(self, request,*args, **kwargs):
        #     context = self.get_context_data(kwargs)
        #     return context
