def two_sum(arr, target):
	"""
	The two sum problem. Return all possible pairs' index as 2-tuple.
	"""
	ans = []
	seen = {}
	for (idx, el) in enumerate(arr):
		other_num = target - el
		if other_num in seen:
			for i in seen[other_num]:
				ans.append((idx, i)) # Every pair that adds up to target is included

		if el in seen:
			seen[el].append(idx)
		else:
			# First time see other_num
			seen[el] = [idx]

	return ans

def two_sum_2_pointer(numbers, target):
    left = 0
    right = len(numbers) - 1
    ans = []
    while left < right:
        print(left, right)
        if numbers[left] + numbers[right] == target: 
            ans.append((left, right))
            while left < right and numbers[left+1] == numbers[left]:
                left += 1
            while left < right and numbers[right-1] == numbers[right]:
                right -= 1
        if (numbers[left] + numbers[right]) > target:
            right -= 1
        else:
            left += 1

    return ans

def three_sum(nums):
	dupref = set()
	ans = []
	for (idx, n1) in enumerate(nums):
		for n2_idx, n3_idx in two_sum(nums[idx + 1:], -n1):
			print(n2_idx, n3_idx)
			triplets_uniq = frozenset((n1, nums[n2_idx + idx + 1], nums[n3_idx + idx + 1]))
			if(triplets_uniq not in dupref): 
				ans.append([n1, nums[n2_idx + idx + 1], nums[n3_idx + idx + 1]])
				dupref.add(triplets_uniq)

	return ans 



if __name__ == '__main__':
	a = [-1,0,1,2,-1,-4]
	# print(two_sum([1, 1, -2], -1))
	# print(three_sum(a))
	b = [1,2,3,4,5,6,7,8,9]
	print(two_sum_2_pointer(b, 10))

