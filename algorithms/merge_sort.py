def merge_sort(lst_input: list):

		if len(lst_input) <= 1:
			return lst_input

		middle_index = len(lst_input)//2

		left_half =  lst_input[:middle_index]
		right_half = lst_input[middle_index:]

		sorted_left = merge_sort(left_half)
		sorted_right = merge_sort(right_half)

		merged = []
		left_index = 0
		right_index = 0

		while left_index < len(sorted_left) and right_index < len(sorted_right):
			if sorted_right[right_index] < sorted_left[left_index]:
				merged.append(sorted_right[right_index])
				right_index += 1

			else:
				merged.append(sorted_left[left_index])
				left_index += 1

		if left_index < len(sorted_left):
			merged.extend(sorted_left[left_index:])

		if right_index < len(sorted_right):
			merged.extend(sorted_right[right_index:])

		return merged

merge_sort([1, 2, 3, 4])