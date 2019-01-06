
import time
import random
import sys
from datetime import datetime

def main():
    print("BEGIN")
    
    # Strings are immutable
    
    
    foo = "The cat's tail"
    print(foo)
    
    # Reverse Index
    # Get Last letter
    lastChar = foo[-1]
    print(lastChar)
    
    # Slicing
    # Indexing and slicing
    # start:stop:step
    bar = "The fox jumped over the dog"
    
    # Length
    print(len(bar))
    
    # Slice to end
    foxToEnd = bar[4:]
    print(foxToEnd)
    
    # Slice
    fox = bar[4:7:1]
    print(fox)
    
    print("hello \nworld")
    
    # String Methods
    x = "Hello World"
    print(x.upper())
    
    # Split
    foo = "sensor1 43.22 description 4"
    listOfWords = foo.split()
    print(listOfWords)
    
    line = "sensor1,43.22,description,4"
    listOfWords = line.split(",")
    print(listOfWords)
    
    # Formatting
    # String interpolation
    # Format
    x = 42
    print("The value is {}".format(x))
    
    # Formatting by Index
    print("the {2} {1} {0}".format("fox","brown","quick"))
    
    # Formatting by Keyword
    print("the {quick} {brown} {fox} ran at {speed} mph".format(fox="fox",brown="brown",quick="quick",speed=35))
    
    # Floating Point
    # {value:width.precisionf}
    result=100/777
    print(result)
    print("result is {r:5.2f}".format(r=result))
    print("result is {r:05.2f}".format(r=result))
    print("result is {:05.2f}".format(result))
    
    # f-strings
    # python 3.6
    # formatted string literals
    name="Chris"
    print(f"Hello {name}")
    age = 25
    print(f"Hello {name} your age is {age}")
    
   

if __name__ == '__main__':
    main()