class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e

class Solution:
	def insert2(self, intervals, new_interval):
		intervals.append(new_interval)
		intervals.sort()
		for x in intervals:
			print x.start, x.end
		
	def insert(self, intervals, new_interval):
		new =[]
		i=0
		First_overlap = False
		overlap_start =0
		overlap_end =0
		min_num = 0 
		if(len(intervals) > 0):
			min_num= intervals[0].start
		for x in intervals:
			max_a_c = max(x.start, new_interval.start)
			min_b_d = min(x.end , new_interval.end)
			min_num = min(x.start,min_num)

			if(max_a_c > min_b_d):				
				if(overlap_start > 0):
					new.append(Interval(overlap_start,overlap_end))
					overlap_start = 0

				new.append(Interval(x.start,x.end))				
			else:
				min_a_c = min(x.start, new_interval.start)
				overlap_end = max(x.end , new_interval.end,overlap_end)					

				if(First_overlap == False):
					overlap_start = min_a_c
					First_overlap = True
		
		if(First_overlap == False):
			start = min(new_interval.start,new_interval.end)
			end = max(new_interval.start,new_interval.end)
			newI = Interval(start,end)
			print "min_num",min_num,"start",start
			if(start < min_num):
				new.insert(0,newI)
			else:
				new.append(newI)		

		for x in new:
			print x.start, x.end

if __name__ =="__main__":
	all = []
	"""all.append(Interval(1,2))
	all.append(Interval(3,5))
	all.append(Interval(6,7))
	all.append(Interval(8,10))
	all.append(Interval(12,16))

	new_interval = Interval(4,9)"""

	all.append(Interval(3,6))
	all.append(Interval(8,10))

	new_interval = Interval(1,2)

	sln = Solution()
	sln.insert2(all,new_interval)

#[1,2],[3,5],[6,7],[8,10],[12,16]
 #insert and merge [4,9]