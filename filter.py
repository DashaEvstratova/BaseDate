from out import ConvertFromDictToCLass
import json

with open('bd.json', 'r') as f:
    res = json.load(f)

result = ConvertFromDictToCLass(res)['CHILD']

criteria = input('Enter criteria separated by a space (For example: name-Daria age-19): ')
criteria = criteria.strip().split(' ')

for i in result:
    a = 0
    for j in criteria:
        criter = j.split('-')
        if criter[0] == 'name':
            if i.name == criter[1]:
                a += 1
        if criter[0] == 'age':
            if i.age == int(criter[1]):
                a += 1
        if criter[0] == 'squad':
            if i.squad == criter[1]:
                a += 1
        if criter[0] == 'phone':
            if i.phone == criter[1]:
                a += 1
        if a == 0:
            break
    if a == 2:
        print(i)