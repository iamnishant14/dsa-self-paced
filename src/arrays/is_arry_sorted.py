class IsArraySorted:
    def __init__(self, numbers_list):
        self.__numbers_list = numbers_list

    def check_if_array_is_sorted(self):
        for i in range(1, len(self.__numbers_list)):
            if self.__numbers_list[i] < self.__numbers_list[i - 1]:
                return False
        return True


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        input_array_str = input('Enter the array of numbers\n').split(' ')
        input_array = list(map(int, input_array_str))
        second_largest_element = IsArraySorted(input_array)
        print(second_largest_element.check_if_array_is_sorted())
        tests -= 1
