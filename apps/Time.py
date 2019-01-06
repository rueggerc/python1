
import time
import random
import sys
from datetime import datetime

def main():
    timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    print(timestamp)
    
    mytime = datetime.now()
    print(mytime)
    foo = mytime.strftime('%Y/%m/%d %H:%M:%S')
    print(foo)
    
    millis = int(round(time.time() * 1000))
    print("millis is {}".format(millis))


if __name__ == '__main__':
    main()