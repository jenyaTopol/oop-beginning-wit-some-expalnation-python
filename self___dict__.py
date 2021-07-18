
import json

class Person:
    def __init__(self, d):
        #d ==  {'name' : 'Moshe',
        #     'age' : 37,
        #    'city' : 'Ashdod'}
        # 1
        #self.__dict__ = d
        # 2
        for k, v in d.items():
            self.__dict__[k] = v

        #self.name = name
        #self.age = age
        #self.city = city
    def __str__(self):
        #return f'name : {self.name} {self.age}'
        # age : {self.age}'
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += ' , '
        return result[:-3]

print('=========================')
#moshe = Person(1,'Moshe', 37, "Ashdod")

moshe = Person({'id ': 1,
                'name' : 'Moshe',
                'age' : 37,
                'city' : 'Ashdod'})
#initParam['age'] = 40
print(moshe)
# this needs to work
moshe.height = 1.95
moshe.__dict__['height'] = 1.95
print(moshe)

print('============================')

moshe.__dict__['hi'] = 'hello'
print(moshe.hi) # 'hello'
moshe.hi = 'hello'

print(moshe)
#print(moshe.__dict__)

dic_came_as_string = json.loads('{"id": 1,"name" : "Moshe", "age" : 37, "city" : "Ashdod"}')
print(dic_came_as_string)
print(dic_came_as_string.keys())
