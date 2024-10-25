from django.db import models


class CuisineType(models.TextChoices):
    FRENCH = "FR", "French"
    CHINESE = "CN", "Chinese"
    ITALIAN = "IT", "Italian"
    BALKAN = "BK", "Balkan"
    OTHER = "OT", "Other"
