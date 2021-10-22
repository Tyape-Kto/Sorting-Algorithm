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
  
### this is as far as i can go i couldn't make merge_sort work, this is all i got

def merge_sort(arr): 
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
 """
l = [randint(1,20) for _ in range(10)]
