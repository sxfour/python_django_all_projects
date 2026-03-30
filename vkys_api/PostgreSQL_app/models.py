from django.db import models
from django.contrib.postgres.fields import ArrayField


class ExtendedIngredient(models.Model):
    id = models.IntegerField(primary_key=True)
    aisle = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    consistency = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nameClean = models.CharField(max_length=255, blank=True, null=True)
    original = models.TextField(blank=True, null=True)
    originalName = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unit = models.CharField(max_length=50, blank=True, null=True)
    meta = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    # Measures (вложенные в JSON, но в модели можно сохранить как отдельные поля или JSONField)
    # Для простоты, будем сохранять их в одном JSONField
    measures = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name or f"Ingredient ID: {self.id}"


class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    imageType = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255)
    readyInMinutes = models.IntegerField(blank=True, null=True)
    servings = models.IntegerField(blank=True, null=True)
    sourceUrl = models.URLField(max_length=500, blank=True, null=True)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    glutenFree = models.BooleanField(default=False)
    dairyFree = models.BooleanField(default=False)
    veryHealthy = models.BooleanField(default=False)
    cheap = models.BooleanField(default=False)
    veryPopular = models.BooleanField(default=False)
    sustainable = models.BooleanField(default=False)
    lowFodmap = models.BooleanField(default=False)
    weightWatcherSmartPoints = models.IntegerField(blank=True, null=True)
    gaps = models.CharField(max_length=50, blank=True, null=True)
    preparationMinutes = models.IntegerField(blank=True, null=True)
    cookingMinutes = models.IntegerField(blank=True, null=True)
    aggregateLikes = models.IntegerField(blank=True, null=True)
    healthScore = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    creditsText = models.CharField(max_length=255, blank=True, null=True)
    sourceName = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    # Связь с ингредиентами
    extendedIngredients = models.ManyToManyField(ExtendedIngredient, related_name='recipes')

    # Списки строк
    cuisines = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    dishTypes = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    diets = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    def __str__(self):
        return self.title
