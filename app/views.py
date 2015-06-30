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
        context['tags_amount'] = len(tags_ids)
        rand = random.sample(tags_ids, 5)
        context['rand'] = rand

        # even one id in array
        overlap = Post.objects.filter(tags__overlap=rand)
        context['overlap'] = overlap
        context['overlap_amount'] = len(overlap)

        # values passed is subset of the data
        contains = Post.objects.filter(tags__contains=rand)
        context['contains'] = contains
        context['contains_amount'] = len(contains)

        # data is subset of the values passed
        contained_by = Post.objects.filter(tags__contained_by=rand)
        context['contained_by'] = contained_by
        context['contained_by_amount'] = len(contained_by)

        return context

home = Home.as_view()

class Test(TemplateView):
    template_name = 'app/test.html'

test = Test.as_view()