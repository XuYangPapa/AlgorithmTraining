class No9:

    def isPalindrome_str(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        str_x = str(x)
        # 切片反转
        # reversed_str_x = str_x[::-1]
        # reversed方法反转
        reversed_str_x = ''.join(reversed(str_x))
        if str_x == reversed_str_x:
            return True
        else:
            return False

    def isPalindrome(self, x: int) -> bool:
        """
        反转一半数字以后进行对比
        注意x==0的判断要放在x%10=0前面，注意判断数字长度为奇数的情况
        """
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        reversed_x = 0
        while reversed_x < x:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10
        if x == reversed_x or x == reversed_x // 10:
            return True
        else:
            return False


if __name__ == '__main__':
    no9 = No9()
    print(no9.isPalindrome(12181))
