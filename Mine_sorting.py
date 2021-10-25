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

"""
def merge(left, right):
### at [0],[11,13] it has flaw
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
  
  ### another one , at this que it has flaw , [8, 9, 13, 20, 20] [0, 2, 3, 4, 20]
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
  if (total - len(sorted_list)) > 1:
    less = total - len(sorted_list)
    if len(left) > len(right):
      sorted_list.extend(left[-less:])
    else:
      sorted_list.extend(right[-less:])
  else:  
    if left[-1] > right[-1]:
      sorted_list.append(left[-1])
    else:
      sorted_list.append(right[-1])
  return sorted_list
  
### this is as far as i can go i couldn't make merge_sort work, this is all i got

def merge_sort(arr):  ### version 1
  print("merge_sort of:", arr)
  if len(arr) > 1:
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    sorted_list = []
    if len(left) >= 1:
      l = merge_sort(left)
      print("l after returned", l)
    if len(right) >= 1:
      r = merge_sort(right)
    if l == None and r == None:
      l, r = left, right
    print('l and r ho, ',l, r)
    return merge(left, right)
    
def merge_sort(arr): ### version 2
  print("merging Started")
  middle = len(arr) // 2
  left = arr[:middle]
  right = arr[middle:]
  print("left",left,"right", right)
  if len(left) == 1:
    print('returned', left)
    return left
  if len(right) == 1:
    print('returned', right)
    return right
  print("left recursion")
  l = merge_sort(left)
  print("right recursion")
  r = merge_sort(right)
  sorted_list = merge(left, right)
  print('returning', sorted_list)
  return sorted_list
  
  

def merge_sort(arr): ### version 3
  if len(arr) < 2:
    return arr[:]
  else:
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)
 """
l = [randint(1,20) for _ in range(10)]
