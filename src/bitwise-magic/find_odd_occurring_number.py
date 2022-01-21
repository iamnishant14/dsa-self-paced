
class OddOccurringNumber:
    def __init__(self,number_list) -> None:
        self.__number_list=number_list

    def find_odd_occurring_number(self):
        xor=self.__number_list[0]
        for i in range(1,len(self.__number_list)):
            xor^=self.__number_list[i]
        return xor
    

if __name__=='__main__':
    tests=int(input('Enter number of testcases\n'))
    while tests>0:
        number_list=input('Enter list of space separated number \n').split(' ')
        number_list=list(map(int,number_list))
        odd_occurring_number=OddOccurringNumber(number_list)
        print(odd_occurring_number.find_odd_occurring_number())
        tests-=1