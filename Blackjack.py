from Blackjack_classes import Card, Deck, Player
from time import sleep

def reveal_all(player, dealer):
    print(f"{dealer.name}'s hand " + ", ".join([str(card.value) for card in dealer.hand]))
    print(f"{player.name}'s hand " + ", ".join([str(card.value) for card in player.hand]) + "\n")

def reveal_some(player,dealer):
    card = dealer.hand[1]
    print(f"{dealer.name}'s hand " "X " + str(card.value))
    print(f"{player.name}'s hand " + ", ".join([str(card.value) for card in player.hand]) + "\n")

def hit_or_stand(deck,player):
    while player.value < 21:
        print(f"{player.name}'s hand " + ", ".join([str(card.value) for card in player.hand]))
        print(f"{player.name}'s hand value: {player.value}")
        try:
            choice = input("Do you want to hit or stand? Enter 'h' or 's' \n")
            if choice[0].lower() == "h":
                hit(deck,player)
                print()
            elif choice[0].lower() == "s":
                print(f"{player.name} stands, dealer's turn \n")
                break
            else:
                raise ValueError
        except ValueError:
            print("Not a valid option\n")

def hit(deck,player):
    print(f"{player.name} hits")
    player.add_card(deck.deal())
    player.ace_adjust_hand()

def bust(person):
    return True if person.value > 21 else False

def has_betterhand(player,dealer):
    return True if player.value > dealer.value else False



play_blackjack = True
game_count = 1
while play_blackjack:
    print(f"\t\t    Game:{game_count}")
    print("------------------------------------------------")
# Initialize deck, player, dealer
    deck = Deck()
    for x in range(10):
        deck.shuffle()
    dealer = Player("Dealer")
    p1 = Player("P1")

# Deal out hands
    for x in range(2):
        p1.add_card(deck.deal())
        dealer.add_card(deck.deal())
        p1.ace_adjust_hand()
        dealer.ace_adjust_hand()

# Soft reveal of dealer/player hands
    reveal_some(p1,dealer)
    sleep(3)


# Ask if player wants to hit/stand, only if player.value < 21
    hit_or_stand(deck,p1)

# Full reveal of dealer/player hands
    reveal_all(p1,dealer)
    sleep(3)

# Dealer hits/must keep hitting if hand value < 17
    while dealer.value < 17:
        hit(deck, dealer)

# Shows the final hand for both the player and dealer
    reveal_all(p1,dealer)

# Check for tie/win/lose conditions (if, elif or, else) and display results
    # Tie
    # player and dealer hands have same value 
    if p1.value == dealer.value:
        print(f"{p1.name} and {dealer.name} have equal hands, TIE!")
    # Both player and dealer bust
    elif bust(p1) and bust(dealer):
        print(f"{p1.name} and {dealer.name} busted, TIE!")
    
    # Win condition
    # dealer bust
    elif bust(dealer) and not bust(p1):
        print(f"{dealer.name} busts, {p1.name} wins")
    # player doesn't bust and player.value > dealer.value
    elif has_betterhand(p1,dealer):
        print(f"{p1.name} wins with a {p1.value}")

    # Lose condition
    # player bust
    elif bust(p1) and not bust(dealer):
        print(f"{p1.name} busts, {dealer.name} wins")
    # dealer.value <= 21 and dealer.value > player.value
    else:
        print(f"{dealer.name} wins with a {dealer.value}")

    print()

# Prompt player if they want to play again
    playagain = True
    while playagain:
        try:
            choice = input("Do you want to play again? Enter 'y' or 'n' \n")
            if choice[0].lower() == "y":
                print()
                game_count+=1
                break
            elif choice[0].lower() == "n":
                play_blackjack = False
                break
            else:
                raise ValueError
        except ValueError:
            print("Not a valid option")