print("Covert decimal to binary and vice versa")

answer = []


def Main():
    while True:
        selection = input("Select input: Decimal(D) or Binary(B)")
        if selection == "d" or selection == "D":
            number = int(input("Enter Decimal number: "))
            DecimalToBinary(number)
        elif selection == "b" or selection == "B":
            number = int(input("Enter binary number: "))
            BinaryToDecimal(number)


def DecimalToBinary(number):
    decimalInput = number
    binaryNumbers = [0] * number
    i = 0
    while number > 0:
        binaryNumbers[i] = number % 2
        number = int(number / 2)
        i += 1
    # reverse order
    binaryNumbers.reverse()
    # take out extra zeros
    rawanswer = binaryNumbers[len(binaryNumbers)-i:]
    # convert to string list
    rawanswerSTR = [str(i) for i in rawanswer]
    # join string together and convert to int
    answer = int("".join(rawanswerSTR))

    print(decimalInput, "==", answer)


def BinaryToDecimal(binary):
    binaryInput = binary
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(binaryInput, "==", decimal)


Main()
