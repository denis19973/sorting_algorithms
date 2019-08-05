

#  O(n^2), Ω(n^2)
def selection_sort(l: list):
	for i in range(len(l)):
		min_element = l[i]
		for j in range(i+1, len(l)):
			if l[j] < min_element:
				l[i] = l[j]
				l[j] = min_element
				min_element = l[i]
	return l


rand_list = [2, 12, 3, 4, 1, 45, 67, 234, 33, 37, 76, 63, 93, 59, 17, 73, 35, 43, 21, 7]

print(selection_sort(rand_list))
 