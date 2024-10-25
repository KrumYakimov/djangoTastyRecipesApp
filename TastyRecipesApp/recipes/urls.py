from django.urls import path, include

from TastyRecipesApp.recipes.views import CatalogueView, RecipeCreateView, RecipeDetailView, RecipeEditView, \
    RecipeDeleteView

urlpatterns = [
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path("create/", RecipeCreateView.as_view(), name="recipe-create"),
    path("<int:pk>", include([
        path("details/", RecipeDetailView.as_view(), name="recipe-details"),
        path("edit/", RecipeEditView.as_view(), name="recipe-edit"),
        path("delete/", RecipeDeleteView.as_view(), name="recipe-delete")
    ]))
]
