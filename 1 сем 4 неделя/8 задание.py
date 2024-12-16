def NIGGER(x):
    while x > 9:
        x = sum(int(i) for i in str(x))
    return x

def partition(nums, low, high):  
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while NIGGER(nums[i]) <= NIGGER(pivot):
			if NIGGER(nums[i]) = NIGGER(pivot):
				if nums[i] < pivot:
					i+=1
			else:
            	i += 1

        j -= 1
        while NIGGER(nums[j]) >= NIGGER(pivot):
			if NIGGER(nums[j]) = NIGGER(pivot):
                if nums[j] > pivot:
                    j-=1
            else:         
				j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)



n = list(map(int, input().split()))
quick_sort(n)
print(n)
	