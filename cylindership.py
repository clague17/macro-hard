import math

with open("PracticeInput-2.txt", "r") as f:
	matrix = []
	for line in f.readlines():
		# print line
		line = line[:-2]
		row = []
		# line.split()
		# print 'line:', line
		for char in line.split(","):
			row.append(int(char))
		matrix.append(row)
# print matrix

def calc_boxes(matrix):
	'''
	Input: a list of lists
	Output: an integer: the number of boxes that fit in the area
	'''
	cylheight = 13
	height = 12

	total_boxes = 0
	cap = matrix[0][0]
	matrix = matrix[1:]
	# while counter <= cap:
	# 	print counter
	#print matrix
	for case in matrix:
		#calculate max vol
		#calculate vol of rects
		#calculate vol of triangle
		#Add and see if it fits
		max_vol = math.pi*(case[0]**2)
		if case[1] == 3:
			# print 'ITS A TRI'
			#its a triangular prism
			volume = .25*((case[2])**2)*math.sqrt(3)
			print 'max_vol', max_vol
			if (max_vol - volume) >= 0:
				# print 'max_vol', max_vol
				# print 'volume', volume
				#max_vol -= volume
				total_boxes += 1
				# print boxes
		elif case[1] == 4:
			# print 'ITS A RECT'
			#Its a rectangular prism
			volume = (case[2]**2)*height
			print 'max_vol', max_vol
			if (max_vol - volume) >= 0:
				# print 'max_vol', max_vol
				# print 'volume', volume
				#max_vol -= volume
				total_boxes += 1
				# print boxes
	# max_boxes = max(max_boxes, boxes)
	# counter += 
	return total_boxes

print calc_boxes(matrix)

#for the practice input, the output should be 4915


