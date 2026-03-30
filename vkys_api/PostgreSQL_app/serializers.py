from rest_framework import serializers
from .models import Recipe, ExtendedIngredient


class ExtendedIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedIngredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    extendedIngredients = ExtendedIngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('extendedIngredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            # Ищем существующий ингредиент по id или создаем новый
            ingredient, created = ExtendedIngredient.objects.get_or_create(
                id=ingredient_data.get('id'),
                defaults=ingredient_data
            )
            # Если ингредиент уже существует, обновляем его данные (опционально)
            if not created:
                for key, value in ingredient_data.items():
                    setattr(ingredient, key, value)
                ingredient.save()

            recipe.extendedIngredients.add(ingredient)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('extendedIngredients')
        instance = super().update(instance, validated_data)

        # Очищаем существующие ингредиенты и добавляем новые
        instance.extendedIngredients.clear()
        for ingredient_data in ingredients_data:
            ingredient, created = ExtendedIngredient.objects.get_or_create(
                id=ingredient_data.get('id'),
                defaults=ingredient_data
            )
            if not created:
                for key, value in ingredient_data.items():
                    setattr(ingredient, key, value)
                ingredient.save()
            instance.extendedIngredients.add(ingredient)

        return instance
