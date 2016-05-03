from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.views.generic import TemplateView

from foodplay.models import Blog as BlogModel


class Blog(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        return {}
    # def get(self, request, *args, **kwargs):
    #     blog_id = request.GET.get("id", 1)
    #     blog = BlogModel.objects.get(id=blog_id)
    #     cont = Context({'blog': model_to_dict(blog)})
    #     temp = get_template('blog.html')
    #     return HttpResponse(temp.render(context=cont, request=request))
