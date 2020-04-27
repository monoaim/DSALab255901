import ctypes

class Array:
    '''Implements the Array ADT with the ctypes module.'''
    
    def __init__(self, size):
        '''
        Creates a one-dimensional array consisting of *size* elements 
        with each element initially set to None. *size* must be greater than zero.
    
        '''        
        assert size > 0, "Array size must be > 0"
        self._size = size
        
        # create the array 
        DSA_ArrayType = ctypes.py_object * size
        self._elements = DSA_ArrayType()
        
        # initialize each element with None
        self.clear(None)
        
    def __len__(self):
        '''
        Returns the length or number of elements in the array.
        '''    
        return self._size
   
    def __getitem__(self, index):
        '''
        Returns the value stored in the array at element position *index*. 
        The *index* argument must be within the valid range. Accessed using the subscript operator.
        '''
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[index]
    
    def __setitem__(self, index, value):
        '''
        Modifies the contents of the array element at position *index* to contain *value*. 
        The index must be within the valid range. Accessed using the subscript operator.
        '''
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[index] = value
    
    def clear(self, value):
        '''
        Clears the array by setting every element to *value*.
        '''
        for i in range(len(self)):
            self._elements[i] = value
    
    def __iter__(self):
        '''
        Returns the array's iterator for traversing the elements.
        '''
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    '''An iterator for the Array ADT.'''
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

class Array2D:
    '''Implements a 2-D array ADT'''
    def __init__(self, nrows, ncols):
        '''
        Creates a two-dimensional array organized into rows and columns. 
        The *nrows* and *ncols* arguments indicate the size of the table. 
        Each element of the table is initialized to *None*.
        '''
        
        # Create a 1-D array to store an array reference for each row.        
        self._theRows = Array( nrows )
        
        # Create the 1-D arrays for each row of the 2-D array.
        for i in range( nrows ):
            self._theRows[i] = Array( ncols )
            
    def numRows(self):
        '''
        Returns the number of rows in the 2-D array.
        '''
        return len( self._theRows )
    
    def numCols(self):
        '''
        Returns the number of columns in the 2-D array.
        '''
        return len( self._theRows[0] )
    
    def clear(self, value):
        '''
        Clears the array by setting every element to *value*.
        '''
        for row in range( self.numRows() ):
            self._theRows[row].clear( value )
            
    def __getitem__(self, ndxTuple):
        '''
        Returns the value stored in the 2-D array at element position indicated by *(r, c)*. 
        Both *r* and *c* must be within the valid range. 
        Accessed using the subscript operator: $y = x[1, 2]$.
        '''
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."
        
        the1dArray = self._theRows[row]
        
        return the1dArray[col]
    
    
    def __setitem__(self, ndxTuple, value):
        '''
        Modifies the contents of the 2-D array element at position indicated by *(r, c)* to contain *value*. 
        The index must be within the valid range. Accessed using the subscript operator: $x[0, 3] = y$.
        '''
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscript out of range."

        the1dArray = self._theRows[row]
        the1dArray[col] = value
        
if __name__=="__main__":
    import random

    # create a 2-D array consisting of 5 rows and 5 columns
    g = Array2D( 5, 5 )

    # fill in the array with random floating-point values.
    for i in range( g.numRows() ):
        for j in range( g.numCols() ):
            g[i, j] = random.random()

    # print the values, one per line.
    for i in range( g.numRows() ):
        for j in range( g.numCols() ):
            print("{0:.4f}\t".format(g[i,j]), end="")
        print()
