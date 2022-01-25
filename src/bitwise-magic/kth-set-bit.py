class KthSetBit:

    def __init__(self, number, k) -> None:
        self.__number = number
        self.__k = k

    def check_kth_set_bit(self):
        return bool((self.__number >> (self.__k)) & 1)


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        inputs = input('Enter number and k to find if it\'s kth bit set or not\n')
        number, k = inputs.split(' ', 1)
        kth_set_bit = KthSetBit(int(number), int(k))
        print(kth_set_bit.check_kth_set_bit())
        tests -= 1
