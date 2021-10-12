#Bubble-Sorting
from random import randint

def Bubble(arr):
  for i in range(len(arr)):
    print(arr[i])

l = [randint(1,20) for _ in range(10)]
Bubble(l)
