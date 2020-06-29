import numpy as np
import random
from time import time
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from scipy.optimize import curve_fit
class Solution(object):
	def __init__(self):
		self.test_string = """
		average runtime, {0: .2E} 
		for binary_search with lists of length 10**{1:.2E}
		and number of runs at {2}, 
		likewise the standard deviation is {3:.2E},
		and the total run time including testing setup for this length is {4:.2E}
		"""
		self.test()
	def make_list(self, length=10):
		"""
		:type length: int
		:rtype: numpy.array(List[int])
		:dependencies: numpy, random
		creates a np.array with length random integers between 0,length (inclusive)
		uses random.random and type casts it to achieve a ~10X speed boost 
		over random.randint(0,length) when creating these lists
		random.sample(range(length),length) forgoes replacement, 
		and so another option is needed
		uses np.randint(args) over [int(length * random.random()) for i in range(length)]
		for a increase from 1.53msec to 170 usec with numpy 
		(the numpy will also have better memory usage, if I remember correctl)
		this switches runtime for the length of 10**5 from 161sec to 1sec
		"""

		arr = np.random.randint(0,length,length,int)

		return arr
	def rand_i(self, length):
		"""
		:type length: int
		:rtype: List[int]
		return an starting int index between [0,length) in list form
		"""
		i = random.randrange(0, length)
		return [i]
	def binary_search(self, arr, index_list):
		"""
		:type arr: numpy.array(List[int])
		:type index_list: List[int]
		:rtype: bool
		returns true when arr[i]==0
		returns false when repeat index, or out of bounds moving both left and right.
		recursion max can occur (on macbook_pro 2015: 1000) at length=10**7
		"""
		i = index_list[-1]
		x =  arr[i]
		if x == 0:
			# print("correct path:", index_list)
			return True
		left = i - x
		right = i + x
		#recursions with left and right step checking false situations in if statement
		if left>=0 and left<len(arr) and left not in index_list:
			index_list.append(left)
			# print("left",left_index_list)
			bs = self.binary_search(arr,index_list)
			if bs:
				return True
		if right>=0 and right<len(arr) and right not in index_list:
			index_list.append(right)
			bs = self.binary_search(arr,index_list)
			if bs:
				return True
		return False
	def std_dev(self, time_avg, time_list):
		variance = 0
		for te in time_list:
			variance += (time_avg-te)**2
		std_dev = np.sqrt(variance)/len(time_list)
		return std_dev
	def plot_times(self,time_stats):
		#linear regression fitting and data reformatting
		print("running LinearRegression")
		time_stats = np.array(time_stats)
		lr = LinearRegression()
		lengths = time_stats[:,0]
		X = np.reshape(lengths,(-1,1))
		time_averages = time_stats[:,1]
		time_std_dev= time_stats[:,2]
		lr.fit(X, time_averages)
		r_squared = lr.score(X, time_averages)
		lr_label = "linear R**2= {0:.5f}".format(r_squared)
		#plotting
		print("plotting")
		plt.scatter(lengths, time_averages, color="red", label="average times raw data")
		plt.errorbar(lengths, time_averages, yerr=time_std_dev, linewidth=0,
			elinewidth=2, color="red", label="standard deviations for time data raw")
		plt.plot(lengths, lr.predict(X), color="green", label=lr_label)

		# plt.plot(lengths, logr.predict(X), color="blue")
		plt.title("binary_search as a function of length")
		plt.xlabel("Length")
		plt.ylabel("Average Time of binary_search")
		plt.legend()
		plt.show()
	def test(self):
		time_stats = []
		print("executing code")
		for xp in np.arange(1,6,0.1): 
			#setting up constants for test and run parameters
			length = int(10**xp)
			time_list=[]
			runs = 5*10**3
			tt = time()
			for x in range(runs):
				#running code and finding elapsed time for binary_search
				arr = self.make_list(length)
				index_list = self.rand_i(length)
				t = time()
				bs = self.binary_search(arr, index_list)
				te = time() - t
				time_list.append(te)
			#time stats calculations and printing stats
			time_total = sum(time_list)
			time_avg = time_total/len(time_list)
			time_std_dev = self.std_dev(time_avg, time_list)
			time_stats.append([length, time_avg, time_std_dev])
			test_setup_time = time()-tt - time_total
			# print(self.test_string.format(time_avg, length, runs, time_std_dev, test_setup_time))
		#plotting the timestats
		self.plot_times(time_stats)
Solution()

