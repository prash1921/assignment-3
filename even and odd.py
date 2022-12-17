numbers =(1,2,3,4,5,6,7,8,9)
count_ odd= 0
count_even= 0
for x in numbers :
    if not x % 2:
        count_even+=1
        else:
            count_odd+=1
            print("numbers is even :",count_even)
            print("numbers is odd :" ,count_odd)
