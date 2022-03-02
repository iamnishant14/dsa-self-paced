class SumOfDigits:
    def __init__(self, number):
        self.__number = number

    def __sum_of_digits(self):
        if self.__number < 10:
            return self.__number
        rightmost_digit = self.__number % 10
        self.__number = self.__number // 10
        return self.__sum_of_digits() + rightmost_digit

    def calculate_sum_of_digits(self):
        return self.__sum_of_digits()


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        input_number = int(input('Enter the number\n'))
        sum_of_digits = SumOfDigits(input_number)
        print(sum_of_digits.calculate_sum_of_digits())
        tests -= 1
