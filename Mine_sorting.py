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


def Merge(arr):
  ### this sorting works but it isn't perfect., [13, 16, 7, 19, 6, 7, 16, 5, 5, 3], shit
  if len(arr) < 2:
    return arr[:]
  else:
    middle = len(arr) // 2
    l = Merge(arr[:middle])
    r = Merge(arr[middle:])
    return merge(l, r)

def merge(left, right):
  ### this function is broken, filled with bugs
  i, j = 0, 0
  sorted_list = []
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_list.append(left[i])
      i += 1
    else:
      sorted_list.append(right[j])
      j += 1
  total = len(right) + len(left)
  if (total - len(sorted_list)) == 1:
    if left[-1] > right[-1]:
      sorted_list.append(left[-1])
    else:
      sorted_list.append(right[-1])  
  else:  
    less = total - len(sorted_list)
    if len(left) > len(right):
      sorted_list.extend(left[-less:])
    else:
      sorted_list.extend(right[-less:])
    
  return sorted_list

def quick_sort(arr):
  print("I couldn't make this function work on my own, i am pathetic.")
  


l = [randint(1,20) for _ in range(10)]
