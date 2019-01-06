
import time
import random
import sys
from datetime import datetime

def incrementByOne(value):
    return value+1

def main():
    print("== LEARN LISTS ==")
    myList = [1,2,3,4,5]
    print(myList)
    print("myList Length=" + str(len(myList)))
    
    # Index and Slice
    myList = ["cat", "dog", "bird"]
    print(myList[1])
    print(myList[1:])
    
    # Concatenate
    list1 = [1,2,3]
    list2 = [4,5,6]
    print(list1+list2)
    list3=list1+list2
    print(list3)
    
    # Mutated
    myList = ["cat", "dog", "bird"]
    myList[1] = "lizard"
    print(myList)
    
    # Append
    myList.append("snake")
    print(myList)
    
    # Remove
    poppedItem = myList.pop(2)
    print(myList)
    print(poppedItem)
    
    # Sort (in-place)
    letters = ["z","d","x","f","c"]
    numbers = [42,3,1,0,12,6,11]
    letters.sort()
    numbers.sort()
    print(letters)
    print(numbers)
    
    # Reverse
    myList = [4,3,8,1]
    myList.reverse()
    print(myList)
    
    foo = incrementByOne(43)
    print(foo)
    

if __name__ == '__main__':
    main()