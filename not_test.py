print('CU' in ['CU', 'M'])

print(float('3,43'.replace(',', '.')))

a = 'cu50.0t'
print(type(''.join([i for i in a if i.isdigit() or i in ',.'])))

str_num = ''.join([n for n in a if n.isalpha()])
print(str_num)

print('.'.isalpha())