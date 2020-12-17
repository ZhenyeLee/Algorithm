def binary_search(list,num):
  low = 0
  high = len(list)-1

  while low <= high:
      mid = round((high + low)/2)
      guess = list[mid]
      if guess > num:
        high = mid - 1
      if guess < num:
        low = mid + 1
      if guess == num:
          return mid
  return "None"

mylist = [1, 2, 3, 6, 7, 8, 9]
print(binary_search(mylist,7))
