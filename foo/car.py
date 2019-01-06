import random
from random import randint

class Car(object):

    def __init__(self, params):
        print("Car Constructor")
        '''
        Constructor
        '''
        
        
    def drive(self):
        print ("Car is Driving!!")
        x = 10*random.uniform(0.0,1.0)
        print('x is {:1.2f}'.format(x))
        
        s = 'temp= {:1.2f}'.format(x)
        print(s)
        
        y = random.uniform(0,100)
        print('y is {}'.format(y))
        
        # Aandom Int
        z = randint(0,9)
        print('z is {}'.format(z))
        