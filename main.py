f = open('recipes.txt', 'r', encoding='utf-8').readlines()
f = [i.rstrip() for i in f]

for i in range(len(f)):
  if ' | ' in f[i]:
    f[i] = f[i].split(' | ')

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
  cook_book[recipes[i][0]] = [{'ingredient_name': '', 'quantity': 0, 'measure': ''} for i in range(int(recipes[i][1]))]

print(recipes)


print(cook_book)