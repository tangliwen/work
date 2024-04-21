班解决方案：
 定义 搜索插入(self, nums: list[int], target: int)-> int:
left,right = zero ,len(nums)- one
whileleft <= right:
m =(left+right)// two
iftarget < nums[m]:
right = m- one
eliftarget > nums[m]:
left = m+ one
else:
returnm
returnright+ one

nums=[ one , three , five , six]
target= five
print(Solution() . 搜索插入(nums,target))
