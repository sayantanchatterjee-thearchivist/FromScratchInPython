class Matrix:
    def __init__(self, array2D):
        self.viewMatrix=array2D
    
    # ACCESSING INDIVIDUAL ELEMENTS USING THE SUBSCRIPT OPERATOR:

    def __getitem__(self, key):
        if isinstance(key, tuple):
            row, col=key
            if isinstance(row,int) and isinstance(col,int):
                return self.viewMatrix[row][col]
            elif isinstance(row, slice) and isinstance(col, slice):
                return Matrix(Matrix(self.viewMatrix[row]).transpose().viewMatrix[col]).transpose()
        elif isinstance(key, slice):
            return Matrix(self.viewMatrix[key])
        else:
            raise ValueError("Requires two arguments")

    # OVERWRITING AN ELEMENT:
    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            row, col=key
            self.viewMatrix[row][col]=value
        else:
            raise ValueError("Requires two arguments")

    # TRANSPOSING THE [EXISTING MATRIX]:
    def transposeMe(self):
        # *list---UNPACKS THE LIST, ZIP FUNCTION THEN ZIPS THE CORRSPONDING ELEMENTS OF ALL THE ROWS WITHIN INTO TUPLES, list(col) THEN FINALLY CONVERTS THE TUPLE INTO A LIST.
        temp=[list(col) for col in zip(*self.viewMatrix)]
        self.viewMatrix.clear()
        self.viewMatrix.extend(temp)
        return self
    
    def transpose(self):

        # *list---UNPACKS THE LIST, ZIP FUNCTION THEN ZIPS THE CORRSPONDING ELEMENTS OF ALL THE ROWS WITHIN INTO TUPLES, list(col) THEN FINALLY CONVERTS THE TUPLE INTO A LIST.
        return Matrix([list(col) for col in zip(*self.viewMatrix)])
    # INTRODUCING A ROW TO THE [EXISTING MATRIX]:

    def appendRow(self, row):

        self.viewMatrix.append(row)
        return self
    # INTRODUCING A COL TO THE [EXISTING MATRIX]:
    def appendCol(self, col):

        self.transposeMe()
        self.viewMatrix.append(col)
        self.transposeMe()
        return self
    # DELETING A ROW FROM THE [EXISTING MATRIX]:
    def popRow(self, row):


        self.viewMatrix.pop(row)
        return self
    # DELETING A COL FROM THE [EXISTING MATRIX]:
    def popCol(self, col):

        self.transposeMe()
        self.viewMatrix.pop(col)
        self.transposeMe()
        return self

    # NEW OBJECT WITH DELETED ROW AND COL:
    def _get_submatrix(self, row,col):

        sub_mat=[]
        current_row=0
        for row_index,row_element in enumerate(self.viewMatrix):
            if(row_index!=row):
                sub_mat.append([])
                for col_index,col_element in enumerate(row_element):
                    if(col_index!=col):
                        sub_mat[current_row].append(col_element)
                    else:
                        continue
                current_row+=1
        return Matrix(sub_mat)


    # SHAPE OF THE MATRIX/ ORDER OF THE MATRIX:
    def shape(self):
        return (len(self.viewMatrix),len(self.transpose().viewMatrix))

    # COUNT TOTAL ELEMENTS IN THE MATRIX:
    def totalElements(self):
        row,col=self.shape()
        return row*col
    
    # REPRESENTATION OF THE MATRIX IN THE TERMINAL:
    def __str__(self):
        return "\n".join(map(str,self.viewMatrix))

    # [OPERATORS]: (+) addition, (-) subtraction, (*) multiplication, (**) power, (@) matrix multiplication:

    # ADDITION (+):
    def __add__(self, other):
        return Matrix([[x+y for x,y in zip(rowSelf,rowOther)] for rowSelf,rowOther in zip(self.viewMatrix,other.viewMatrix)])

    # SUBTRACTION (+):
    def __sub__(self, other):
        return Matrix([[x-y for x,y in zip(rowSelf,rowOther)] for rowSelf,rowOther in zip(self.viewMatrix,other.viewMatrix)])

    # MULTIPLICATION (*):
    def __mul__(self, other):
        # IF SCALAR:
        if (isinstance(other,int) or isinstance(other,float)):
            return Matrix([[element*other for element in row] for row in self.viewMatrix])
        # IF MATRIX:
        elif (isinstance(other,Matrix)):
            return Matrix([[self_element*other_element for self_element,other_element in zip(self_row,other_row)] for self_row,other_row in zip(self.viewMatrix,other.viewMatrix)])
    def __rmul__(self, other):
        # IF SCALAR:
        if (isinstance(other,int) or isinstance(other,float)):
            return Matrix([[element*other for element in row] for row in self.viewMatrix])
        # IF MATRIX:
        elif (isinstance(other,Matrix)):
            return Matrix([[self_element*other_element for self_element,other_element in zip(self_row,other_row)] for self_row,other_row in zip(self.viewMatrix,other.viewMatrix)])

    # MATRIX MULTIPLICATION (@):
    def __matmul__(self, other):
        if isinstance(other, Matrix):
            return Matrix([[sum([x*y for x,y in zip(row,col)]) for col in other.transpose().viewMatrix] for row in self.viewMatrix])
        else:
            raise TypeError("Cannot multiply to a non-matrix")

    # POWER (**):
    def __pow__(self, other):

        if isinstance(other,int):
            row, col=self.shape()
            matrix=Matrix([[(1 if (i==j) else 0) for j in range(col)] for i in range(row)])
            for n in range(other):
                matrix=self@matrix
            return matrix
        else:
            raise TypeError("Must be an integer value")

    # EQUALITY COMPARISON OPERATOR:
    def __eq__(self,other):
        return (True if self.viewMatrix==other.viewMatrix else False)
    
    # MINOR OF AN ELEMENT AT (row, col):
    def minor(self, row, col=None):

        if col is None and isinstance(row, tuple):
            row, col = row
        return self._get_submatrix(row, col).det()

    # COFACTOR OF AN ELEMENT AT (row, col):
    def cofactor(self, row, col):
        return ((-1) ** (row + col)) * self.minor(row, col)

    # DETERMINANT OF A MATRIX:
    def det(self):

        rows, cols = self.shape()
        if rows != cols:
            raise ValueError("Determinant is only defined for square matrices.")
        
        if rows == 1:
            return self.viewMatrix[0][0]
        if rows == 2:
            return self.viewMatrix[0][0] * self.viewMatrix[1][1] - self.viewMatrix[0][1] * self.viewMatrix[1][0]
        
        determinant = 0
        for j in range(cols):
            sign = 1 if j % 2 == 0 else -1
            determinant += sign * self.viewMatrix[0][j] * self._get_submatrix(0, j).det()
            
        return determinant

    # ADJOINT OF A MATRIX:
    def adjoint(self):
        rows, cols = self.shape()
        if rows != cols:
            raise ValueError("Adjoint is only defined for square matrices.")
        if rows == 1:
            return Matrix([[1]])
        cofactor_mat = []
        for i in range(rows):
            cofactor_row = []
            for j in range(cols):
                cofactor_row.append(self.cofactor(i, j))
            cofactor_mat.append(cofactor_row)
        return Matrix(cofactor_mat).transpose()

    # INVERSE OF A MATRIX:
    def inverse(self):
        return ((1/self.det())*(self.adjoint()))

    
    # IS CHECKS:
    # CHECK ORTHOGONAL:
    def isOrthogonal(self):
        row,col=self.shape()
        return (self.transpose()@self==Matrix([[(1 if (i==j) else 0) for j in range(col)] for i in range(row)]))

    # CHECK SINGULAR:
    def isSingular(self):
        return True if self.det()==0 else False

    # CHECK INVERTIBLE:
    def isInvertible(self, tol=1e-9):
        row, col = self.shape()
        if row != col:
            return False
        return abs(self.det()) > tol
