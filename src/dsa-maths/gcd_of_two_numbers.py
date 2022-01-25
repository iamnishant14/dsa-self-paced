class GCD:
    def __init__(self, number_one, number_two) -> None:
        self.__number_one = number_one
        self.__number_two = number_two

    def gcd_optimised(self, number_one, number_two) -> int:
        if number_two == 0:
            return number_one
        return self.gcd_optimised(number_two, number_one % number_two)

    def calculate_gcd(self, optimised=False):
        if optimised:
            """
            Finding GCD of two numbers is based on eucledian algorithms , where GCD(a,b)=GCD(a-b.b) if a>b
            Then by same logic , instead of decrement we use the modular division where we check if the modular division of second argument 
            is zero or not , if not then use the current call's second argument as first of next call and find first % second to pass as second argument.
            as the first argument is always greater than second argument.
            We will only find the gcd of two numbers , if second args in current call is zero else some remainder is left.
            """
            minimum_number = self.gcd_optimised(self.__number_one, self.__number_two)
            return minimum_number
        else:
            return self.gcd_naive()

    def gcd_naive(self) -> int:
        minimum_number = min(self.__number_one, self.__number_two)
        while minimum_number > 0:
            if self.__number_one % minimum_number == 0 and self.__number_two % minimum_number == 0:
                return minimum_number
            minimum_number -= 1
        return minimum_number


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        number = input('Enter two numbers to find their GCD\n')
        number_list = number.split(' ')
        numbers_list = list(map(int, number_list))
        gcd = GCD(numbers_list[0], numbers_list[1])
        print(gcd.calculate_gcd(optimised=True))
        tests -= 1
