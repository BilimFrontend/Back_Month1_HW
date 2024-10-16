
geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}


#1 пункт

deleted_bag = geeks.pop('bag')

#2 пункт

geeks['address'] = 'Ибраимова 103'

#3 пункт

geeks.update(dict(phone='+996 507 052 018', instagram='https://www.instagram.com/geeks_edu/'))

#4 пункт

geeks['courses'].extend(['UX-UI', '1C', 'Project Manager', 'PO Tester', 'SMM Manager', 'Data Science'])
geeks['courses'] = set(geeks['courses'])

#5 пункт
geeks['founded'] = '2018'

#6 пункт
print(f'Количество курсов: {len(geeks['courses'])}')

#7 пункт

for key,value in geeks.items():
    print(f'{key}: {value}')