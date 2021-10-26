'''
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
'''
  
  '''
  def quick_sort(arr):
  if len(arr) < 2:
    print('returned', arr)
    return arr[:]
  middle = arr[-1:]
  left = []
  right = []
  for i in arr[:-1]:
    if i > middle[0]:
      right.append(i)
    else:
      left.append(i)
  print(left, middle, right)
  print('left recursion')
  l = quick_sort(left)
  print('right recursion')
  r = quick_sort(right)
  if l:
    return l.extend(r)
  else:
    return []
def quick_sort_two():
  if len(arr) < 2:
    print('returned',arr[:])
    return arr[:]
  middle = arr[-1]
  left = []
  right = []
  for i in range(len(arr)):
    if middle > arr[i]:
      left.append(arr[i])
    else:
      right.append(arr[i])
  print(left, right)
  if len(left) < len(right):
    l = quick_sort(left)
  else:
    r = quick_sort(right)
  print(left, right)
'''
