def insertionSort(myList):
  
    # Traverse through 1 to len(myList)
    for i in range(1, len(myList)):
  
        key = myList[i]
  
        # Move elements of myList[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < myList[j] :
                myList[j+1] = myList[j]
                j -= 1
        myList[j+1] = key
  
  

myList = [26,78,14,92,57,44,37,58,26]
insertionSort(myList)
print(myList)