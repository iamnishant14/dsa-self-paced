class Prime:

    def __init__(self, number) -> None:
        self.__number = number

    def is_prime(self):
        if self.__number == 1:
            return False
        if self.__number == 2 or self.__number == 3:
            return True
        if self.__number % 2 == 0 or self.__number % 3 == 0:
            return False
        divisor = 5
        while divisor * divisor <= self.__number:
            if self.__number % divisor == 0:
                return False
            divisor += 6
        return True


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        number = int(input('Enter number to find if it\'s prime\n'))
        prime = Prime(number)
        print(prime.is_prime())
        tests -= 1
