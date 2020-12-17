def findsmallest(array):
    smallest = array[0]
    smallestindex = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallestindex = i
    return smallestindex

def selectionsort(array):
    i = 0
    newarray = []
    while i < len(array):
        smallest = findsmallest(array)
        #newarray.append(array.pop(smallest))
        newarray.insert(5, array.pop(smallest))
    return newarray


array = [21, 4, 6, 3, 9, 0]
#print(findsmallest(array))
print(selectionsort(array))

