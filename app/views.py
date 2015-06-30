import random

from django.views.generic import TemplateView

from app.models import Tag
from app.models import Post

class Home(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        tags_ids = Tag.objects.all().values_list('id', flat=True)

        context['posts_amount'] = Post.objects.count()
        context['tags_amount'] = Tag.objects.count()
        rand = random.sample(tags_ids, 5)
        context['rand'] = rand
        context['overlap'] = Post.objects.filter(tags__overlap=rand)

        return context

home = Home.as_view()

class Test(TemplateView):
    template_name = 'app/test.html'

test = Test.as_view()