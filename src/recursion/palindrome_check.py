class PalindromeCheck:
    def __init__(self, word):
        self.__word = word

    def __is_palindrome(self, start, end):
        if start >= end:
            return True
        return self.__word[start] == self.__word[end] and self.__is_palindrome(start + 1, end - 1)

    def palindrome_checker(self):
        start, end = 0, len(self.__word) - 1
        return self.__is_palindrome(start, end)


if __name__ == '__main__':
    tests = int(input('Enter number of testcases\n'))
    while tests > 0:
        word = input('Enter word to find if it\'s a palindrome or not\n')
        palindrome_checker = PalindromeCheck(word)
        print(palindrome_checker.palindrome_checker())
        tests -= 1
