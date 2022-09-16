from classes import Housing, Leaders, Squads, Children, DataBase
import json


housing1 = Housing(2, 20, 40)
leader1 = Leaders("Daria", "+46655768", 19)
squad1 = Squads(6, 20, "9-10", leader1, housing1)
child1 = Children("Katerina", 9, squad1, "+7654457")

housing2 = Housing(4, 45, 80)
leader2 = Leaders("Timur", "+4665676657", 27)
squad2 = Squads(2, 18, "13-16", leader2, housing2)
child2 = Children("Pasha", 16, squad2, "+76563793")
child3 = Children("Ranel", 15, squad2, "+7653738939")

data_base = DataBase([child1, child2, child3])

r = json.dumps(data_base, default=lambda x: x.__dict__, ensure_ascii=False, indent=4)
my_file = open("bd.json", "w+")
my_file.write(r)
my_file.close()
if __name__ == '__main__':
    print(r)