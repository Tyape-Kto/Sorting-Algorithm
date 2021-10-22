from random import randint

def Bubble(arr):
  """
    This checks 2 element each time and checks for len(arr) times [ Picchadi bate mildai aau6 ] { TimeComplexity: O(n^2) }
  """
  for j in range(len(arr)):
    for i in range(len(arr)-j-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
  return arr

def Insertion(arr):
  """
    This checks one element to every then moves on, sorts from forward [first element bate mildai aau6] { O(n^2) } 
  """
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] > arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
  return arr

def toMerge(left, right):
  sorted_list = []
  i, j = 0, 0
  while j < len(right) and i < len(left):
    if left[i] > right[j]:
      sorted_list.append(right[j])
      j += 1
    else:
      sorted_list.append(left[i])
      i += 1
  if len(sorted_list) < len(left) + len(right):
    if right[-1] > left[-1]:
      sorted_list.append(right[-1])
    else:
      sorted_list.append(left[-1])
  return sorted_list

def Merge(arr):
  


l = [randint(1,20) for _ in range(10)]
