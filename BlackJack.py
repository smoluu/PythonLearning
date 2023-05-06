import random
import sys


def main():
    global deck
    deck = []
    money = 1000
    global player
    global dealer

    while True:  # game loop start
        newdeck()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Money: ", money, "$")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if money <= 0:
            sys.exit("No money. GG!")
        while True:
            bet = getBet(money)
            print("your Bet:", bet, "$")
            player = []
            player.append(getcard(deck))
            player.append(getcard(deck))
            dealer = []
            dealer.append(getcard(deck))
            printplayers(player, dealer)
            while True:
                hands = checkplayers(player, dealer)
                if hands[0] < 21 and hands[1] <= 16:
                    getmove()
                else:
                    break

            if checkwincondition() == "win":
                money += bet
                print("YOU WIN!")
                break
            elif checkwincondition() == "lose":
                money -= bet
                print("YOU LOSE!")
                break
            elif checkwincondition() == "push":
                print("PUSH!")
                break


def newdeck():
    for i in range(1, 5):
        for j in range(1, 15):
            deck.append(j)
    random.shuffle(deck)


def checkplayers(player, dealer):
    player.sort()
    dealer.sort()
    playersum = 0
    dealersum = 0
    for i in range(len(player)):
        if player[i] > 10 and player[i] < 14:
            playersum += 10
            continue
        if player[i] == 14:
            if playersum + 11 > 21:
                playersum + 1
                continue
            else:
                playersum += 11
                continue
        if player[i] <= 10:
            playersum += player[i]
    for i in range(len(dealer)):
        if dealer[i] > 10 and dealer[i] < 14:
            dealersum += 10
            continue
        if dealer[i] == 14:
            if dealersum + 11 > 21:
                dealersum + 1
                continue
            else:
                dealersum += 11
                continue
        if dealer[i] <= 10:
            dealersum += dealer[i]

    return [playersum, dealersum]


def checkwincondition():
    result = checkplayers(player, dealer)
    localplayer = result[0]
    localdealer = result[1]
    if (localplayer == 21 and localdealer != 21 or
            localplayer > localdealer and localplayer <= 21 and localdealer < 21 or
            localdealer > 21 and localplayer <= 21):
        return "win"
    elif localdealer == localplayer:
        return "push"
    return "lose"


def printplayers(player, dealer):
    result = checkplayers(player, dealer)
    player.sort()
    dealer.sort()
    print("Player:", end=" ")
    for i in range(len(player)):
        if player[i] == 14:
            print("ACE", end=" ")
            continue
        print(player[i], end=" ")
    print()
    print("Dealer:", end=" ")
    for i in range(len(dealer)):
        if dealer[i] == 14:
            print("ACE", end=" ")
            continue
        print(dealer[i], end=" ")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Player:", result[0], "Dealer:", result[1])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


def getcard(deck):
    card = deck[0]
    deck.pop(0)
    return card


def getmove():
    while True:
        hands = checkplayers(player, dealer)
        print("HIT (H) , Stand (S)")
        move = input().upper()
        if move == "H":
            player.append(getcard(deck))
            # check if to draw for dealer
            if hands[1] < 17:
                dealer.append(getcard(deck))
            printplayers(player, dealer)
            return "H"
        if move == "S":
            # while dealer below 16 draw
            while hands[1] < 17:
                dealer.append(getcard(deck))
                printplayers(player, dealer)
                hands = checkplayers(player, dealer)
            return "S"


def getBet(maxbet):
    while True:
        print(" Enter Bet: 1 -", maxbet)
        bet = input("> ").upper().strip()
        if not bet.isdecimal():
            print("Invalid Bet!")
            continue
        bet = int(bet)
        if bet <= maxbet and bet > 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
            return bet
        else:
            print("Invalid Bet!")


main()
