from loguru import logger
from time import time


class CountSetBits:
    def __init__(self, number) -> None:
        self.__number = number

    def count_set_bits_naive(self):
        count = 0
        number = self.__number
        while number > 0:
            count += number & 1
            number >>= 1
        return count

    def count_set_bits_brian(self):
        """
        It uses the logic where if 0....1000 is the number , then number -1 = 0....0111 and & of both will return 0....0000.
        Which will only runs for set bits.
        """
        count, number = 0, self.__number
        while number > 0:
            number = number & (number - 1)
            count += 1
        return count


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        number = int(input('Enter number to find it\'s count of set-bit \n'))
        count_set_bits = CountSetBits(number)
        logger.info('Naive algo started')
        start = time()
        print(count_set_bits.count_set_bits_naive())
        logger.info('Naive algo ended in {}'.format(time() - start))
        logger.info('Brian Algo started')
        start = time()
        print(count_set_bits.count_set_bits_brian())
        logger.info('Brian Algo ended in {}'.format(time() - start))
        tests -= 1
