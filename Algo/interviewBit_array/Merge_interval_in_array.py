start = newInterval.start
		end = newInterval.end
		right = left = 0
		while right < len(intervals):
			if start <= intervals[right].end:
				if end < intervals[right].start:
					break
				start = min(start, intervals[right].start)
				end = max(end, intervals[right].end)
			else:
				left += 1
			right += 1
		return intervals[:left] + [Interval(start, end)] + intervals[right:]