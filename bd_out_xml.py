from out import ConvertFromDictToCLass
import xmltodict


if __name__ == '__main__':
    with open('bd.xml') as fd:
        doc = xmltodict.parse(fd.read(), process_namespaces=True)

    result = ConvertFromDictToCLass(doc['DataBase']['childs'])

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
