import json

class Data:
    def __init__(self, d):
        for k, v in d.items():
            self.__dict__[k] = v
    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += ' , '
        return result[:-3]

user_data = dict()
print('Enter key-values for example "name:moshe", and exit to finish:')
counter = 1
while True:
    user_input = input(f'{counter}#: ')
    if user_input.upper() == 'exit'.upper():
        break
    # name : moshe
    # list_of_inputs = ['name','moshe']
    # list_of_inputs[0] = 'name' --- key
    # list_of_inputs[1] = 'moshe' --- value
    # list_of_inputs = ['age','20']
    # list_of_inputs[0] = 'age' --- key
    # list_of_inputs[1] = '20' --- value
    list_of_inputs = user_input.split(':')
    if len(list_of_inputs) != 2:
        print('input in wrong format')
        continue
    counter += 1
    user_data[list_of_inputs[0]] = list_of_inputs[1]

print(user_data)
data = Data(user_data)
print(data)
