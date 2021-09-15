from functions import cards1, cards2, table

ante = 10
call = ante * 2
player_money = 100
player_choice = input(' to fold press f to call press anything: ')

if player_choice == 'f':
    player_money -= ante
    print('your money: ',player_money)
    quit()

print(table)
print("dealer's card: ",cards2[:2])
    

# test_cards = ['2H', '10H', '11c', '12D', '13H', '14H', '9C']
# print(cards1)
# print(cards2)

print('----------')

def main(cards, player):
    flush_comb = is_flush(cards, player)
    strit_comb = streat(cards, player)
    strong_comb = strongest_combination(cards, player)
    # print(flush_comb, strit_comb, strong_comb)
    if flush_comb:
        return flush_comb
    elif strit_comb:
        return strit_comb
    elif strong_comb:
        return strong_comb


def is_flush(cards: list, player):
    suit=[]
    card_num = []

    for i in cards:
        card_num.append(int(i[:-1]))
        suit.append(i[-1])

    sorted_cards = sorted(card_num, reverse=True)
    count_suits = {i:suit.count(i) for i in suit} # create dictionary to count suits
    key = [k for k, v in count_suits.items() if v >= 5] # find 5 or more suit values in dictionary and return key
    # print('key', key)
    if key:
        flush_list = []
        for card in cards:
            if key[0] == card[-1]:
                flush_list.append(card)

        sort_flush = sorted(flush_list, key = lambda x: int(x[:-1]), reverse=True)
        final_flush = sort_flush[:5]
        if len(sort_flush) >= 5 and int(sort_flush[0][:-1]) - int(sort_flush[4][:-1]) == 4 and int(sort_flush[0][:-1]) == 14:
            print(f'{player} have flush royal ', sort_flush[:5])
            final_flush = sort_flush[:5]
            return 10
        elif len(sort_flush) >= 5 and int(sort_flush[0][:-1]) - int(sort_flush[4][:-1]) == 4:
            print(f'{player} have flush street', sort_flush[:5])
            final_flush = sort_flush[:5]
            return 9, int(sort_flush[0][:-1])
        elif len(sort_flush) >= 6 and int(sort_flush[1][:-1]) - int(sort_flush[5][:-1]) == 4:
            print(f'{player} have flush street', sort_flush[1:6])
            final_flush = sort_flush[1:6]
            return 9, int(sort_flush[1][:-1])
        elif len(sort_flush) == 7 and int(sort_flush[2][:-1]) - int(sort_flush[5][:-1]) == 4:
            print(f'{player} have flush street', sort_flush[2:])
            final_flush = sort_flush[2:]
            return 9, int(sort_flush[2][:-1])
        elif len(sort_flush) >= 5 and int(sort_flush[0][:-1]) == 14 and int(sort_flush[-4][:-1]) == 5 and int(sort_flush[-4][:-1]) - int(sort_flush[-1][:-1]) == 3:
            print(f'{player} have flush street', sort_flush[-4:] + [sort_flush[0]])
            final_flush = sort_flush[2:]
            return 9, int(sort_flush[-4][:-1])
        else:
            print(f'{player} have flush {final_flush}')          
            return 6, int(final_flush[0][:-1]), int(final_flush[1][:-1]), int(final_flush[2][:-1]), int(final_flush[3][:-1]), int(final_flush[4][:-1])
    else:
        return False


def streat(cards, player):
    suit=[]
    card_num = []

    for i in cards:
        card_num.append(int(i[:-1]))
        suit.append(i[-1])

    sorted_cards = sorted(card_num, reverse=True)
    set_sorted_cards = set(sorted_cards)
    uniq_cards_list = list(set_sorted_cards)
    uniq_cards_list.reverse()
    # print(uniq_cards_list)
    if len(uniq_cards_list) >= 5 and uniq_cards_list[0] - uniq_cards_list[4] == 4:
        print('{player} have straight', uniq_cards_list[:5])
        return 5, uniq_cards_list[0]
    elif len(uniq_cards_list) >= 6 and uniq_cards_list[1] - uniq_cards_list[5] == 4:
        print('{player} have straight', uniq_cards_list[1:6])
        return 5, uniq_cards_list[1]
    elif len(uniq_cards_list) == 7 and uniq_cards_list[2] - uniq_cards_list[6] == 4:
        print("{player} have straight", uniq_cards_list[2:])
        return 5, uniq_cards_list[2]
    elif len(uniq_cards_list) >= 5 and uniq_cards_list[0] == 14 and uniq_cards_list[-4] == 5 and uniq_cards_list[-4] - uniq_cards_list[-1] == 3:
        print("{player} have straight", uniq_cards_list[-4:] + [14])
        return 5, uniq_cards_list[0]
    else:
        return False


