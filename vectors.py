class Matrix:
	"""docstring for Matrix
		row next columns
	"""
	def __init__(self,row =0,column=0,matrix = None):
		if(matrix == None):
			self.matrix = []
			self.columns_size =0
			self.row_size = 0
		else:
			self.matrix = matrix
			self.columns_size =row
			self.row_size = column

		

	def fillMatrix(self,*args):
		self.row_size = len(args)
		self.columns_size = len(args[0])
		for enum,arg in enumerate(args):
			 #print(arg, end=" ")
			 #print(enum)
			 self.matrix.append(arg)

	
	def get_rc(self,r,c):
		return self.matrix[r][c]
	def get_matrix(self):
		return self.matrix
	
	def zeros(self,row_size,columns_size):
		self.matrix = []
		self.row_size = row_size
		columns_size = columns_size
		i,j = 0,0
		zer = []
		while(i<columns_size):
			zer.append(0)
			i+=1
		while(j<row_size):	
			self.matrix.append(zer)
			j+=1


	def _get_column(self,x):
		tmp = []
		for r in self.matrix:
			tmp.append(r[x])
		return tmp

	def __add__(self,other):
		tmp = []
		for e1,row in enumerate(self.matrix):
			tmp.append([])
			for e2,x in enumerate(row):
				tmp[e1].append(x + other.get_rc(e1,e2))
		return Matrix(self.row_size,self.columns_size,tmp)

	def __sub__(self,other):
		tmp = []
		for e1,row in enumerate(self.matrix):
			tmp.append([])
			for e2,x in enumerate(row):
				tmp[e1].append(x - other.get_rc(e1,e2))
		return Matrix(self.row_size,self.columns_size,tmp)
	
	def __mul__(self,other):
		tmp = []
		for e1,row in enumerate(self.matrix):
			rc = 0
			c = 0
			tmp_r =[]
			while (c<other.columns_size):
				for e2,col in enumerate(other._get_column(c)):
					#print(row[e2] , end= " ")
					#print(col)
					rc += row[e2]* col 
				tmp_r.append(rc)
				c+=1
			tmp.append(tmp_r)

		return Matrix(other.columns_size,self.row_size,tmp) 

				
	def __str__(self):
		matrix_string =""
		for row in self.matrix:
			matrix_string += "\n"
			for x in row:
				matrix_string = matrix_string + "  " + str(x)
		return matrix_string


makeMatrix = Matrix()
mM = Matrix()
makeMatrix.fillMatrix([1,2,3],[4,5,6],[7,8,9])
mM.fillMatrix([1],[4],[1])
print(makeMatrix)
print(mM)

#print(mM - makeMatrix)

makeZeros = Matrix()
makeZeros.zeros(3,3)
print(makeZeros)
x = makeMatrix *mM
print(x)
print(x.row_size)
print(x.columns_size)


x = Matrix()
y = Matrix()

x.fillMatrix([1,1,2])
y.fillMatrix([0,1,0])

print(y+x)
print(x+y)

print(y-x)
print(x-y)

z = Matrix()
z.fillMatrix([1],[0],[2])
print(z*x)
print(x*z) 
		