values = input('Please, write numbers separated by commas: ')
list_of_values = values.split(',')
tuple_of_values = tuple(list_of_values)
print(f'''
List of the numbers written: {list_of_values}
Tuple of the numbers written: {tuple_of_values}
''')
