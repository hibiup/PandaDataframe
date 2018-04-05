from unittest import TestCase

import numpy as np

class testNumpy(TestCase):
    def test_array(self):
        a = np.array([1, 2, 3])
        print(a)

        b = np.array([[1,2,3],[4,5,6]])
        print(b.shape)
        print(type(b))
        print(b.shape)                      # (2, 3)
        print(b[0, 0], b[0, 1], b[1, 0])    # 1 2 4

        # Initiate
        print(np.zeros((2,2)))          # Create an array of all zeros
        print(np.ones((1,2)))           # Create an array of all ones
        print(np.full((2,2), 7))        # Create a constant array wit all 7
        print(np.random.random((2,2)))  # Create an array filled with random values

    def test_nyarray(self):
        ''' Numpy array is pretty line general array'''
        _a = [[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12]]
        print(_a)

        a = np.array([[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12]])
        print(a)

        print(np.arange(4))  # [0 1 2 3]
        print([x for x in range(4)])

    def test_index(self):
        a = np.array([[1,2,3,4],
                      [5,6,7,8],
                      [9,10,11,12]])
        ''' 
         [[2 3]
          [6 7]]
        '''
        b = a[:2, 1:3]
        print(b)

        ''' [5 6 7 8] '''
        print(a[1, :])
        '''
        [[1 2 3 4]
         [5 6 7 8]]
        '''
        print(a[0:2, :])

        print(a[[0, 1, 2]]) # return individual line: 0, 1, 2. which means print all lines
        print(a[[0, 2]])    # return individual line: 0 and 2.

        ''' [ 2 12] '''
        print(a[[0, 2], [1 ,3]])  # return elements: [0,1] and [2, 3]
        ''' [2 2] '''
        print(a[[0, 0], [1, 1]])  # Print [0 ,1] twice.
    
    def test_operation(self):
        a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
        b = np.array([0, 2, 0, 1])
        a[np.arange(4), b] += 10  # add 4 elements at once.
        print(a)

        '''
        [[ True False False]
         [False False  True]
         [ True  True  True]
         [ True  True  True]]
        '''
        bool_idx = (a > 5)   # find number larger then 5 and return boolean
        print(bool_idx)
        ''' [11 16 17  8  9 10 21 12] '''
        print(a[bool_idx])   # return "True" elements, but downgrade to 1 dimension

        print(a[a > 5])      # all put above two lines in one

    def test_calculation(self):
        x = np.array([[1,2],[3,4]], dtype=np.float64)
        y = np.array([[5,6],[7,8]], dtype=np.float64)
        '''
        [[ 6.  8.]
         [10. 12.]]
        '''
        print (x + y)
        '''
        [[1. 3.]
         [2. 4.]]
        '''
        print(x.T)
        '''
        [[-4. -4.]
         [-4. -4.]]
        '''
        print(np.subtract(x, y))

        # matrix operation
        '''
        [[19. 22.]
         [43. 50.]]
        '''
        print(x.dot(y))

        #v = np.array([9,10])
        #w = np.array([11, 12])
        #print(v.dot(w))
        #print(x.dot(v))
        