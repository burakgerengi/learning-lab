class Replacement:

	@staticmethod
	def search_and_replace(value_to_replace, replacing_value, lst: list) -> None:
		
		for current_index in range(0, len(lst)):

				if lst[current_index] == value_to_replace:
					lst[current_index] = replacing_value

	@staticmethod
	def replace_values_in_the_same_index(lst1: list, lst2: list, index_to_replace: int) -> None:

		try:
			temp_1, temp_2 = lst1[index_to_replace], lst2[index_to_replace]

			lst2[index_to_replace] = temp_1
			lst1[index_to_replace] = temp_2
		except IndexError as e:
			print("Index out of range:", e)

numbers = [1, 4, 7, 4, 9]
prices = [120, 250, 90]
backup_prices = [110, 230, 95]

print(numbers)
Replacement.search_and_replace(4, 99, numbers)
print(numbers)

print(prices, backup_prices)
Replacement.replace_values_in_the_same_index(prices, backup_prices, 1)
print(prices, backup_prices)