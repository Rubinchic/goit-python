

#exersice 1
'''
class Human:
    def __init__(self, name, age, live_in):
        self.name = name
        self.age = age
        self.live_in = live_in
    
    def speak(self):
        print('-Hello, what is your name?')
        print(f'-my name is {self.name}')
        print(f'-How old are you, {self.name}?')
        print(f'-I am {self.age} years old')
        print(f'-Are you from {self.live_in}?')
        print('-Yes!')

class Me(Human):
        def __init__(self):
            super().__init__('Micle',
                            15,
                            'NewYork',
                            )
hmn = Me()
hmn.speak()
'''

#exersice 2
'''
class ClassList():
    def __init__(self):
        self.quantity = 6
        self.list = [1, 3, 5, 4, 7, 6]

    def __str__(self):
        return self.list

    def sum_el(self):
        theSum = 0
        for i in self.list:
            theSum = theSum + i
        return theSum

    def chet(self):
        theSum = 0
        for i in self.list:
            if i%2 == 0:
                theSum = theSum + 1
        return theSum

array = ClassList()

print(array.__str__())
print(array.sum_el())
print(array.chet())
'''

#exersice 3

class Animal():
    def __init__(self, weight, years, color, poroda):
        self.weight = weight
        self.years = years
        self.color = color
        self.poroda = poroda

    def get_list(self):
        return [f'weight:{self.weight}, years:{self.years}, color:{self.color}, poroda:{self.poroda}']

class cat(Animal):
    def __init__(self):
        super().__init__(3,
                        2,
                        'orange',
                        'meynkun',
                         )

class dog(Animal):
    def __init__(self):
        super().__init__(5,
                         3,
                         'white',
                         'akita-inu',
                         )
