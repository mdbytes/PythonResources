numbers_file = open('Average_Numbers/numbers.txt','r')
sum = 0
num = 0

for line in numbers_file:
    sum += float(line)
    num += 1

print(sum/num)


