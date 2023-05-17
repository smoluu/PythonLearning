global answer
answer = True

dateinput = input("Enter a date: (DDMMYYYY)")

if (len(dateinput) != 8):
    answer = False
datelist = []
for letter in dateinput:
    datelist.append(letter)
dd = int("".join(datelist[:2]))
mm = int("".join(datelist[2:4]))
yyyy = int("".join(datelist[4:8]))
match mm:
    case 1:
        if dd not in range(1, 31+1):
            answer = False
    case 2:
        # leap year check
        if yyyy % 400 == 0 and yyyy % 100 == 0:
            if dd not in range(1, 29+1):
                answer = False
        # leap year check
        elif yyyy % 4 == 0 and yyyy % 100 != 0:
            if dd not in range(1, 29+1):
                answer = False
        elif dd not in range(1, 28+1):
            answer = False
    case 3:
        if dd not in range(1, 31+1):
            answer = False
    case 4:
        if dd not in range(1, 30+1):
            answer = False
    case 5:
        if dd not in range(1, 31+1):
            answer = False
    case 6:
        if dd not in range(1, 30+1):
            answer = False
    case 7:
        if dd not in range(1, 31+1):
            answer = False
    case 8:
        if dd not in range(1, 31+1):
            answer = False
    case 9:
        if dd not in range(1, 30+1):
            answer = False
    case 10:
        if dd not in range(1, 31+1):
            answer = False
    case 11:
        if dd not in range(1, 30+1):
            answer = False
    case 12:
        if dd not in range(1, 31+1):
            answer = False
    case other:
        answer = False

print(dd, mm, yyyy)
print(answer)
