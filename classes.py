class Housing(object):
    def __init__(self,number, free_place, all_place):
        self.number = number
        self.free_place = free_place
        self.all_place = all_place

    def __str__(self):
        return f'number: {self.number}, all place: {self.all_place}, free plase: {self.free_place}'


class Squads(object):
    def __init__(self, number, amount, age, leader, hausing):
        self.number = number
        self.amount = amount
        self.age = age
        self.leader = leader
        self.hausing = hausing

    def __str__(self):
        return f'number: {self.number}, amount: {self.amount}, age: {self.age}, leader: {self.leader}, hausing: {self.hausing}'


class Leaders(object):
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age

    def __str__(self):
        return f'name: {self.name}, phone: {self.phone}, age: {self.age}'


class Children(object):
    def __init__(self, name, age, squad, phone):
        self.name = name
        self.age = age
        self.squad = squad
        self.phone = phone

    def __str__(self):
        return f'name: {self.name}, age: {self.age},squad: {self.squad}, phone: {self.phone}'


class DataBase(object):
    def __init__(self, child):
        self.child = child

    def __str__(self):
        return f'child: {self.child}'