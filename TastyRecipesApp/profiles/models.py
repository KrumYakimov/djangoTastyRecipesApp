from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from TastyRecipesApp.recipes.choices import CuisineType


class Profile(models.Model):
    MAX_NICKNAME_LENGTH = 20
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    nickname = models.CharField(
        max_length=MAX_NICKNAME_LENGTH,
        validators=[
            MinLengthValidator(
                2,
                message="Name must start with a capital letter!"
            ),
        ],
        null=False,
        blank=False,
        unique=True
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            RegexValidator(
                '^[A-Z]',
                message="Name must start with a capital letter!"
            ),
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            RegexValidator(
                '^[A-Z]',
                message="Name must start with a capital letter!"
            ),
        ],
        null=False,
        blank=False,
    )

    chef = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    bio = models.TextField(
        null=True,
        blank=True,
    )







