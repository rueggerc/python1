import sys
import random
import time
import socket
from datetime import datetime


def getMessage():
    host = socket.gethostname()
    temp = 100*random.uniform(0.0,1.0)
    millis = int(round(time.time() * 1000))
    timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    msg = '{},{:#5.2f},{},{}'.format(host,temp,millis,timestamp)
    return msg


numParms = len(sys.argv)
print("Number of Parms={}".format(numParms))

print("Parm0=" + sys.argv[0])
for x in range(numParms):
    print("Next Parm=" + sys.argv[x])
    
temp = 100*random.uniform(0.0,1.0)
print('x is {:1.2f}'.format(temp))

millis = int(round(time.time() * 1000))
print('Time={}'.format(millis))

host = socket.gethostname()
print('Host={}'.format(host))

timestamp=datetime.now().strftime('%Y/%m/%d %H:%M:%S')
print("TIMESTAMP=" + timestamp)

msg = '{},{:#5.2f},{},{}'.format(host,temp,millis,timestamp)
print("MSG=" + msg)

now = datetime.now()
print(now.strftime("%c"))

print("NOW=" + now.strftime("%Y/%b/%d"))

print(now)

#foo = now.strftime("%c") + now.strftime("%x") + now.strftime("%X")
#print(foo)

age=74
bar = f"Hello You are {age}"
print(bar)

junk=1.45
print("{:#05.2f}".format(junk))

junk=1.45
print("{:5.2f}".format(junk))

finalMessage = getMessage()
print(finalMessage)

#date_string = f"{datetime.now():%Y-%m-%d %H:%M:%S%z}"
#print(date_string)




