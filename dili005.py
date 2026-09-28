nums=[2,7,11,15]
target_nums=[]
target=int(input("请输入目标值: "))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            target_nums.append([i, j])
else:
    print("未找到满足条件的数组。")
for n in target_nums:  
    print(n)