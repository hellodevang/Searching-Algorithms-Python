n = int(input("How many elements do you want to play with?"))
a = []

for i in range(n):
	a.append(int(input("Enter Element")))

s = int(input("Enter element to search: "))

def search(s, a):

	for i in range(len(a)):
		if s == a[i]:
			return i
		else:
			return 0

if search(s, a) == 0:
	print("Element doesn't Exist")
else:
	print("Element " + str(s) + " found at index " + str(search(s,a)))