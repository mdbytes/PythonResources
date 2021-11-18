
def main():
    nums = [0,1,4,5,3,6,7,82,2,4,5,6,6,82]
    max_dup = get_max_dup(nums)
    print(max_dup)

def get_max_dup(nums):
    dups = []
    for num in nums:
        k = 0
        for i in range(0,len(nums)):
            if num == nums[i]:
                k += 1
        if k > 1:
            dups.append(num)
    if len(dups) > 0:
        return max(dups)
    else:
        return -1

main()