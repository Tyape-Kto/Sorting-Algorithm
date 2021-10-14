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
  pass
