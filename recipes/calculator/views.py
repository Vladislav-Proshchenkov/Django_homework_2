from lib2to3.fixes.fix_input import context

from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def dishs_view(request):
    context = {
        'data': DATA.keys()
    }
    return render(request, 'demo.html', context)

def dish_view(request, name_dish):
    servings = int(request.GET.get('servings', 1))
    recipe = {}
    for key, value in DATA[name_dish].items():
        recipe[key] = value
    for key, value in recipe.items():
        recipe[key] = round(value * servings, 2)
    context = {
        "name_dish": name_dish,
        "recipe": recipe,
        }
    return render(request, 'index.html', context)