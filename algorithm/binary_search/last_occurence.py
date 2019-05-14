def findLast(arr, a):
	"""
	To understand the advantage of `l + 1 < r`, consider edge case [2, 2].
	If using `l < r` as condition, it leads to infinite loop (convince yourself).

	Can combine two conditions: `arr[m] <= a`
	"""
	if not arr: return -1
	l, r = 0, len(arr) - 1

	while l + 1 < r:
		m = (r - l) // 2 + l

		if arr[m] == a:
			# cannot do l = m + 1, because
			# m could be the last occurrence
			# out-of-bound error also possible
			l = m
		elif arr[m] > a:
			# can do r = m - 1
			r = m
		else:
			# can do l = m + 1
			l = m

	# three possible result
	if arr[r] == a:
		# XXOO
		# ^^
		return r
	elif arr[l] == a:
		# XXOO
		#  ^^
		return l
	return -1 # not found
