arr = [int(i) for i in input().split(" ")]


def sort(arr):
	#sorting algo
	# n = len(arr)

	# for i in range(n):
	# 	for j in range(0,n-i-1):
	# 		if arr[j] > arr[j+1]:
	# 			arr[j], arr[j+1] = arr[j+1], arr[j]
	# 1/0
	# while True:
	# 	pass
	#while True:
	#	pass
	arr.sort()
	return arr


print(*sort(arr))




