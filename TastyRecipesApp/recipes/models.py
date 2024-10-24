from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from TastyRecipesApp.recipes.choices import CuisineType


class Recipe(models.Model):
    MAX_TITLE_LENGTH = 100
    MAX_CUISINE_TYPE_LENGTH = 7

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[
            MinLengthValidator(10)
        ],
        unique=True,
        error_messages={
            'unique': "We already have a recipe with the same title!"
        },
        null=False,
        blank=False,
    )

    cuisine_type = models.CharField(
        max_length=MAX_CUISINE_TYPE_LENGTH,
        choices=CuisineType.choices,
        null=False,
        blank=False,
    )

    ingredients = models.TextField(
        null=False,
        blank=False,
        help_text="Provide the cooking time in minutes."
    )

    instructions = models.TextField(
        null=False,
        blank=False,
    )

    cooking_time = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1)
        ],
        help_text="Provide the cooking time in minutes."
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        to="profiles.Profile",
        on_delete=models.CASCADE,
        related_name="authors",
        editable=False
    )
