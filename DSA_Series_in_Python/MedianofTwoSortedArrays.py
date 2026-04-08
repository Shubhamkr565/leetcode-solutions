def medianOfSortedArr(num1, num2):
    l1 = len(num1)
    l2 = len(num2)

    num3 = []
    i = 0
    j = 0
    while i < l1 and j < l2:
        if(num1[i] < num2[j]):
            num3.append(num1[i])
            i += 1
        else:
            num3.append(num2[j])
            j += 1
    while i<l1:
        num3.append(num1[i])
        i += 1
    while j<l2:
        num3.append(num2[j])
        j += 1
    print(num3, end=" ")
    
    l3 = len(num3)
    if l3 % 2 !=0:
        print("Median Of two Sorted Array: ",float(num3[l3//2]))
    else:
        median = (num3[l3//2-1]+ num3[l3//2])/2
        print("Median Of two Sorted Array: ",float(median))


num1 = [1,2]
num2 = [3,4]

medianOfSortedArr(num1,num2)
