def bsearch(arr, a):
	"""
	九章算法模版
	"""
	if not arr: return -1
	l, r = 0, len(arr) - 1

	# exit loop when l + 1 == r, i.e. consecutive
	while l + 1 < r:
		# avoid integer overflow
		m = (r - l) // 2 + l

		if arr[m] == a:
			return m
		elif arr[m] > a:
			# can do r = m - 1
			r = m
		else:
			# can do l = m + 1
			l = m

	# three possible result
	if arr[l] == a:
		# XXOXX
		#   ^^
		return l
	elif arr[r] == a:
		# XXOXX
		#  ^^
		return r
	# XXYY
	#  ^^
	# X < O < Y, insert at index r
	return -1 # not found
