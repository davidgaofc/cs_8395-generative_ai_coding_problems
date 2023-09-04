from problems.problem_20 import MergeSort

def test_merge_sort():
    merge_sorter = MergeSort()
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sorter.merge_sort(arr)
    assert sorted_arr == [3, 9, 10, 27, 38, 43, 82]