def strongest_combination(cards, player):
    suit=[]
    card_num = []

    for i in cards:
        card_num.append(int(i[:-1]))
        suit.append(i[-1])

    sorted_cards = sorted(card_num, reverse=True)
    weight_dict = {i: sorted_cards.count(i)**3 for i in sorted_cards}  
    weight = sum(weight_dict.values())
    # print(weight)
    if weight == 7:
        print(F"{player} have high card: {sorted_cards[0]}")
        return 1, sorted_cards[0], sorted_cards[1], sorted_cards[2], sorted_cards[3], sorted_cards[4]
    elif weight == 13:
        pair = [x for x in sorted_cards if sorted_cards.count(x) > 1]
        remain_cards = list(set(sorted_cards) - set(pair))
        remain_cards = sorted(remain_cards, reverse=True)
        final_cards = remain_cards[:3] + pair
        print(final_cards)
        print(F"{player} have pairs: {pair}" )
        return 2, pair[0], remain_cards[0], remain_cards[1], remain_cards[2]
    elif 19 <= weight <= 25:
        two_pair = [x for x in sorted_cards if sorted_cards.count(x) > 1]
        remain_cards = list(set(sorted_cards) - set(two_pair))
        remain_cards = sorted(remain_cards, reverse=True)
        if len(two_pair) == 4:
            final_cards = [remain_cards[0]] + two_pair
            print(final_cards)
            print(F"{player} have two pairs: {two_pair}")
            return 3, two_pair[0], two_pair[2], remain_cards[0]
        elif len(two_pair) == 6:
            remain_cards.append(two_pair[-1])
            remain_cards.append(two_pair[-1])
            remain_cards = sorted(remain_cards, reverse=True)
            two_pair = two_pair[:4]
            final_cards = [remain_cards[0]] + two_pair
            print(final_cards)
            print(F"{player} have two pairs: {two_pair}")
            return 3, two_pair[0], two_pair[2], remain_cards[0]
    elif weight == 31:
        three_of_kind = [x for x in sorted_cards if sorted_cards.count(x) > 2]
        remain_cards = list(set(sorted_cards) - set(three_of_kind))
        remain_cards = sorted(remain_cards, reverse=True)
        final_cards = remain_cards[:2] + three_of_kind
        print(final_cards)
        print(F"{player} have three of kind: {three_of_kind}")
        return 4, three_of_kind[0], remain_cards[0], remain_cards[1]
    elif 37 <= weight <= 55:
        full_house_3 = [x for x in sorted_cards if sorted_cards.count(x) > 2]
        full_house_2 = [x for x in sorted_cards if sorted_cards.count(x) == 2]
        if len(full_house_2) == 2:
            full_house_5 = full_house_2 + full_house_3
            print(F"{player} have full house: {full_house_5}")
            return 7, full_house_3[0], full_house_2[0]
        elif len(full_house_2) == 4:
            full_house_2 = sorted(full_house_2, reverse=True)
            full_house_2 = full_house_2[:2]
            full_house_5 = full_house_2 + full_house_3
            print(F"{player} have full house: {full_house_5}")
            return 7, full_house_3[0], full_house_2[0] 
    elif weight >= 64:
        kare = [x for x in sorted_cards if sorted_cards.count(x) > 3]
        remain_cards = list(set(sorted_cards) - set(kare))
        remain_cards = sorted(remain_cards, reverse=True)
        final_cards = [remain_cards[0]] + kare
        print(final_cards)
        print(F"{player} have four of kind: {kare}")
        return 8, kare[0], remain_cards[0]


player = main(cards1, 'You')
dealer = main(cards2, 'Dealer')

print(player)
print(dealer)

# winner
def compare(player: list, dealer: list):
    if player[0] > dealer[0]:
        print('player win')
        return 'player win'
    elif player[0] < dealer[0]:
        print('dealer win')
        return 'dealer win'
    elif player[0] == 10 and dealer[0] == 10:
        print('tie')
        return 'tie'
    elif player[0] == dealer[0]:
        if player[1] > dealer[1]:
            print('player win')
            return 'player win'
        elif player[1] < dealer[1]:
            print('dealer win')
            return 'dealer win'
        elif player[1] == dealer[1]:
            if len(player) > 2:
                if player[2] > dealer[2]:
                    print('player win')
                    return 'player win'
                elif player[2] < dealer[2]:
                    print('dealer win')
                    return 'dealer win'
                elif player[2] == dealer[2]:
                    if len(player) > 3:
                        if player[3] > dealer[3]:
                            print('player win')
                            return 'player win'
                        elif player[3] < dealer[3]:
                            print('dealer win')
                            return 'dealer win'
                        elif player[3] == dealer[3]:
                            if len(player) > 4:
                                if player[4] > dealer[4]:
                                    print('player win')
                                    return 'player win'
                                elif player[4] < dealer[4]:
                                    print('dealer win')
                                    return 'dealer win'
                                elif player[4] == dealer[4]:
                                    if len(player) > 5:
                                        if player[5] > dealer[5]:
                                            print('player win')
                                            return 'player win'
                                        elif player[5] < dealer[5]:
                                            print('dealer win')
                                            return 'dealer win'
                                        elif player[4] == dealer[4]:
                                            print('tie')
                                            return 'tie'
                                    else:
                                        print('tie')
                                        return 'tie'
                            else:
                                print('tie')
                                return 'tie'
                    else:
                        print('tie')
                        return 'tie'
            else:
                print('tie')
                return 'tie'

compare(player, dealer)


# finances

winner = compare(player, dealer)

def diler_down(cards):
    if cards[0] == 1:
        return True
    if cards[0] == 2 and cards[1] < 4:
        return True
    return False

dealer_no_game = diler_down(dealer)


if winner == 'player win':
    if dealer_no_game == True:
        player_money += ante
    else:
        player_money += ante + call
elif winner == 'dealer win':
    player_money -= ante + call

print('you have: ', player_money)
                









