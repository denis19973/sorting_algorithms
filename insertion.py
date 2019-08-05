

# O(n^2), Ω(n)
def insertion_sort(l: list):
	for i in range(1, len(l)):
		element = l[i]
		j = i
		while j > 0 and l[j-1] > element:
			l[j] = l[j-1]
			j -= 1
		l[j] = element
	return l


rand_list = [2, 12, 3, 4, 1, 45, 67, 234, 33, 37, 76, 63, 93, 59, 17, 73, 35, 43, 21, 7]

print(insertion_sort(rand_list))
