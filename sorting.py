from random import randint
### This sorting algorithm sorts from backwards [Picchadi bate mildai aauxa]
def Bubble(arr):
  for j in range(len(arr)):
    for i in range(len(arr)-j-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr

def Insertion(arr):
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr


l = [randint(1,20) for _ in range(10)]
