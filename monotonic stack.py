# monotonic stack
# randome
import random

nums:int = []
for i in range(10):
	nums.append(random.randrange(1,100))
print(nums)
for n in nums:
    print('='*n)
stack = []
res = [-1]*len(nums)

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        res[idx] = nums[i]
    stack.append(i)
print(res)