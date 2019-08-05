

def merge_lists(l: list):
	sorted_lists = []
	added_zeros = 0
	if len(l) % 2 != 0:
		zeros = [0 for _ in range(len(l[0]))]
		added_zeros = len(zeros)
		l.append(zeros)
	for i in range(0, len(l), 2): 
		current_list = l[i]
		current_list_len = len(current_list)
		next_list = l[i + 1]
		merged_list = []
		while current_list and next_list:
			if current_list[0] <= next_list[0]:
				elem = current_list.pop(0)
			else:
				elem = next_list.pop(0)
			merged_list.append(elem)
		if current_list:
			merged_list += current_list
		elif next_list:
			merged_list += next_list
		sorted_lists.append(merged_list)
	return sorted_lists, added_zeros


# O(n * log(n))
def merge_sort(l: list):
	l = [[elem] for elem in l]
	added_zeros = 0
	while len(l) != 1:
		l, zeros = merge_lists(l)
		added_zeros += zeros
	for _ in range(added_zeros):
		l[0].remove(0)
	return l


rand_list = [2, 12, 3, 4, 1, 45, 67, 234, 33, 37, 76, 63, 93, 59, 17, 73, 35, 43, 21, 7]

print(merge_sort(rand_list))
