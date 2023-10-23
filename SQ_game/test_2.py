
def get_cards_without_pairs(cards):
    temp_cards_values = get_cards_value(cards)
    last = []
    for card in cards:
        if temp_cards_values[card[0]] % 2 != 0:
            last.append(card)
            temp_cards_values[card[0]] -= 1
    return last

def get_cards_value(cards):
    cards_by_value = {}
    for card in cards:
        if card[0] not in cards_by_value:
            cards_by_value[card[0]] = 1      # 9 : 1
        else:
            cards_by_value[card[0]] += 1     # 9 : 2
    print(cards_by_value)
    return cards_by_value                      # Returns dictionary



if __name__ == "__main__":
    cards = ["9A", "6S", "9D", "6D", "AS", "A4", "6H", "A5", "10D", "10H", "10S"]
    cards_withour_pairs = get_cards_without_pairs(cards)
    for card in cards_withour_pairs:
        print(card, end=" ")