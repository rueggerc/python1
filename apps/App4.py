
import time
import random
import sys


def getReading(maxTemp):
    temp = 100*random.uniform(0.0,1.0)
    print("Compare to {}".format(temp))
    return max(temp,maxTemp)
    
    # delta = abs(maxTemp-temp)  
#     print("Delta is {}".format(delta))
#     if temp > maxTemp:
#         return temp
#     else:
#         return maxTemp



def main():
    print("hello world")
    maxTemp = 0
    
    while True:
        maxTemp = getReading(maxTemp)
        print("Max Temp is {}".format(maxTemp))
        time.sleep(2)

if __name__ == '__main__':
    main()