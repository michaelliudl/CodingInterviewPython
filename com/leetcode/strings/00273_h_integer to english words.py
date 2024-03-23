from typing import List

class Solution:

    def numberToWords(self, num: int) -> str:

        def toWords(num):
            result = []
            hundreds = num // 10 ** 2
            if hundreds > 0:
                result.append(digits[hundreds])
                result.append('Hundred')
                num %= 10 ** 2
            if num > 0:
                if num < 10:
                    result.append(digits[num])
                elif num < 20:
                    result.append(tens[num])
                else:
                    result.append(doubles[num // 10])
                    if num % 10 > 0:
                        result.append(digits[num % 10])
            return ' '.join(result)

        if num == 0:
            return 'Zero'
        digits = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        tens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        doubles = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
        result = []
        billions = num // 10 ** 9
        if billions > 0:
            result.append(toWords(billions))
            result.append('Billion')
            num %= 10 ** 9
        millions = num // 10 ** 6
        if millions > 0:
            result.append(toWords(millions))
            result.append('Million')
            num %= 10 ** 6
        thousands = num // 10 ** 3
        if thousands > 0:
            result.append(toWords(thousands))
            result.append('Thousand')
            num %= 10 ** 3
        if num > 0:
            result.append(toWords(num))
        return ' '.join(result)
            


import unittest

class TestSolution(unittest.TestCase):
    def testNumberToWords(self):
        s = Solution()
        self.assertEqual(s.numberToWords(num = 123), "One Hundred Twenty Three")
        self.assertEqual(s.numberToWords(num = 12345), "Twelve Thousand Three Hundred Forty Five")
        self.assertEqual(s.numberToWords(num = 1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
        

if __name__ == '__main__':
    unittest.main()