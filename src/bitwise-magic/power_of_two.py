class PowerOfTwo:

    def __init__(self,number) -> None:
        self.__number=number

    def is_power_of_two(self):
        number=self.__number
        if number==0:
            return False
        return bool(not (number&(number-1)))


if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number=int(input('Enter number find if it\'s power of 2 or not\n'))
        power_of_two=PowerOfTwo(number)
        print(power_of_two.is_power_of_two())
        tests-=1


