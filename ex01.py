class Solution:
    def __init__(self, usenum):
        self.num = usenum

    def romanToInt(self) -> int:
        dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        answer = 0
        past = 'I'
        for current in self.num[::-1]: 
            answer = answer - dictionary[current] if dictionary[current] < dictionary[past] else answer + dictionary[current]
            past = current

        return answer
  
    def intToRoman(self) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while int(self.num) > 0:  # self.num을 정수로 변환하여 비교
            if int(self.num) >= val[i]:  # self.num을 정수로 변환하여 비교
                roman_num += syb[i]
                self.num = str(int(self.num) - val[i])  # self.num을 정수로 변환하여 뺀 후 다시 문자열로 변환
            else:
                i += 1
        return roman_num


number = input('정수 또는 로마숫자를 입력하세요: ')
sol = Solution(number)

if number.isdigit():
    number = int(number)
    print(f'입력한 정수 {number}는(은) 로마 숫자로 {sol.intToRoman()} 입니다.')
else:
    print(f'입력한 로마 숫자 {number}는(은) 정수 값으로 {sol.romanToInt()} 입니다.')
