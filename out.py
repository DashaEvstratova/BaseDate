from classes import Housing, Squads, Leaders, Children
import json

CHILD1 = []
CHILD = []
SQUAD1 = []
SQUAD = []
LEADER = []
HOUS = []

def ConvertFromDictToCLass(res):
    result = {}
    b = []
    key = res.keys()
    for i in key:
        for j in res[i]:
            a = []
            key_child = list(j.keys())
            for k in key_child:
                a.append(j[k])
            if a not in b:
                b.append(a)
                CHILD1.append(Children(a[0], a[1], a[2], a[3]))

    a = []
    count_squad = 0
    for i in CHILD1:
        key_squad = list(i.squad.keys())
        list_of_squad = [i.squad[key_squad[0]], i.squad[key_squad[1]], i.squad[key_squad[2]],
                         i.squad[key_squad[3]], i.squad[key_squad[4]]]
        if list_of_squad not in a:
            a.append(list_of_squad)
            SQUAD1.append(Squads(a[count_squad][0], a[count_squad][1], a[count_squad][2],
                                a[count_squad][3], a[count_squad][4]))
            count_squad += 1

    a = []
    b = []
    count_hous = 0
    count_lead = 0
    for i in SQUAD1:
        key_leader = list(i.leader.keys())
        key_housing = list(i.hausing.keys())
        list_of_lead = [i.leader[key_leader[0]], i.leader[key_leader[1]], i.leader[key_leader[2]]]
        if list_of_lead not in a:
            a.append(list_of_lead)
            LEADER.append(Leaders(a[count_lead][0], a[count_lead][1], a[count_lead][2]))
            count_lead+=1
        list_of_hous = [i.hausing[key_housing[0]], i.hausing[key_housing[1]], i.hausing[key_housing[2]]]
        if list_of_hous not in b:
            b.append(list_of_hous)
            HOUS.append(Housing(b[count_hous][0], b[count_hous][1], b[count_hous][2]))
            count_hous+=1
    result['LEADER'] = LEADER
    result['HOUS'] = HOUS

    for i in SQUAD1:
        for j in LEADER:
            if i.leader[list(i.leader.keys())[0]] == j.name:
                leader = j
                break
        for j in HOUS:
            if i.hausing[list(i.hausing.keys())[0]] == j.number:
                house = j
                break
        SQUAD.append(Squads(i.number, i.amount, i.age, leader.name, house.number))
    result['SQUAD'] = SQUAD

    for i in CHILD1:
        for j in SQUAD:
            if i.squad[list(i.squad.keys())[0]] == j.number:
                squad = j
                break
        CHILD.append(Children(i.name, i.age, squad.number, i.phone))
    result['CHILD'] = CHILD

    return result
