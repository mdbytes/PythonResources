'''
Compute the sum of the list [1,3,5,7,9] using recursion

'''

# without recursion

numlist = [1,3,5,7,9]
sum = 0

for i in numlist:
    sum += i
    
print(f"The total is {sum}")


# with recursion

def listsum(number_list):
    
    # base case (smallest list) provides termination of recursion
    if len(number_list) == 1: 
        return number_list[0]
    
    else:
        return number_list[0] + listsum(number_list[1:])
    
sum = listsum(numlist)

print(f"The total is {sum}")
