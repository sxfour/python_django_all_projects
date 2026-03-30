from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q

from .models import Recipe
from .serializers import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        tags_param = request.query_params.get('tags')
        if tags_param:
            # Проверяем, есть ли запятые — если есть, считаем, что это список тегов
            if ',' in tags_param:
                # Разделяем на теги
                tags_list = [tag.strip() for tag in tags_param.split(',')]
                filters = Q(dishTypes__overlap=tags_list) | Q(diets__overlap=tags_list)
            else:
                # Нет запятых — считаем, что это часть названия
                filters = Q(title__icontains=tags_param)

            queryset = queryset.filter(filters)

        # Ограничение по количеству
        numbers = request.query_params.get('numbers')
        if numbers:
            try:
                numbers = int(numbers)
                queryset = queryset[:numbers]
            except ValueError:
                return Response({"error": "Invalid 'numbers' parameter."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(queryset, many=True)
        return Response({"recipes": serializer.data})

    def create(self, request, *args, **kwargs):
        # Ожидаем JSON в формате {"recipes": [...]}
        recipes_data = request.data.get('recipes')

        if not isinstance(recipes_data, list):
            return Response({"error": "Invalid data format. Expected {'recipes': [...]}"},
                            status=status.HTTP_400_BAD_REQUEST)

        created_recipes = []
        for recipe_data in recipes_data:
            serializer = self.get_serializer(data=recipe_data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            created_recipes.append(serializer.data)

        # Возвращаем созданные рецепты в том же формате
        return Response({"recipes": created_recipes}, status=status.HTTP_201_CREATED)

    # Переопределяем retrieve, update, partial_update, destroy для работы с одним рецептом
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # Возвращаем один рецепт в списке для соответствия формату
        return Response({"recipes": [serializer.data]})

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # Ожидаем JSON в формате {"recipes": [{...}]}
        recipes_data = request.data.get('recipes')

        if not isinstance(recipes_data, list) or len(recipes_data) != 1:
            return Response({"error": "Invalid data format. Expected {'recipes': [{...}]}"},
                            status=status.HTTP_400_BAD_REQUEST)

        recipe_data = recipes_data[0]
        serializer = self.get_serializer(instance, data=recipe_data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # Возвращаем обновленный рецепт в списке
        return Response({"recipes": [serializer.data]})

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
