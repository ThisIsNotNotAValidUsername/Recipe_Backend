from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name
