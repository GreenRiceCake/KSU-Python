import random
cardtyp = ["♠", "◆", "♥", "♣"]
cardrnk = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def shuffle_deck():
    cards = []
    for typ in cardtyp:
        for rnk in cardrnk:
            cards.append(f"{typ} {rnk}")
    random.shuffle(cards)
    return cards

def main():
    print("카드 뽑기 게임")
    deck = shuffle_deck()
    while True:
        print(f"남은 카드 {len(deck)}")
        choice = input("1. 카드 뽑기 | 2. 게임 종료 : ")
        if choice == "1":
            if len(deck) == 0:
                print("카드를 모두 뽑았습니다! 게임을 종료합니다.")
                break

            picked_card = deck.pop()
            print(f"당신이 뽑은 카드는 {picked_card} 입니다.")

        elif choice == "2":
            print("게임을 종료합니다.")
            break

        else :
            print("잘못된 입력입니다.")

def lucktest():
    print("특정 카드 뽑기 게임")
    attempt = 0
    deck = shuffle_deck()
    rand_choice = random.choice(deck)
    print(f"뽑아야 하는 카드는 {rand_choice} 입니다!")
    while True:
        print(f"남은 카드 {len(deck)}")
        choice = input("1. 카드 뽑기 | 2. 게임 종료 : ")
        if choice == "1":
            attempt += 1
            picked_card = deck.pop()
            print(f"당신이 뽑은 카드는 {picked_card} 입니다.")
            if rand_choice == picked_card:
                print(f"축하합니다! {picked_card} 를 뽑는데에 성공하셨군요!\n이 카드를 뽑기까지 {attempt}번을 시도했습니다.")
                break

        elif choice == "2":
            print("게임을 종료합니다.")
            break

        else :
            print("잘못된 입력입니다.")

while True:
    gamemode = input("1.기본 카드 뽑기 | 2.특정 카드 뽑기 | 3.프로그램 종료 : ")
    if gamemode == "1":
        main()
    elif gamemode == "2":
        lucktest()
    elif gamemode == "3":
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못된 입력입니다.")