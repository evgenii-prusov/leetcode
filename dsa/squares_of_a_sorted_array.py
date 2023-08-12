def squares_of_a_sorted_array(nums: list[int]) -> list[int]:
    sorted_squares: list[int] = list()

    left = 0
    right = len(nums) - 1

    if nums[left] > 0:
        sorted_squares = [x*x for x in nums]
        return sorted_squares

    if nums[right] < 0:
        sorted_squares = [x*x for x in nums[::-1]]
        return sorted_squares

    positive_nums: list[int] = []
    negative_nums: list[int] = []

    while True:
        if nums[left] >= 0:
            negative_nums = nums[0:left][::-1]
            positive_nums = nums[left:len(nums)]
            break
        left += 1
        if nums[right] < 0:
            positive_nums = nums[right+1:len(nums)]
            negative_nums = nums[0: right+1][::-1]
            break
        right -= 1

    negative_pointer = 0
    positive_pointer = 0

    while negative_pointer < len(negative_nums) and positive_pointer < len(positive_nums):
        if abs(negative_nums[negative_pointer]) < abs(positive_nums[positive_pointer]):
            sorted_squares.append(negative_nums[negative_pointer]**2)
            negative_pointer += 1
        else:
            sorted_squares.append(positive_nums[positive_pointer] ** 2)
            positive_pointer += 1

    while negative_pointer < len(negative_nums):
        sorted_squares.append(negative_nums[negative_pointer]**2)
        negative_pointer += 1

    while positive_pointer < len(positive_nums):
        sorted_squares.append(positive_nums[positive_pointer]**2)
        positive_pointer += 1

    return sorted_squares


def test_squares_of_a_sorted_array_1():
    input: list[int] = [-4, -1, 0, 3, 10]
    output: list[int] = [0, 1, 9, 16, 100]
    assert squares_of_a_sorted_array(nums=input) == output


def test_squares_of_a_sorted_array_2():
    input: list[int] = [-7, -3, 2, 3, 11]
    output: list[int] = [4, 9, 9, 49, 121]
    assert squares_of_a_sorted_array(nums=input) == output


def test_squares_of_a_sorted_array_3():
    input: list[int] = [2, 3, 11]
    output: list[int] = [4, 9, 121]
    assert squares_of_a_sorted_array(nums=input) == output


def test_squares_of_a_sorted_array_4():
    input: list[int] = [-9, -7, -7, -2]
    output: list[int] = [4, 49, 49, 81]
    assert squares_of_a_sorted_array(nums=input) == output

def test_squares_of_a_sorted_array_5():
    input: list[int] = [-10000,-9999,-7,-5,0,0,10000]
    output: list[int] = [0,0,25,49,99980001,100000000,100000000]
    assert squares_of_a_sorted_array(nums=input) == output