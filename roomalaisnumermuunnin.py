romans = ["I", "IV", "V", "IX", "X", "XL",
          "L", "XC", "C", "CD", "D", "CM", "M"]
nums = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]

print("Convert arabic numbers to roman & vice versa")


def Main():
    while True:
        selection = input("Select input: Arabic(A) or Romans(R)")
        if selection == "a" or selection == "A":
            number = int(input("Enter arabic number: "))
            ArabicToRoman(number)
        elif selection == "r" or selection == "R":
            roman = input("Enter roman number: ").upper()
            RomanToArabic(roman)


def ArabicToRoman(number):
    i = 12
    while number:
        divider = number // nums[i]
        number %= nums[i]

        while divider:
            print(romans[i], end="")
            divider -= 1
        i -= 1
    print("")


def RomanToArabic(string):
    res = 0
    i = 0
    while (i < len(string)):
        # Getting value of symbol s[i]
        s1 = value(string[i])
        if (i + 1 < len(string)):
            # Getting value of symbol s[i + 1]
            s2 = value(string[i + 1])
            # Comparing both values
            if (s1 >= s2):
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    print(res)


def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1


Main()
