#
#TODO:
#add coins
#actual gambling
#double down
#save states?
#
#
import blackjack_mod as bj
suits = {'\u2661','\u2667','\u2664','\u2662'}
ranks  = {2,3,4,5,6,7,8,9,10,'J','Q','K','A'}
deck = []
hand = []
dhand = []
value = 0
dvalue = 0
error = "ERROR:Please enter a valid option"
welcome = ("\nWelcome to Blackjack!\n")
controls = ("Hit         |1\nStay        |2\nEnd         |3\n")
goodbye = ("Goodbye!\n")
count = 1
play = True
deck_count = 1
win_count = 0
lose_count = 0

#MAIN
if __name__ == "__main__":

    while deck_count > 0:
        bj.building_deck(ranks, suits, deck)
        deck_count -= 1
    print(len(deck))
    hand.append(deck.pop(0))
    dhand.append(deck.pop(0))
    hand.append(deck.pop(0))
    dhand.append(deck.pop(0))
    print(f'{welcome}')

#MAIN GAME LOOP
    while play == True:
        print("Dealer Stands on 17 or higher.\n")
        player = 'Your'
        value = bj.value_adder(hand, value)
        dvalue = bj.value_adder(dhand, dvalue)
        bj.print_hand(hand, value, player)

#Instant win/loss checks
        try:
            if value == 21:
                print("Black Jack!\n")
                win_count += 1
                bj.reset(deck,hand,dhand,value,dvalue)
                continue
            elif dvalue == 21:
                player = 'Dealer'
                lose_count += 1
                bj.print_hand(dhand, dvalue, player)
                print("Dealer black jack.\n")
                bj.reset(deck, hand, dhand, value, dvalue)
                continue
            elif value > 21:
                lose_count += 1
                print("Bust.\n")
                play = bj.play_again(play,deck,hand,dhand,value,dvalue,goodbye,error)
                bj.reset(deck,hand,dhand,value,dvalue)
                continue
            else:
                print(controls)
                selection = input("-")
            print()

#Menu Loop
            if selection == '1':
                selection = 0
                hand.append(deck.pop(0))
                value = bj.value_adder(hand,value)
                continue
            elif selection ==  '2':
                selection = 0
                dvalue = bj.dealer_move(dhand,dvalue,deck,value)
            elif selection == '3':
                print("Exiting game.\n")
                print(goodbye)
            else:
                print(error)
                continue

#End game checks
            player = 'Dealer'
            if selection == '3':
                break
            elif value > dvalue or dvalue > 21:
                win_count += 1
                print(f'\nYou win!\nYou had      |{value}\nDealer had   |{dvalue}\n')
            elif value < dvalue or dvalue > 21:
                lose_count += 1
                print(f'\nDealer win.\nYou had      |{value}\nDealer had   |{dvalue}\n')
            else:
                print(f'\nDealer Push.\nYou had      |{value}\nDealer had   |{dvalue}\n')
            play = bj.play_again(play,deck,hand,dhand,value,dvalue,goodbye,error)
            if play == False:
                break
        except ValueError:
            print(error)

    print(f'You won  [{win_count}] hands!\nYou lost [{lose_count}] hands!\n\n')