print 'matrix compute'

class Matrix:
	
	def matrix(self, list1, list2):
		r1 = len(list1)
		r2 = len(list2)
		c1 = len(list1[0])
		c2 = len(list2[0])
		re = []
		result = [[0 for r in range(c2)] for c in range(r1)]
	
		for m in range(len(result)):
			for n in range(len(result[0])):
				for j in range(r2):
					re.append(list1[m][j]*list2[j][n])
					
				result[m][n] =sum(re)
				re = []
		return result

m = Matrix()

l1 = [[1,0,0],[0,1,0],[0,0,1]]
l2 = [[1,2,3],[3,4,6],[3,4,6]]
l3 = [[9], [10], [11]]
print m.matrix(l1,l3)
