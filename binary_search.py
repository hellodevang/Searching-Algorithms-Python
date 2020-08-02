import math

n = int(input("Enter number of elements"))
a = []
for i in range(n):
	a.append(int(input("Enter Element")))

low_index = 0
high_index = len(a)-1
key = int(input("Enter element to search"))
mid_index = math.floor((low_index+high_index)/2)

def binary(key, mid_index, low_index, high_index):

	if key == a[mid_index]:
		print("Element found at index "+ str(mid_index))

	while True:
		if key > a[mid_index]:
			low_index = mid_index + 1
			mid_index = math.floor((low_index+high_index)/2)
			if key == a[mid_index]:
				print("Element found at index "+ str(mid_index))
				break
			elif low_index > high_index:
				print("Element not found")
				break

		elif key < a[mid_index]:
			high_index = mid_index - 1
			mid_index = math.floor((low_index+high_index)/2)
			if key == a[mid_index]:
				print("Element found at index "+ str(mid_index))
				break
			elif low_index > high_index:
				print("Element not found")
				break

binary(key, mid_index, low_index, high_index)

