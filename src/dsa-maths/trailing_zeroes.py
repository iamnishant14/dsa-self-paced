class TrailingZeroes:
    def __init__(self, number) -> None:
        self.__number = number

    def count_trailing_zeroes(self):
        factorial = 1
        for i in range(2, self.__number + 1):
            factorial *= i
        count = 0
        while factorial % 10 == 0:
            count += 1
            factorial /= 10

        """
        Trailing zeroes are made by number of 5's and 2's in the prime factorization of number.
        So we can count number of 5's since it's way less than number of 2's.
        So we can use number of 5's , 25's ,125's and so on till the number is greater than next iteration of 5,25,125,625 and so on.
        """
        count, i = 0, 5
        while i <= self.__number:
            count += int(self.__number / i)
            i *= 5
        return count


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        number = int(input('Enter number to find trailing zeroes in it\'s factorial\n'))
        trailing_zeroes = TrailingZeroes(number)
        print(trailing_zeroes.count_trailing_zeroes())
        tests -= 1
