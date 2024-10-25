from django.shortcuts import render
from django.views.generic import TemplateView


class CatalogueView(TemplateView):
    template_name = 'recipes/catalogue.html'


