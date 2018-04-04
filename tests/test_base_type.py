from unittest import TestCase

class testList(TestCase):
    def test_list(self):
        nums = list(range(5)) 
        print(nums[-1])     # [4]
        print(nums[:-1])    # [0, 1, 2, 3]
        print(nums[:])      # [0, 1, 2, 3, 4]
        print(nums[1:2])    # [1]
        nums.pop()
        print(nums[:])      # [0, 1, 2, 3]
    
    def test_enumerate(self):
        ''' enumerate() is able to add index to list '''
        animals = ['cat', 'dog', 'monkey']
        for idx, animal in enumerate(animals):
            print('#%d: %s' % (idx, animal))

    def test_set(self):
        nums = list(range(5))
        
        # convert to set
        nums_set = set(nums)
        print(nums_set)    # {0, 1, 2, 3, 4}
        nums_set = {*nums}
        print(nums_set)    # {0, 1, 2, 3, 4}

        # remove duplicate item
        nums.append(2)
        print(nums)
        nums_set = set(nums)  # [0, 1, 2, 3, 4, 2]
        print(nums_set)       # {0, 1, 2, 3, 4}

        # Convert set to list
        nums = list(nums_set)
        print(nums)    # [0, 1, 2, 3, 4]
        nums = {*nums_set}
        print(nums)    # [0, 1, 2, 3, 4]
