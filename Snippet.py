lst = []
tpl = ('Ram','Mohan','Shyam','Raju','Abdul','Chris','Suman','Muskan')
dct = {
    'Ram' : 98,
    'Mohan' : 99,
    'Shyam' : 89,
    'Raju' : 91,
    'Abdul' : 34,
    'Chris' : 80,
    'Suman' : 76,
    'Muskan' : 59,
} 

print('Initial Data')
print(lst)
print(tpl)
print(dct)

len_tpl = len(tpl) - 1

for i in range(0,len_tpl):
    if len(tpl[i]) >= 5:
        lst.append(tpl[i])
    if dct[tpl[i]] < 50:
        dct.pop(tpl[i])

print('\nFinal Data')
print(lst)
print(tpl)
print(dct)

'''
Output :-

Initial Data
[]
('Ram', 'Mohan', 'Shyam', 'Raju', 'Abdul', 'Chris', 'Suman', 'Muskan')
{'Ram': 98, 'Mohan': 99, 'Shyam': 89, 'Raju': 91, 'Abdul': 34, 'Chris': 80, 'Suman': 76, 'Muskan': 59}

Final Data
['Mohan', 'Shyam', 'Abdul', 'Chris', 'Suman']
('Ram', 'Mohan', 'Shyam', 'Raju', 'Abdul', 'Chris', 'Suman', 'Muskan')
{'Ram': 98, 'Mohan': 99, 'Shyam': 89, 'Raju': 91, 'Chris': 80, 'Suman': 76, 'Muskan': 59}
'''