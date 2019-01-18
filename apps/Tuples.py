
import time
import random
import sys
from datetime import datetime


def GetTempAndHumidity():
    temperature = 35.12
    humidity = 88.36
    return (temperature, humidity)

def main():
    print("BEGIN")
    t,h = GetTempAndHumidity()
    if t > 100:
        print("Temperature={} Humidity={}".format(t,h))
    
    
if __name__ == '__main__':
    main()