

# f = open("PracticeInput-1.txt","r")

with open("PracticeInput-1.txt", "r") as f:
	matrix = []
	for line in f.readlines():
		print line
		row = []
		# line.split()
		print 'line:', type(line)
		for char in line.split():
			row.append(int(char))
		matrix.append(row)

def Transpose(matrix):
    res = [[0] * len(matrix) for i in range(len(matrix[0]))]

    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            res[i][j] = matrix[j][i]

    return res

mat = Transpose(matrix)

MATRIX = ""
for row in mat:
	for element in row:
		MATRIX += str(element) + ' '
	MATRIX += '\n'
print MATRIX


# print Transpose(matrix)



