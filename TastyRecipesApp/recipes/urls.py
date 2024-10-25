from django.urls import path

from TastyRecipesApp.recipes.views import CatalogueView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
]
