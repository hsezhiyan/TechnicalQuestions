from itertools import combinations 
import numpy as np

def create_indices_array(length):
	indices_arr = [0] * length
	for i in range(length):
		indices_arr[i] = i
	return indices_arr

def sum_of_array(A):
	sum = 0
	for i in range(len(A)):
		sum = sum + A[i]
	return sum

def minimum_for_length(A, comb, sum):
	max_possible = 10000
	internal_sum = 0
	for i in list(comb):
		for j in i:
			internal_sum = internal_sum + A[j]
		if abs(2 * internal_sum - sum) < max_possible:
			max_possible = abs(2 * internal_sum - sum)
		internal_sum = 0
	return max_possible

def solution(A):
	max_possible = 10000
	sum = sum_of_array(A)
	indices_arr = create_indices_array(len(A))

	for i in range(len(A)):
		if minimum_for_length(A, combinations(indices_arr, i + 1), sum) < max_possible:
			max_possible = minimum_for_length(A, combinations(indices_arr, i + 1), sum)

	return(max_possible)

a = np.array([1, 2, 3, 4, 100])

print(solution(a))
