file = open("input.txt", "r")

nums = []
for line in file:
    nums.append(int(line))

print(sum(nums))

table = []
current = 0
i = 0
while current not in table:
    table.append(current)
    current += nums[i]
    i = (i+1) % len(nums)

print(current)

