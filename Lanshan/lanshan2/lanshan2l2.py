def movezero(nums):
    tmp = []
    for i in nums:
        if i : tmp.append(i)
    for i in range(len(tmp)):
        nums[i] = tmp[i]
    for i in range(len(tmp),len(nums)):
        nums[i] = 0

raw_input = input("Please enter numbers:")
input_nums = list(map(int, raw_input.split()))
movezero(input_nums)
print(input_nums)