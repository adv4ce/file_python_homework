import os

def open_file(files_name_list):
  result_str = []

  for file_name in files_name_list:
    file = open(f'files/task_2_files/{file_name}', 'r', encoding='utf-8').readlines()
    file = [i.rstrip() for i in file]
    
    result_str.append([file_name, file])

  return result_str

def sorted_file(str_list):
  return sorted(str_list, key=lambda x: len(x[1]))

def print_files(file):
  for file_list in file:
    file_name = file_list[0]
    print(f'{file_name}\n'
          f'{len(file_list[1])}')
    
    for str in file_list[1]:
      print(f'{str}')

if __name__ == "__main__":
  files_name = os.listdir('files/task_2_files')
  file = open_file(files_name)
  sorted_file = sorted_file(file)
  print_files(sorted_file)
  
