from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from TastyRecipesApp.recipes.mixins import RecipeFormPlaceholderMixin, RecipeFormHelpTextMixin
from TastyRecipesApp.recipes.models import Recipe
from TastyRecipesApp.utils.mixins import ReadOnlyFormMixin
from TastyRecipesApp.utils.profile_helpers import get_profile


class CatalogueView(ListView):
    model = Recipe
    template_name = 'recipes/catalogue.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_exists'] = True
        return context


class RecipeCreateView(RecipeFormPlaceholderMixin, RecipeFormHelpTextMixin, CreateView):
    model = Recipe
    fields = ["title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url"]
    template_name = "recipes/create-recipe.html"
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        profile = get_profile()
        form.instance.author = profile
        return super().form_valid(form)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/details-recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.object
        context['ingredients_list'] = recipe.ingredients.split(', ')
        return context


class RecipeEditView(RecipeFormPlaceholderMixin, RecipeFormHelpTextMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit-recipe.html"
    fields = ["title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url"]
    success_url = reverse_lazy('catalogue')


class RecipeDeleteView(RecipeFormHelpTextMixin, ReadOnlyFormMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete-recipe.html"
    form_class = modelform_factory(
        Recipe,
        fields=(
            "title", "cuisine_type", "ingredients", "instructions", "cooking_time", "image_url"
        )
    )
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


