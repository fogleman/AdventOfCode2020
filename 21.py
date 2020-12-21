from collections import defaultdict
import fileinput
import re

foods = []
allergen_foods = defaultdict(list)
for line in fileinput.input():
    tokens = re.findall(r'\w+', line)
    i = tokens.index('contains')
    ingredients = set(tokens[:i])
    allergens = set(tokens[i+1:])
    foods.append((ingredients, allergens))
    for allergen in allergens:
        allergen_foods[allergen].append(ingredients)

candidates = {}
for allergen, ingredients in allergen_foods.items():
    candidates[allergen] = set.intersection(*ingredients)

ingredient_allergen = {}
while True:
    for allergen, ingredients in candidates.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            ingredient_allergen[ingredient] = allergen
            for ingredients in candidates.values():
                ingredients.discard(ingredient)
            break
    else:
        break

print(sum(ingredient not in ingredient_allergen
    for ingredients, _ in foods for ingredient in ingredients))

print(','.join(x[0] for x in
    sorted(ingredient_allergen.items(), key=lambda x: x[1])))
