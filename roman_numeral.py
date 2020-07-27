class RomanNumeral:
    def int_to_Roman(self, num):
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
        while num > 0:
            print(range(num // val[i]))
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


if __name__ == '__main__':
    number = int(input('Enter a number to be converted to Roman Numeral\n'))
    roman_number = RomanNumeral()
    print(roman_number.int_to_Roman(number))
