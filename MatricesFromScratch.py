class Matrix:
    # INITIALIZATION OF THE MATRIX OBJECT AS A STRICT 2D PYTHON LIST OF INTEGERS AND FLOATS.
    def __init__(self, array2D):
        if not isinstance(array2D, list) or not array2D:
            raise ValueError("Must be a non-empty 2D Python list.")
        
        row_length = len(array2D[0])
        
        for row in array2D:
            if not isinstance(row, list):
                raise ValueError("Must be a 2D Python list.")
            if len(row) != row_length:
                raise ValueError("All rows must have the same length (must be a uniform matrix).")
                
            for col in row:
                if not isinstance(col, (int, float)):
                    raise ValueError("Must be a 2D Python List of int or float objects.")
                    
        self.viewMatrix=[list(row) for row in array2D]

    # STRING REPRESENTATION OF THE MATRIX OBJECT:
    def __str__(self):
        colWidths=[max([len(row) for row in map(str,col)]) for col in zip(*self.viewMatrix)]

        fixed=[[str(col).rjust(width) for width,col in zip(colWidths,row)] for row in self.viewMatrix]
        final_look="\n".join(["["+("  ".join([col for col in row]))+"]" for row in fixed])
        return final_look

    # TRANSPOSING A MATRIX RETURNS A COMPLETELY NEW TRANSPOSED (INTERCHANGING ROWS AND COLUMNS Ri <---> Ci) MATRIX.
    def transpose(self):
        return Matrix([list(col) for col in zip(*self.viewMatrix)])

    # THE SHAPE METHOD RETURNS THE ORDER OF THE MATRIX STORED IN A TUPLE AS: (row,col)
    def shape(self):
        return (len(self.viewMatrix),len(self.viewMatrix[0]))

    # RETURNS THE TOTAL NUMBER OF ENTRIES IN THE MATRIX OBJECT.
    def totalElements(self):
        row,col=self.shape()
        return row*col

    # LETS THE USER ACCESS ANY ELEMENT OF THE MATRIX OBJECT. A[i,j]--> Returns the number at the i-th row and j-th column.
    def __getitem__(self, key):
        if not isinstance(key, tuple):
            raise TypeError("Requires two arguments.")
        else:
            row,col=key
            return self.viewMatrix[row][col]

    # LETS THE USER OVERWRITE THE VALUE AT THE i-th ROW AND j-th COLUMN, BY REASSIGNING AFTER ACCESSING. 
    # A[i,j]=value
    def __setitem__(self, key, value):
        if not isinstance(key, tuple):
            raise TypeError("Index key must be a tuple: (row, col).")
        if not isinstance(value, (int, float)):
            raise TypeError("Only int or float values can be assigned.")

        row, col = key
        self.viewMatrix[row][col] = value

    # OPERATORS: ADDITION (+), SUBTRACTION (-), MULTIPLICATION (*)--FOR SCALAR AS WELL AS HADAMARD PRODUCT (MULTIPLYING CORRESPONDING ELEMENTS OF TWO MATRICES OF THE SAME ORDER.), MATRIX MULTIPLICATION (@), POWER(**).

    # ADDITION (+): A+B=C, BOTH A AND B MUST BE A MATRIX OBJECT OF THE SAME ORDER/SHAPE.
    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Must be a Matrix object.")
        elif self.shape()!=other.shape():
            raise ValueError("Shape mismatch. Both Matrices must be of the same order.")
        else:
            return Matrix([[x+y for x,y in zip(rowSelf,rowOther)] for rowSelf,rowOther in zip(self.viewMatrix,other.viewMatrix)])

    # SUBTRACTION (-): A-B=C, BOTH A AND B MUST BE A MATRIX OBJECT OF THE SAME ORDER/SHAPE.
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("Must be a Matrix object.")
        elif self.shape()!=other.shape():
            raise ValueError("Shape mismatch. Both Matrices must be of the same order.")
        else:
            return Matrix([[x-y for x,y in zip(rowSelf,rowOther)] for rowSelf,rowOther in zip(self.viewMatrix,other.viewMatrix)])

    # MULTIPLICATION (*): CAN BE USED FOR STANDARD SCALAR MULTIPLICATION OR FOR HADARMARD PRODUCT. FOR HADAMARD PRODUCT BOTH MATRICES MUST BE OF THE SAME ORDER OR SHAPE.
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[x*other for x in row] for row in self.viewMatrix])
        elif isinstance(other,Matrix):
            if self.shape()==other.shape():
                return Matrix([[x*y for x,y in zip(rowSelf,rowOther)] for rowSelf,rowOther in zip(self.viewMatrix,other.viewMatrix)])
            else:
                raise ValueError("Shape mismatch. Both Matrices must be of the same order.")
        else:
            raise ValueError("Cannot perform multiplication. Only for scalar multiplication or hadamard product")

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[x*other for x in row] for row in self.viewMatrix])
        else:
            raise ValueError("Cannot perform multiplication. Only for scalar multiplication.")

    # SCALAR DIVISION (/): ONLY FOR DIVIDING MATRICES BY SCALAR VALUES, IT IS EFFECTIVELY THE SAME AS M*(1/scalar)
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError("Must be a scalar.")
        else:
            return Matrix([[x/scalar for x in row] for row in self.viewMatrix])

    def __mod__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError("Must be a scalar.")
        else:
            return Matrix([[x%scalar for x in row] for row in self.viewMatrix])
    
    def __floordiv__(self, scalar):
        if not isinstance(scalar, (int,float)):
            raise TypeError("Must be a scalar.")
        else:
            return Matrix([[x//scalar for x in row] for row in self.viewMatrix])
        
    # STANDARD MATRIX MULTIPLICATION: A@B=C. THE TOTAL NUMBER OF COLUMNS IN A MUST BE EQUAL TO THE TOTAL NUMBER OF ROWS IN B. THE RESULTING MATRIX C IS OF ORDER: (row_of_A,col_of_B)
    def __matmul__(self, other):
        if isinstance(other,Matrix):
            if self.shape()[1]==other.shape()[0]:
                return Matrix([[sum([x*y for x,y in zip(row,col)]) for col in other.transpose().viewMatrix] for row in self.viewMatrix])
            else:
                raise ValueError("The matrices are non-conformable, since the total number of columns in the first one is not equal to the total number of rows in the second matrix.")
        else:
            raise TypeError("Matmul requires both matrices to be a Matrix object.")

    # POWER (**): REPEATED MULTIPLICATION OF MATRIX.
    def __pow__(self, other):
        if not isinstance(other,int):
            raise TypeError("Power can be whole numbers only.")
        elif self.shape()[0]!=self.shape()[1]:
            raise ValueError("Must be a square matrix.")
        elif other<0:
            raise ValueError("Cannot raise to negative values. Must be a whole number/non-negative Integer: {0,1,2,3,...}")
        else:
            row,col=self.shape()
            identity_matrix=Matrix([[1 if index_row==index_col else 0 for index_col in range(col)] for index_row in range(row)])
            if other==0:
                return identity_matrix
            for _ in range(other):
                identity_matrix=identity_matrix@self
            return identity_matrix

    # MULTIPLYING A by THE SCALAR -1:
    def __neg__(self):
        return self*(-1)

    # CHECKING EQUALITY OF TWO MATRICES:
    def __eq__(self, other):
        if not isinstance(other,Matrix):
            return False
        else:
            return self.viewMatrix==other.viewMatrix

    def getSubmatrix(self, excluded_row, excluded_col):
        subMat=[[]]
        current_row=0
        for index_row,row_element in enumerate(self.viewMatrix):
            if index_row!=excluded_row:
                for index_col,col_element in enumerate(row_element):
                    if index_col!=excluded_col:
                        subMat[current_row].append(col_element)
                current_row+=1
                subMat.append([])
        subMat.pop()
        return Matrix(subMat)

    def getRow(self, row_num):
        return Matrix([self.viewMatrix[row_num]])

    def getCol(self, col_num):
        return Matrix([self.transpose().viewMatrix[col_num]]).transpose()

    def det(self):
        row,col=self.shape()
        if(row!=col):
            raise ValueError("Determinant is defined for square matrices only.")
        else:
            if(row==1):
                return self[0,0]
            elif(row==2):
                return (self[0,0]*self[1,1])-(self[0,1]*self[1,0])
            else:
                Det=0
                for j in range(col):
                    sign=(-1)**j
                    minor=self.getSubmatrix(0,j)
                    Det+=self[0,j]*(sign*(minor.det()))
                return Det   

    def minor(self, element_row, element_col):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            return self.getSubmatrix(element_row,element_col).det()

    def cofactor(self, element_row, element_col):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            return (self.getSubmatrix(element_row,element_col).det())*((-1)**(element_row+element_col))

    def adjoint(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            _cofacMat=[[self.cofactor(i,j) for j in range(col)] for i in range(row)]
            return Matrix(_cofacMat).transpose()

    def inverse(self):
        if self.det()==0:
            raise ValueError("A singular matrix does not have an inverse.")
        else:
            _detCal=self.det()
            _adjCal=self.adjoint()
            return (1/_detCal)*_adjCal

    def isSquare(self):
        row,col=self.shape()
        return row==col

    def isRectangular(self):
        row,col=self.shape()
        return row!=col

    def isDiagonal(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            for i in range(row):
                for j in range(col):
                    if(i!=j):
                        if self[i,j]==0:
                            continue
                        else:
                            return False
            return True
    
    def isScalar(self):
        row,col=self.shape()
        if(row==col):
            value=self[0,0]
            validity=0
            for i in range(row):
                for j in range(col):
                    if (i!=j and self[i,j]==0):
                        continue
                    elif(i==j and self[i,j]==value):
                        validity+=1
                    else:
                        return False
            if validity==row:
                return True
        else:
            return False
            
    def isIdentity(self):
        row,col=self.shape()
        if(row==col):
            value=self[0,0]
            validity=0
            for i in range(row):
                for j in range(col):
                    if (i!=j and self[i,j]==0):
                        continue
                    elif(i==j and self[i,j]==1):
                        validity+=1
                    else:
                        return False
            if validity==row:
                return True
        else:
            return False

    def isNull(self):
        check=self.totalElements()
        validity=0
        for row in self.viewMatrix:
            for col in row:
                if col==0:
                    validity+=1
        if validity==check:
            return True
        else:
            return False

    def isSingular(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            return self.det()==0

    def isNormal(self):
        return self@self.transpose()==self.transpose()@self

    def isOrthogonal(self):
        return self@self.transpose()==Matrix.identityMatrix(self.shape()[0])

    def isUpperTriangular(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            for i in range(row):
                for j in range(col):
                    if i>j:
                        if self[i,j]==0:
                            continue
                        else:
                            return False
            return True

    def isLowerTriangular(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            for i in range(row):
                for j in range(col):
                    if i<j:
                        if self[i,j]==0:
                            continue
                        else:
                            return False
            return True

    def isTriangular(self):
        if self.isUpperTriangular() or self.isLowerTriangular():
            return True
        else:
            return False

    def isRowVector(self):
        return self.shape()[0]==1

    def isColumnVector(self):
        return self.shape()[1]==1

    def isSymmetric(self):
        row,col=self.shape()
        if row==col:
            return self.transpose()==self
        else:
            raise ValueError("Must be a square matrix.")

    def isSkewSymmetric(self):
        row,col=self.shape()
        if row==col:
            return self.transpose()==-self
        else:
            raise ValueError("Must be a square matrix.")

    def isIdempotent(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            return self**2==self

    def isInvolutory(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            return self**2==Matrix.identityMatrix(row)

    def isNilpotent(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Must be a square matrix.")
        else:
            k=1
            while(k<=row):
                if self**k==Matrix.zeros(row):
                    return True
                k+=1
            return False

    def trace(self):
        row,col=self.shape()
        if row!=col:
            raise ValueError("Trace is undefined for rectangular matrices.")
        else:
            return sum([self[i,i] for i in range(row)])

    def rank(self):
        pass

    @classmethod
    def diagonalMatrix(cls,diagonal):
        if isinstance(diagonal,list):
            if all(map(lambda x: isinstance(x,(int,float)),diagonal)):
                return Matrix([[diagonal[i] if i==j else 0 for j in range(len(diagonal))] for i in range(len(diagonal))])
            else:
                raise TypeError("Diagonal elements must be int or floats.")
        else:
            raise TypeError("Must be a 1D Python list.")

    @classmethod
    def scalarMatrix(cls,scalar,n):
        if isinstance(scalar,(int,float)) and isinstance(n,int) and n>0:
            return Matrix([[scalar if i==j else 0 for j in range(n)] for i in range(n)])
        else:
            raise TypeError("Scalar must be an integer or a float, and order must be a natural number.")

    @classmethod
    def identityMatrix(cls,n):
        if isinstance(n,int) and n>0:
            return Matrix([[1 if i==j else 0 for j in range(n)] for i in range(n)])
        else:
            raise TypeError("Order must be a natural number.")

    @classmethod
    def constant(cls,scalar,n):
        if isinstance(scalar,(int,float)) and isinstance(n,int) and n>0:
            return Matrix([[scalar for j in range(n)] for i in range(n)])
        else:
            raise TypeError("Scalar must be an integer or a float, and order must be a natural number.")

    @classmethod
    def zeros(cls,n):
        if isinstance(n,int) and n>0:
            return Matrix([[0 for j in range(n)] for i in range(n)])
        else:
            raise TypeError("Order must be a natural number.")

    @classmethod
    def ones(cls,n):
        if isinstance(n,int) and n>0:
            return Matrix([[1 for j in range(n)] for i in range(n)])
        else:
            raise TypeError("Order must be a natural number.")
