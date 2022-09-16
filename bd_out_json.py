from out import ConvertFromDictToCLass
import json


if __name__ == '__main__':
    with open('bd.json', 'r') as f:
        res = json.load(f)

    result = ConvertFromDictToCLass(res)

    print('HOUSE')
    for i in result['HOUS']:
        print(i)
    print('')

    print('LEADERS')
    for i in result['LEADER']:
        print(i)
    print('')

    print('SQUAD')
    for i in result['SQUAD']:
        print(i)
    print('')

    print('CHILD')
    for i in result['CHILD']:
        print(i)
    print('')

