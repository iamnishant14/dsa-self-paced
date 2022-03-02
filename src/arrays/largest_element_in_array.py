import sys


class LargestElementInArray:
    def __init__(self, input_array_list):
        self.__input_array = input_array_list

    def find_largest_number(self):
        largest_number = -1 * sys.maxsize
        for number in self.__input_array:
            largest_number = max(number, largest_number)
        return largest_number


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        input_array_str = input('Enter the array of numbers\n').split(' ')
        input_array = list(map(int, input_array_str))
        largest_element = LargestElementInArray(input_array)
        print(largest_element.find_largest_number())
        tests -= 1
