from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'app/home.html'

home = Home.as_view()

class Test(TemplateView):
    template_name = 'app/test.html'

test = Test.as_view()