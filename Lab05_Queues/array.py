# Listing 2.2

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
            