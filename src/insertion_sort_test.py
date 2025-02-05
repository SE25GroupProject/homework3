"""Testing the insertion_sort method"""
from insertion_sort import insertion_sort

class TestInsertionSort:
    """Test Class For Insertion Sort"""
    def test_one_element_array(self):
        """Testing with an array that only has 1 element"""
        arr = [1]
        assert insertion_sort(arr) == [1]

    def test_element_already_sorted(self):
        """Testing with an array that is already sorted"""
        arr = [1,2,3,4]
        assert insertion_sort(arr) == arr

    def test_elements_reverse_order(self):
        """Testing with an array that is in reverse order"""
        arr = [4,3,2,1]
        assert insertion_sort(arr) == [1,2,3,4]

    def test_elements_random_order(self):
        """Testing with an array that is in random order"""
        arr = [2,4,1,3]
        assert insertion_sort(arr) == [1,2,3,4]
