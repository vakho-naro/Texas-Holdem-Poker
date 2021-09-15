import random

values = ['2','3','4','5','6','7','8','9','10','11','12','13','14']
suites = ['H', 'C', 'D', 'S']

deck = [v + s for s in suites for v in values]

random.shuffle(deck)


table = deck[-5:]

print(f'table {table[:3]}')

for card in table:
    deck.pop(deck.index(card))


def player1_cards():
    player1 = deck[-2:]

    print(f'your cards: {player1}')
    for card in player1:
        deck.pop(deck.index(card))

    player1_pos = player1 + table

    return player1_pos


cards1 = player1_cards()

def player2_cards():
    player2 = deck[-2:]
    # print(f'player2 {player2}')

    for card in player2:
        deck.pop(deck.index(card))
    
    player2_pos = player2 + table

    return player2_pos


cards2 = player2_cards()
