import random, sys

# 상수 설정:
HEARTS = chr(9829)
DIAMONDS = chr(9830)
CLUBS = chr(9827)
SPADES = chr(9824)
BACKSIDE = "backside"


def main():
    print(
        """ blackjack
          
    규칙:
        Try to get as close to 21 as possible without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 throught 10 are worth their face value.
        (H) it to take another card. 
        (S)tand to keep your current hand.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17."""
    )

    money = 5000
    while True:  # 메인 게임 루프.
        # 플레이어가 돈을 다 썼는지 검사:
        if money <= 0:
            print("너 돈 다 썼어. 게임 끝!")
            sys.exit()

        # 이번 판에 얼마를 베팅할 것인지 입력하게 한다:
        print("Money:", money)
        bet = getBet(money)

        # 딜러와 플레이어에게 두 장의 카드를 준다:
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # 플레이어의 동작을 처리한다:
        print("Bet:", bet)
        while True:  # 플레이어가 stand 또는 bust할 때까지 반복한다.
            displayHands(playerHand, dealerHand, False)
            print()

            # 플레이어의 bust되었는지 검사:
            if getHandValue(playerHand) > 21:
                break
            # 플레이어의 동작(H, S, D)을 입력받는다:
            move = getMove(playerHand, money - bet)

            # 플레이어의 동작을 처리한다:
            if move == "D":
                # 플레이어가 double down을 선택했을 때:
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)

            if move in ("H", "D"):
                # Hit 또는 double down이면 다른 카드를 하나 받는다.
                newCard = deck.pop()
                rank, suit = newCard
                print("you drew the {} of {}.".format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # 플레이어가 bust됨:
                    continue
            if move in ("S", "D"):
                # Stand 또는 double down이면 플레이어의 차례가 끝남:
                break

        # 딜러의 동작을 처리한다:
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # 딜러가 hit 함:
                print("Dealer hits.")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # 딜러가 bust됨:
                input("Press Enter to continue...")
                print("\n\n")

        # 들고 있던 패를 공개한다:
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # 플레이어가 이겼는지, 졌는지, 아니면 비겼는지 처리함:
        if dealerValue > 21:
            print("Dealer busts! You win ${}.".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lose ${}.".format(bet))
            money -= bet
        elif playerValue > dealerValue:
            print("You win ${}.".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie! Your bet of ${} is returned.")

        input("Press Enter to continue...")
        print("\n\n")


def getBet(maxBet):
    """플레이어가 베팅할 금액을 입력받는다."""
    while True:  # 유효값을 입력받을 때까지 반복한다.
        print("How much do you want to bet? (1-{}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Goodbye!")
            sys.exit()
        if not bet.isdecimal():
            continue  # 플레이어가 숫자를 입력하지 않았다면 다시 물어본다.

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # 플레이어가 유효한 베팅을 입력


def getDeck():
    """52장의 모든 카드에 대한 (rank, suit) 튜플 리스트를 반환한다."""
    deck = []
    for suit in (HEARTS, DIAMONDS, CLUBS, SPADES):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # 숫자로 된 카드를 추가한다.
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))  # 문자로 된 카드를 추가한다.
    random.shuffle(deck)  # 카드를 섞는다.
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """플레이어와 딜러의 패를 출력한다.
    만약에 showDealerHand가 False이면, 딜러의 첫 번째 카드를 가린다."""
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        # 딜러의 첫 번째 카드를 가린다.:
        displayCards([BACKSIDE] + dealerHand[1:])

    # 플레이어의 패를 출력한다:
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """카드의 값을 반환한다. 얼굴이 있는 카드들은 모두 10이며, 에이스는 11 또는 1이다."""
    value = 0
    numberOfAces = 0

    # 에이스가 아닌 나머지 카드들에 값을 추가한다.:
    for card in cards:
        rank = card[0]  # cards는 (rank, suit) 튜플의 리스트이다.
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):  # 문자 카드는 10을 더한다.
            value += 10
        else:  # 숫자 카드는 숫자만큼 더한다.
            value += int(rank)

    # 에이스의 값을 추가한다.:
    value += numberOfAces  # 에이스는 1로 계산한다.
    for i in range(numberOfAces):
        # 에이스가 11이 되어도 21을 넘지 않는다면 11로 계산한다.
        if value + 10 <= 21:
            value += 10

    return value  # 카드의 총 값을 반환한다.


def displayCards(cards):
    """카드의 리스트를 출력한다."""
    rows = ["", "", "", "", ""]  # 카드의 각 행을 저장할 리스트.

    for i, card in enumerate(cards):
        if card == BACKSIDE:
            # 카드의 뒷면을 출력한다:
            rows[0] += "┌─────────┐ "
            rows[1] += "│░░░░░░░░░│ "
            rows[2] += "│░░░░░░░░░│ "
            rows[3] += "│░░░░░░░░░│ "
            rows[4] += "└─────────┘ "
        else:
            rank, suit = card
            # 카드의 앞면을 출력한다: card는 튜플구조이다!
            rows[0] += "┌─────────┐ "
            rows[1] += "│{}       │ ".format(rank.ljust(2))
            rows[2] += "│    {}    │ ".format(suit)
            rows[3] += "│       {} │ ".format(rank.rjust(2))
            rows[4] += "└─────────┘ "

    # 각 행을 출력한다:
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """플레이어의 동작(H, S, D)을 입력받는다. H는 히트, S는 스탠드, D는 더블다운을 의미한다."""
    while True:  # 유효값을 입력받을 때까지 반복한다.
        moves = ["(H)it", "(S)tand"]

        # 플레이어가 최초에 받은 카드 두 장이 서로 같다면, double down을 선택할 수 있다:
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # 플레이어의 선택을 받는다:
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move  # 플레이어가 유효한 동작을 입력
        if move == "D" and "(D)ouble down" in moves:
            return move


# 이 프로그램이 다른 프로그램에 임포트된게 아니라면 게임이 시작된다:
if __name__ == "__main__":
    main()
