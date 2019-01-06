
import time
import random
import sys
from datetime import datetime

def main():
    
    # Mod
    foo = 13 % 10
    print(foo)
    
    # 2^3
    bar = 2**3
    print(bar)
    
    bar = 3.14
    foo = int(bar)
    print("foo=" + str(foo))
    
    # Get Type 
    print("Type of bar is " + str(type(bar)))


if __name__ == '__main__':
    main()