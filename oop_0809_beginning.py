class MobilePhone:
    def __init__(self, model, size, color, os_name):  # magic function(build in function in python)
        #this function will be called every time we will creatrea new object(this time mobile phone)
        print('new phone was created')
        print(f'parameters send: {model}, {size}, {color}, {os_name}')

        self.model = model # like lines 31-34
        self.size = size
        self.color = color
        self.os_name = os_name


    def turn_on(self):
        print('turning on phone...')
    def turn_off(self):
        print('turning off phone')
    def ring(self):
        print('phone is ringing')
    def play_music(self):
        print('la la la...')


samsung_s10_ultra = MobilePhone(model='samsung s10 ultra', size=6.5, color='blue', os_name="android10")#calls the __init__ function(the build in function)
iphone_x = MobilePhone(model='iphone x', size=6.5, color='white', os_name='ios13') #this line calls __init__ function again.(its a generic function)
iphone_x.color = 'black'
print(f'the color is,{iphone_x.color}')
samsung_s10_ultra.extra = 'the screen is extra sharp'
print(samsung_s10_ultra.extra)
print('============================')
'''
iphone_x.model = 'iphone x'
iphone_x.size = 6.5
iphone_x.color = 'white'
iphone_x.os_name = 'ios13' #lina 17and line 31 - 34 is basicley the same, the diffrance is it runs it over this way, and we may forget to add somthting without the __init__ function
                           #its a bad practice,  we better put it inside the __init__ function

#d_map_id_to_name = dict()

samsung_s10_ultra.turn_on()
samsung_s10_ultra.turn_off()
samsung_s10_ultra.ring()
samsung_s10_ultra.play_music()

iphone_x = MobilePhone(model='iphone x', size=6.5, color='white', os_name='ios13') #this line calls __init__ function again.(its a generic function)
iphone_x.turn_on()
iphone_x.turn_off()
iphone_x.ring()
iphone_x.play_music()'''
print('=================================')
class Computer():
    # called when creating instance
    def __init__(self, color = 'black'):
        self.color = color
    def turnOn(self):
        print("On...")

lenovo = Computer() # creating instance
mac = Computer('blue') # creating instance with color blue
lenovo.turnOn()
lenovo.color = 'red'
print(lenovo.color)
print(mac.color)

# create Person class
# func: sayHello()
# data: name , __init__  parameter
# data: age , __init__  parameter
# *etgar: sayMyName() - print
#       current person name
# create 2 persons
# set name default value 'Incognito'
class Person():
    def __init__(self,
                 time,
                 name = 'Incognito'
                 , age = 0):
        self.__time = time
        self.name = name
        self.age = age
    def sayMyName(self):
        print(f'name = {self.name}')
    def getTime(self):
        return self.__time + ' GMT+3'

dana = Person('13:00', 'Dana', 33)
print(dana.name, dana.age)
dana.sayMyName()
print(dana.getTime())
