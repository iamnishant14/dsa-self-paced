

class GCD:
    def __init__(self,number_one,number_two) -> None:
        self.__number_one=number_one
        self.__number_two=number_two

    def calculate_gcd(self) -> int:
        minimum_number=min(self.__number_one,self.__number_two)
        while minimum_number>0:
            if self.__number_one%minimum_number==0 and self.__number_two%minimum_number==0:
                return minimum_number
            minimum_number-=1

        return minimum_number



if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number=input('Enter two numbers to find their GCD\n')
        number_list=number.split(' ')
        numbers_list=list(map(int,number_list))
        gcd=GCD(numbers_list[0],numbers_list[1])
        print(gcd.calculate_gcd())
        tests-=1