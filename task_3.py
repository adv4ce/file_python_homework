f_1 = open('files/1.txt', 'r', encoding='utf-8').readlines()
f_2 = open('files/2.txt', 'r', encoding='utf-8').readlines()
f_3 = open('files/3.txt', 'r', encoding='utf-8').readlines()

f_1 = [i.rstrip() for i in f_1]
f_2 = [i.rstrip() for i in f_2]
f_3 = [i.rstrip() for i in f_3]

sorted_len_list = sorted([['1.txt', f_1], ['2.txt', f_2], ['3.txt', f_3]], key=lambda x: len(x[1]))

print(f'{sorted_len_list[0][0]}\n'
      f'{len(sorted_len_list[0][1])}')
for i in range(len(sorted_len_list[0][1])):
  print(sorted_len_list[0][1][i])

print('\n')

print(f'{sorted_len_list[1][0]}\n'
      f'{len(sorted_len_list[1][1])}')
for i in range(len(sorted_len_list[1][1])):
  print(sorted_len_list[1][1][i])

print('\n')

print(f'{sorted_len_list[2][0]}\n'
      f'{len(sorted_len_list[2][1])}')
for i in range(len(sorted_len_list[2][1])):
  print(sorted_len_list[2][1][i])