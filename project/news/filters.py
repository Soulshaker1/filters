from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, PostCategory


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    type = ModelMultipleChoiceFilter(
        field_name='',
        queryset=Post.objects.all(),  # название класса в models.py
        label='категория',
    )


class Meta:
    # В Meta классе мы должны указать Django модель,
    # в которой будем фильтровать записи.
    model = Post
    # В fields мы описываем по каким полям модели
    # будет производиться фильтрация.
    fields = {
        # поиск по названию
        'title': ['icontains'],
        # количество товаров должно быть больше или равно
        'dateCreation': ['day'],
        'postCategory': [
            'lt',  # цена должна быть меньше или равна указанной
            'gt',  # цена должна быть больше или равна указанной
        ],
    }
