


class TrailingZeroes:
    def __init__(self,number) -> None:
        self.__number=number

    def count_trailing_zeroes(self):
        factorial=1
        for i in range(2,self.__number+1):
            factorial*=i
        count=0
        while factorial%10==0:
            count+=1
            factorial/=10
        return count



if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number=int(input('Enter number to find trailing zeroes in it\'s factorial\n'))
        trailing_zeroes=TrailingZeroes(number)
        print(trailing_zeroes.count_trailing_zeroes())
        tests-=1
