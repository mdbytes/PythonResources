
def main():
    square = get_square()
    result = test_square(square)
    display(result)

def get_square():
    square = []
    row = []
    for i in range(0,3):
        for j in range(0,3):
            row.append(int(input("enter an integer between 1 and 9: ")))
        square.append(row)
        row = []
    return square

def test_square(square):
    nums = [1,2,3,4,5,6,7,8,9]
    row_sum = 0
    col_sum = 0
    diag_one_sum = 0
    diag_two_sum = 0
    sums = []
    for i in range(0,3):
        for j in range(0,3):
            if square[i][j] in nums:
                nums.remove(square[i][j])
            else:
                return (False,"The square is not comprised of the numbers 1 to 9")
            row_sum += square[i][j]
            col_sum += square[j][i]
            if i == j:
                diag_one_sum += square[i][j]
            if i==0 and j==2:
                diag_two_sum += square[i][j]
            if i==1 and j==1:
                diag_two_sum += square[i][j]
            if i==2 and j==0:
                diag_two_sum += square[i][j]
        sums.append(row_sum)
        sums.append(col_sum)
        row_sum = 0
        col_sum = 0
    sums.append(diag_one_sum)
    sums.append(diag_two_sum)

    return sum_test(sums)        

def sum_test(sums):
    # for i in range(1,len(sums)-1):
    #     if sums[i] != sums[i-1]:
    #         return (False,"The sums are not equal")
    # return (True,"The sums are equal and the numbers between 1 and 9")

def display(result):
    if result[0]:
        print("This is a Lo Shu Magic Square: ",result[1])
    else: 
        print("Not a Lo Shu Magic Square: ",result[1])

main()