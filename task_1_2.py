f = open('files/recipes.txt', 'r', encoding='utf-8').readlines()
f = [i.rstrip() for i in f]

for i in range(len(f)):
  if ' | ' in f[i]:
    f[i] = f[i].split(' | ')

f.append('') #Пришлось добавить, потому что код не видел Фахитос, из-за того, что в конце строки нет ''

recipes = []
list = []
for i in range(len(f)):
  if f[i] != '':
    list.append(f[i])
  else:
    recipes.append(list)
    list = []

cook_book = {}

for i in range(len(recipes)):
  cook_book[recipes[i][0]] = []

for recipe in recipes:
  dish = recipe[0]
  ingredient_list = []
  for i in range(2, len(recipe)):
    ingredient_name = recipe[i][0]
    quantity = int(recipe[i][1])
    measure = recipe[i][2]
  
    ingredient_list.append({'ingredient_name' : ingredient_name, 
                            'quantity' : quantity, 
                            'measure': measure})
  
  cook_book[dish] = ingredient_list

def get_shop_list_by_dishes(dishes, person_count):
  result_ingredients = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingredient_name'] not in result_ingredients:
        result_ingredients[ingredient['ingredient_name']] = {'measure' : ingredient['measure'], 'quantity' : ingredient['quantity'] * person_count}
      else:
        result_ingredients[ingredient_name]['quantity'] += ingredient['quantity'] * person_count

  return result_ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)) #Вариант из задания
print('\n')
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)) #Вариант с повторяющимися продуктами (Помидор)