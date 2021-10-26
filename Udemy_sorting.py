### Bubble sorting from udemy python mastery course
def bubble_sort(arr):
  swap_happened = True
  while swap_happened:
    swap_happened = False
    for i in range(1,len(arr)):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        swap_happened = True
  return arr


def merge_sort(arr):
  if len(arr) < 2:
    return arr[:]
  else:
    middle = len(arr) // 2
    l = merge_sort(arr[:middle])
    r = merge_sort(arr[middle:])
    return merge(l, r)

def merge(left, right):
  sorted_list = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      sorted_list.append(left[i])
      i += 1
    else:
      sorted_list.append(right[j])
      j += 1
  while i < len(left):
    sorted_list.append(left[i])
    i += 1
  while j < len(right):
    sorted_list.append(right[j])
    j += 1
  return sorted_list

def quick_sort(arr):
  pass
