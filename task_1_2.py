def file_work(file):
  file = [i.rstrip() for i in file]

  for i in range(len(file)):
    if ' | ' in file[i]:
      file[i] = file[i].split(' | ')

  file.append('') #Пришлось добавить, потому что код не видел Фахитос, из-за того, что в конце строки нет ''

  recipes = []
  list = []
  for i in range(len(file)):
    if file[i] != '':
      list.append(file[i])
    else:
      recipes.append(list)
      list = []

  return recipes


def dictionary_work(recipes):
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

  return cook_book

def get_shop_list_by_dishes(dishes, person_count):
  result_ingredients = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingredient_name'] not in result_ingredients:
        result_ingredients[ingredient['ingredient_name']] = {'measure' : ingredient['measure'], 'quantity' : ingredient['quantity'] * person_count}
      else:
        result_ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count

  return result_ingredients

if __name__ == "__main__":
  file = open('files/recipes.txt', 'r', encoding='utf-8').readlines()
  recipes = file_work(file)
  cook_book = dictionary_work(recipes)
  
  print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)) #Вариант из задания
  print('\n')
  print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)) #Вариант с повторяющимися продуктами (Помидор)