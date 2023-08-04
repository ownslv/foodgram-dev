from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.db import models
from users.models import User


class Recipes(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='autor_repices',
        verbose_name='Автор',
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Название рецепта',
    )
    image = models.ImageField(
        upload_to='media/',
        verbose_name='Картинка рецепта',
    )
    text = models.TextField(
        verbose_name='Описание рецепта',
    )
    ingredients = models.ManyToManyField(
        'Ingredients',
        through='IngredientAmount',
        related_name='ingredients_recipe',
        verbose_name='Ингредиенты',
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Тэги',
    )
    cooking_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                1, 'Время приготовления не может быть меньше 1 минуты!'
            )],
        default=1,
        verbose_name='Время приготовления',
        help_text='Время приготовления в минутах',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания рецепта',
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )
    measurement_unit = models.CharField(
        max_length=10,
        verbose_name='Единицы измерения',
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredients,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        verbose_name='Рецепт',
    )
    amount = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(
                1, 'Количество ингредиентов не может быть меньше 1!'
            )],
        default=1,
        verbose_name='Количество',
    )

    class Meta:
        verbose_name = 'Количество ингредиентов'
        verbose_name_plural = 'Количество ингредиентов'

    def __str__(self):
        return f'{self.ingredient} {self.recipe}'


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Избранный автор',
    )

    class Meta:
        verbose_name = 'Избранный автор'
        verbose_name_plural = 'Избранные авторы'

    def __str__(self):
        return f'{self.user} {self.author}'


class FavoriteRecipe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_list',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='in_favorite',
        verbose_name='Избранный рецепт',
    )

    class Meta:
        verbose_name = 'Список избранного'
        verbose_name_plural = 'Списки избранного'

    def __str__(self):
        return f'{self.user} {self.recipe}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipes,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт в списке покупок',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'

    def __str__(self):
        return f'{self.user} {self.recipe}'


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
        verbose_name='Название',
    )
    color = ColorField(
        format='hex',
        default='#FF0000',
        verbose_name='Цветовой HEX-код',
    )
    slug = models.SlugField(
        unique=True,
        max_length=20,
        verbose_name='Slug',
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
