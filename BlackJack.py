#
#
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
playagain = ("---Play Again---\nPress Enter to continue\nor type anything and hit enter to quit.")
goodbye = ("Goodbye!\n")
count = 1
play = True
deck_count = 1
win_count = 0
lose_count = 0

def play_again(play):
    while True:
            try:
                again = input(playagain)
                if again == '':
                    bj.reset(deck,hand,dhand,value,dvalue)
                    play = True
                    return play
                elif again != '':
                    print()
                    print(goodbye)
                    play = False
                    return play
                else:
                    print(error)
            except ValueError:
                print()

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

    while play == True:
        print("Dealer Stands on 17 or higher.\n")
        player = 'Your'
        #print(deck)
        #print(f'\n-----Deck Check-----\n{len(deck)} cards in deck \n\n')
        value = bj.value_adder(hand, value)
        dvalue = bj.value_adder(dhand, dvalue)
        #print(f'-----Value Checks-----\nPlayer: {hand},{value}\nDealer: {dhand},{dvalue}\n{len(deck)} cards in deck\n\n')
        bj.print_hand(hand, value, player)
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
                play = play_again(play)
                bj.reset(deck,hand,dhand,value,dvalue)
                continue
            else:
                print(controls)
                selection = input("-")
            print()

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

            player = 'Dealer'
            if selection == '3':
                break
            elif value > dvalue or dvalue > 21:
                win_count += 1
                print(f'\nYou win!\nYou had      |{value}\nDealer had   |{dvalue}\n')
                #bj.end_stats(dhand, hand, value, dvalue)
            elif value < dvalue or dvalue == 21:
                lose_count += 1
                print(f'\nDealer win.\nYou had      |{value}\nDealer had   |{dvalue}\n')
                #bj.end_stats(dhand, hand, value, dvalue)
            else:
                print(f'\nDealer Push.\nYou had      |{value}\nDealer had   |{dvalue}\n')
                #bj.end_stats(dhand,hand,value,dvalue)
            #print(f'\n-----Deck Check-----\n{len(deck)} cards in deck \n\n')
            play = play_again(play)
            if play == False:
                break
        except ValueError:
            print(error)

    print(f'You won  [{win_count}] hands!\nYou lost [{lose_count}] hands!\n\n')