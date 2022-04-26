class SecondLargestElementInArray:
    def __init__(self, array_list):
        self.__numbers_list = array_list

    def find_second_largest_number(self):
        largest, second_largest = 0, -1
        for i in range(len(self.__numbers_list)):
            if self.__numbers_list[i] > self.__numbers_list[largest]:
                second_largest = largest
                largest = i
            elif self.__numbers_list[i]!=self.__numbers_list[largest]:
                if second_largest == -1 or self.__numbers_list[i] > self.__numbers_list[second_largest]:
                    second_largest = i
        if second_largest == -1:
            return -1
        return self.__numbers_list[second_largest]


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        input_array_str = input('Enter the array of numbers\n').split(' ')
        input_array = list(map(int, input_array_str))
        second_largest_element = SecondLargestElementInArray(input_array)
        print(second_largest_element.find_second_largest_number())
        tests -= 1
