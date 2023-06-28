import deck
import player

WAR_CARDS = 5

player_one = player.Player("One")
player_two = player.Player("Two")

new_deck = deck.Deck()
new_deck.shuffle()
# first = new_deck.all_cards[-1]
# print(len(new_deck.all_cards))
# my_card = new_deck.deal_one()


for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

# Game logic
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Player Two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Player One wins!")
        game_on = False
        break

    # Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            if len(player_one.all_cards) < WAR_CARDS:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS")
                game_on = False
                break

            elif len(player_two.all_cards) < WAR_CARDS:
                print("Player Two unable to declare war")
                print("PLAYER ONE WINS")
                game_on = False
                break

            else:
                for num in range(WAR_CARDS):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())




