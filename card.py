import random
cardtype = ["♠", "◆", "♥", "♣"]
cardrank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def shuffle_deck():
    cards = []
    for type in cardtype:
        for rank in cardrank:
            cards.append(f"{type} {rank}")
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
                print(f"축하합니다! {picked_card} 을 뽑는데에 성공하셨군요!\n이 카드를 뽑기까지 {attempt}번을 시도했습니다.")
                break

        elif choice == "2":
            print("게임을 종료합니다.")
            break

        else :
            print("잘못된 입력입니다.")

def showhelp():
    print("\n" + "="*40)
    print("         카드 뽑기 게임 도움말")
    print("="*40)
    print("1. 기본 카드 뽑기")
    print("   - 52장의 카드 덱에서 무작위로 카드를 한 장씩 뽑습니다.")
    print("   - 카드를 뽑을 때마다 남은 카드 수가 줄어듭니다.")
    print("   - 모든 카드를 소진하거나 종료를 원할 때 끝낼 수 있습니다.")
    print("")
    print("2. 특정 카드 뽑기")
    print("   - 컴퓨터가 52장 중 하나의 목표 카드를 지정합니다.")
    print("   - 여러분은 목표 카드가 나올 때까지 카드를 계속 뽑아야 합니다.")
    print("   - 과연 몇 번 만에 원하는 카드를 뽑을 수 있을지 운을 시험해보세요!")
    print("="*40 + "\n")

while True:
    gamemode = input("1.기본 카드 뽑기 | 2.특정 카드 뽑기 | 3.도움말 | 4.프로그램 종료 : ")
    if gamemode == "1":
        main()
    elif gamemode == "2":
        lucktest()
    elif gamemode == "3":
        showhelp()
    elif gamemode == "4":
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못된 입력입니다.")