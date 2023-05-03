import random


def main():

    deck = []
    for i in range(1, 4):
        for j in range(1, 15):
            deck.append(j)

    random.shuffle(deck)  # shuffle deck
    money = 500

    while True:  # game loop start
        print(deck)

        print("Money: ", money, "$")
        if money <= 0:
            print("No money. GG!")
            quit()

        bet = getBet(money)
        print("your Bet:", bet)
        hand = []
        hand.append(getcard(deck))
        hand.append(getcard(deck))
        dealer = []
        dealer.append(getcard(deck))
        printhands(hand, dealer)
        move = getmove()

        if move == "H":  # HIT
            hand.append(getcard(deck))
        dealer.append(getcard(deck))
        printhands(hand, dealer)
        checkhands(hand, dealer)
        move = getmove()
        return  # end


def checkhands(hand, dealer):
    handsum = 0
    dealersum = 0
    for i in range(len(hand)):
        if hand[i] == 14:
            if handsum + 10 > 21:
                handsum + 1
                continue
        handsum += hand[i]
    for i in range(len(dealer)):
        if dealer[i] == 14:
            if dealersum + 10 > 21:
                dealersum + 1
                continue
        dealersum += dealer[i]


def printhands(hand, dealer):
    hand.sort()
    dealer.sort()
    print("Your Hand: ")
    for i in range(len(hand)):
        if hand[i] == 14:
            print("ACE")
            continue
        print(hand[i])
    print("Dealers Hand: ")
    for i in range(len(dealer)):
        if dealer[i] == 14:
            print("ACE")
            continue
        print(dealer[i])


def getcard(deck):
    card = deck[0]
    deck.pop(0)
    return card


def getmove():
    while True:
        print("HIT (H) , Stand (S) , Bust (B)")
        move = input().upper()
        if move == "H":
            return move
        if move == "S":
            return move
        if move == "B":
            return move


def getBet(maxbet):
    while True:
        print(" Enter Bet: 1 -", maxbet)
        bet = input("> ").upper().strip()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if bet <= maxbet:
            return bet


main()
