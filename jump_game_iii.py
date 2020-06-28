# from random import randrange, seed
# import numpy as np
#
#
# class Solution(object):
#     def __init__(self):
#         """
#         """
#         pass
#
#     def can_reach(self, arr, start):
#         """
#         :type arr: List[int]
#         :type start: int
#         :rtype: bool
#         returns whether a zero can be reached by moving indecies
#         forwards or backwards determined by the number (int) at the current index
#         """
#         answer = self.brute(arr, start)
#
#     def brute(self, arr, start):
#         """
#         :type arr: List[int]
#         :type start: int
#         :rtype: bool
#         does a brute force can_reach() search
#         binary search, where we branch and try both above and below
#         """
#         x = arr[start]
#         if x == 0:
#             return True
#         elif start - x >= 0:
#             left_answer = self.brute(arr, start - x)
#             if left_answer == True:
#                 return True
#         elif start + x < len(arr):
#             right_answer = self.brute(arr, start + x)
#             if right_answer == True:
#                 return True
#         else:
#             return False
#
#     def test(self, length=10):
#         """
#         :type length: int
#         :rtype: None
#         generates and prints out random seed arrays used, start_index,
#         tests can_reach() for each array and prints
#         """
#         assert 1 <= length and length <= 5 * 10 ^ 4, "\
#         length of list is out of the range of 1 <= arr.length <= 5 * 10^4"
#         for sd in range(10):
#             arr = self.make_list(length, sd)
#             start = self.start_index(length, sd)
#             print(arr, start)
#             cr = self.can_reach(arr, start)
#             print(cr)
#
#     def make_list(self, length=10, sd=1):
#         """
#         :type length: int
#         :type sd: int
#         :rtype: List[int]
#         creates a list which follows the following constraint
#         0 <= arr[i] < arr.length
#         """
#         seed(sd)
#         arr = [randrange(0, length) for x in range(length)]
#         arr = np.array(arr)
#         return arr
#
#     def start_index(self, length=10, sd=1):
#         """
#         :type length: int
#         :type sd: int
#         :rtype: int
#         creates a start index which follows the following constraint
#         0 <= start < arr.length
#         """
#         seed(sd)
#         start = randrange(0, length)
#         return start
import numpy as np
import random
def make_list(length=10):
	"""
	:type length: int
	:rtype: numpy.array(List[int])
	:dependencies: numpy, random
	creates a np.array with length random integers between 0,length (inclusive)
	"""
	arr = np.array([random.randint(0,length) for i in range(length)])
	return arr
def rand_i(length=10):
	"""
	:type length: int
	:rtype: List[int]
	return an starting int index between [0,length) in list form
	"""
	i = random.randint(0, length-1)
	return [i]
def binary_search(arr, index_list):
	"""
	:type arr: numpy.array(List[int])
	:type index_list: List[int]
	:rtype: bool
	returns true when arr[i]==0
	returns false when repeat index, or out of bounds moving both left and right.
	"""
	# print("ir",index_list)
	i = index_list[-1]
	# print("i", i)
	x =  arr[i]
	if x == 0:
		return True
	left = i - x
	right = i + x
	if left>=0 and left<len(arr) and left not in index_list:
		left_index_list = index_list.append(left)
		# print("left",left_index_list)
		bs = binary_search(arr,left_index_list)
		if bs:
			return True
	if right>=0 and right<len(arr) and right not in index_list:
		right_index_list=index_list.append(right)
		bs = binary_search(arr,right_index_list)
		if bs:
			return True
	return False
def test():
	length = 10
	for x in range(100):
		arr = make_list(length)
		print(arr)
		index_list = rand_i(length)
		bs = binary_search(arr, index_list)
		print(bs)

test()