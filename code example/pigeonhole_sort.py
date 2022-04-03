def pigeonhole_sort(a):
    # size of range of values in the list 
    my_minimum = min(a)
    my_maximum = max(a)
    size = my_maximum - my_minimum + 1
  
    # our list of pigeonholes
    holes = [0] * size
  
    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_minimum] += 1
  
    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_minimum
            i += 1
              
  
a = [8, 3, 2, 5, 4, 6, 4, 8]
print("Sorted order is : ", end =" ")
  
pigeonhole_sort(a)
          
for i in range(0, len(a)):
    print(a[i], end =" ")