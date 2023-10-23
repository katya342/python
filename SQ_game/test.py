
from api.deskforcards import draw_cards, init_game


suits = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
ranks = ["6", "7", "8", "9", "0", "J", "Q", "K", "A"]
def check_cards(cards: dict, deck_id: str) -> dict:
    id = 0  # Initialize the index
    while id < len(cards["cards"]):
        card = cards["cards"][id]
        if card["code"][0] not in ranks:
            cards["cards"].pop(id)  # Удалить карту, которая не входит в ranks
            continue
        while card["code"][0] not in ranks:
            new_cards = draw_cards(deck_id, str(1))["cards"]
            if not new_cards:
                break  # No more cards in the deck
            new_card = new_cards[0]
            new_card["code"] = ("10" if new_card["code"][0] == "0" else new_card["code"][0]) + suits[new_card["code"][1]]
            cards["cards"][id] = new_card
            card = new_card
        id += 1  # Increment the index

    return cards


def get_cards_without_pairs(cards):
    cards_without_pairs = []
    number_of_cards_by_values = get_number_of_cards_by_values(cards)
    print(number_of_cards_by_values)
    for card in reversed(cards):
        if number_of_cards_by_values[card[0]] % 2 != 0:
            cards_without_pairs.append(card)
            number_of_cards_by_values[card[0]] -= 1
            print(number_of_cards_by_values)
    return cards_without_pairs

def get_number_of_cards_by_values(cards):
    number_of_cards_by_values = {}
    
    for card in cards:
        if card[0] not in number_of_cards_by_values:
            number_of_cards_by_values[card[0]] = 1
        else:
            number_of_cards_by_values[card[0]] += 1
    
    return number_of_cards_by_values

if __name__ == "__main__":
    deck_id = init_game()
    player1_hand = [
        val["code"] for val in check_cards(draw_cards(deck_id, str(26)), deck_id)["cards"]
    ]
    
    player2_hand = [
        val["code"] for val in check_cards(draw_cards(deck_id, str(26)), deck_id)["cards"]
    ]
    print(player1_hand, " ")
    print(player2_hand, " ")
