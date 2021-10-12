from random import randint

def Bubble(arr):
  for j in range(len(arr)):
    for i in range(len(arr)-j-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr

l = [randint(1,20) for _ in range(10)]
Bubble(l)
