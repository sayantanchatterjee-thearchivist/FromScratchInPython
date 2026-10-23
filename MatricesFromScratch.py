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

    def getSubmatrix(self, excluded_row, excluded_col):
        pass

    def getRow(self, row_num):
        pass

    def getCol(self, col_num):
        pass

    def det(self):
        pass

    def minor(self, element_row, element_col):
        pass

    def cofactor(self, element_row, element_col):
        pass

    def adjoint(self):
        pass

    def inverse(self):
        pass

    def isSquare(self):
        pass

    def isRectangular(self):
        pass

    def isDiagonal(self):
        pass

    def isScalar(self):
        pass

    def isIdentity(self):
        pass

    def isNull(self):
        pass

    def isSingular(self):
        pass

    def isOrthogonal(self):
        pass

    def isUpperTriangular(self):
        pass

    def isLowerTriangular(self):
        pass

    def isTriangular(self):
        pass

    def isRowVector(self):
        pass

    def isColumnVector(self):
        pass

    def isSymmetric(self):
        pass

    def isSkewSymmetric(self):
        pass

    def isIdempotent(self):
        pass

    def isInvolutary(self):
        pass

    def isNilpotent(self):
        pass

    def isNormal(self):
        pass

    def trace(self):
        pass

    def rank(self):
        pass
