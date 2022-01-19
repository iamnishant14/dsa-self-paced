

class PrimeFactors:

    def __init__(self,number) -> None:
        self.__number=number
        self.__prime_factors=list()

    def calculate_prime_factors(self):
        while self.__number%2==0:
            self.__prime_factors.append(2)
            self.__number=int(self.__number/2)
        while self.__number%3==0:
            self.__prime_factors.append(3)
            self.__number=int(self.__number/3)
        divisor=5
        while divisor*divisor<=self.__number:
            while self.__number%divisor==0:
                self.__prime_factors.append(divisor)
                self.__number=int(self.__number/divisor)
            while self.__number%(divisor+2)==0:
                self.__prime_factors.append(divisor+2)
                self.__number=int(self.__number/(divisor+2)) 
            divisor+=6
        if self.__number>3:
            self.__prime_factors.append(number)
        return self.__prime_factors
    

if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number=int(input('Enter number to find it\'s prime factors\n'))
        prime_factors=PrimeFactors(number)
        print(prime_factors.calculate_prime_factors())
        tests-=1