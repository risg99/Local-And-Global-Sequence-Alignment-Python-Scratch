class ScoreParams:
	'''
	Define scores for each parameter
	'''
	def __init__(self,gap,match,mismatch):
		self.gap = gap
		self.match = match
		self.mismatch = mismatch

def getMatrix(sizeX,sizeY):
	'''
	Create an empty matrix of zeros, such that its len(y) x len(x)
	'''
	matrix = []
	for i in range(len(sizeY)+1):
		subMatrix = []
		for j in range(len(sizeX)+1):
			subMatrix.append(0)
		matrix.append(subMatrix)
	return matrix

def localAlign(x,y,score):
	'''
	Fill in the matrix with alignment scores and obtain the best score and position
	'''
	matrix = getMatrix(x,y)
	best = 0
	optLoc = (0,0)

	for i in range(1,len(y)+1):
		for j in range(1,len(x)+1):
			matrix[i][j] = max(
				matrix[i][j-1] + score.gap,
				matrix[i-1][j] + score.gap,
				matrix[i-1][j-1] + (score.match if x[j-1] == y[i-1] else score.mismatch),
				0
				)

			if matrix[i][j] >= best:
				best = matrix[i][j]
				optLoc = (i,j)

	return best, optLoc, matrix

def printMatrix(matrix):
	'''
	Create a custom function to print the matrix
	'''
	for i in range(len(matrix)):
		print(matrix[i])
	print()

def getSequence(x,best,optLoc,matrix):
	'''
	Obtaining the locally aligned sequence using matrix
	'''
	seq = ''
	i = optLoc[0]
	j = optLoc[1]

	while(i > 0 or j > 0):

		diag = matrix[i-1][j-1]
		up = matrix[i-1][j]
		left = matrix[i][j-1]

		if min(diag,left,up) == diag:
			# Break condition when diag score is the maximum
			break
		else:
			# Adding to the sequence
			i = i - 1
			j = j - 1
			seq += x[j]
	return seq[::-1]

'''
Driver Code:
'''
x = 'bestoftimes'
y = 'soften'
print('Input sequences are: ')
print(x)
print(y)
print()
score = ScoreParams(-7,10,-5)
best, optLoc, matrix = localAlign(x,y,score)

print('Score matrix:')
printMatrix(matrix)

print('The best score obtained is: '+str(best))
print('The best locally aligned sequence is from index '+str(optLoc[0])+' to index '+str(optLoc[1])+' of the string: '+x)
print('The sequence thus obtained: ' + x[optLoc[0]:optLoc[1]])

alignedSequence = getSequence(x,best,optLoc,matrix)
print('The sequence obtained via traceback is: '+ str(alignedSequence))