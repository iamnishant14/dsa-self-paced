

class LCM:
    def __init__(self,number_one,number_two) -> None:
        self.__number_one=number_one
        self.__number_two=number_two

    def __calculate_gcd(self,number_one,number_two):
        if number_two==0:
            return number_one
        return self.__calculate_gcd(number_two,number_one%number_two)
    
    def calculate_lcm(self):
        """
        Use the logic: a*b=gcd(a,b)*lcm(a,b)
        """
        product_of_numbers=self.__number_one*self.__number_two
        gcd=self.__calculate_gcd(self.__number_one,self.__number_two)
        return int(product_of_numbers/gcd)
    

if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number=input('Enter two numbers to find their LCM\n')
        number_list=number.split(' ')
        numbers_list=list(map(int,number_list))
        lcm=LCM(numbers_list[0],numbers_list[1])
        print(lcm.calculate_lcm())
        tests-=1