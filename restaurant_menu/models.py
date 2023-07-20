from django.db import models
from django.contrib.auth.models import User

Meal_Type = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main dishes", "Main Dishes"),
)

Status = (
    (0, "Unavailable"),
    (1, "Available")
)


class item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=Meal_Type)
    authors = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
