import random
def building_deck(ranks,suits,deck):
    count = 1
    for rank in ranks:
        for suit in suits:
            card = (rank, suit, count)
            count += 1
            deck.append(card)
    random.shuffle(deck)

def a_check(card):
    if card[0] == 'A':
        return True
    else:
        return False

def value_adder(hand,value):
    value = 0
    for card in hand:
        if card[0] == 'A':
            value += 11
            if value > 21:
                value -= 10
                continue
            else:
                continue
        elif card[0] == 'A' and value > 21:
            value -= 11
            value += 1
            continue
        elif card[0] == 'J' or card[0] == 'Q' or card[0] == 'K':
            value += 10
            continue
        else:
            temp_value = card[0]
            value += temp_value
            continue
    return value

def print_hand(hand,value,player):
    print(f'{player} hand:')
    for card in hand:
        print(f"""{'_'*10}\n|{card[0]:>2} of {card[1]:<2}|\n{'\u203E'*10}""")
    print(f'{value:>2} = Total\n')

def dealer_move(dhand,dvalue,deck,value):
    player = 'dealer'
    while True:
        if dvalue > 21:
            print_hand(dhand,dvalue,player)
            print("Dealer bust")
            break
        elif dvalue == 21:
            print_hand(dhand,dvalue,player)
            print("Dealer Wins!")
            break
        elif dvalue >= 17:
            print_hand(dhand, dvalue, player)
            print("Dealer stands.")
            break
        else:
            dhand.append(deck.pop(0))
            dvalue = value_adder(dhand,dvalue)
            continue
    return dvalue

def reset(deck,hand,dhand,value,dvalue):
    deck.extend(hand)
    hand.clear()
    deck.extend(dhand)
    dhand.clear()
    random.shuffle(deck)
    hand.append(deck.pop(0))
    dhand.append(deck.pop(0))
    hand.append(deck.pop(0))
    dhand.append(deck.pop(0))

def end_stats(dhand,hand,value,dvalue):
    print(f'Dealer hand_____')
    player = 'Dealer'
    print_hand(dhand, dvalue, player)
    print(f'Your hand_____')
    player = 'Your'
    print_hand(hand, value, player)