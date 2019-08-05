

# O(n^2), ussually O(n * log(n))
def quick_sort(l: list):
	smaller = []
	bigger = []
	print(l)
	if len(l) > 1:
		for i in range(len(l)-1):
			pivot = l[-1]
			current_element = l[i]
			if current_element < pivot:
				smaller.append(current_element)
			elif current_element > pivot:
				bigger.append(current_element)
		return quick_sort(smaller) + [pivot] + quick_sort(bigger)
	else:
		return l


rand_list = [2, 12, 3, 4, 1, 45, 67, 234, 33, 37, 76, 63, 93, 59, 17, 73, 35, 43, 21, 7]

print(quick_sort(rand_list))