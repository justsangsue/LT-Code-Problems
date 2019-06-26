import functools
class Solution:
	"""
	@param logFile: list of string (id + substring)
	@return sorted list
	"""
	def sortLogFile(self, logFile):
		if not logFile:
			return []
		return sorted(logFile, key=functools.cmp_to_key(lambda x, y : self.compareLog(x, y)))

	def compareLog(self, log1, log2):
		log1 = log1[log1.find(' ') + 1:]
		log2 = log2[log2.find(' ') + 1:]
		for i in range(min(len(log1), len(log2))):
			print('log1[i]', log1[i])
			print('log2[i]', log2[i])
			if (log1[i].isdigit()) and (not log2[i].isdigit()):
				print("here1!")
				return 1
			if (not log1[i].isdigit()) and (log2[i].isdigit()):
				print("here2!")
				return -1
			if (log1[i].isdigit() and log2[i].isdigit()) or \
				((not log1[i].isdigit()) and (not log2[i].isdigit())):
				if log1[i] > log2[i]:
					return 1
				if log1[i] < log2[i]:
					return -1
				if log1[i] == log2[i]:
					return 0

if __name__ == '__main__':
	logFile = ["fhie 1df8 sfds",
			   "fdsf 2def sees",
			   "efe2 br9o fjsd",
			   "asd1 awer jik9"]
	sol = Solution()
	print(sol.sortLogFile(logFile))