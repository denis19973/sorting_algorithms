from copy import copy


def simple_bubble_sort(l: list):
	"""
	Max count of iterations for sorting all elements in list with n elements is n - 1.
	for example: sorting [2, 1] needs 1 iteration; [3, 2, 1] needs 2 iterations
	"""
	iterations = 0
	for _ in range(len(l) - 1):
		for i in range(len(l) - 1):
			iterations += 1
			a = l[i]
			b = l[i + 1]
			if b < a:
				l[i] = b
				l[i+1] = a
	print('num iterations: {}'.format(iterations))
	return l


def optimized_bubble_sort(l: list):
	"""
	• In first iteration biggest number moves to the end of list also in second iteration the biggest 
	number from remainings moves to the end and stays before last element(from first iteration).
	This means that we can optimize our algorithm by not checking last k elements after each k iteration
	
	• Also we can add boolean variable(not_sorted) that will indicate that in current iteration wasn't sorting action 
	and it means that there is no more numbers to move, sorting completed.
	 """
	iterations = 0
	not_sorted = False
	for k in range(1, len(l)):
		if not_sorted:
			break
		for i in range(len(l) - k):
			iterations += 1
			a = l[i]
			b = l[i + 1]
			if b < a:
				l[i] = b
				l[i+1] = a
			else:
				not_sorted = True
	print('num iterations: {}'.format(iterations))
	return l


rand_list = [2, 12, 3, 4, 1, 45, 67, 234, 33, 37, 76, 63, 93, 59, 17, 73, 35, 43, 21, 7]

print(simple_bubble_sort(copy(rand_list)))
# >> num iterations: 361
# >> [1, 2, 3, 4, 7, 12, 17, 21, 33, 35, 37, 43, 45, 59, 63, 67, 73, 76, 93, 234]

print(optimized_bubble_sort(copy(rand_list)))
# >> num iterations: 19
# >> [1, 2, 3, 4, 7, 12, 17, 21, 33, 35, 37, 43, 45, 59, 63, 67, 73, 76, 93, 234]
