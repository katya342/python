
from api.deskforcards import draw_cards, init_game
from cardsgame import check_cards


import requests

suits = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
ranks = ["6", "7", "8", "9", "0", "J", "Q", "K", "A"]
def get_cards_without_pairs(cards):
    cards_without_pairs = []
    number_of_cards_by_values = get_number_of_cards_by_values(cards)
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
def draw_cards(deck_id: str, num_cards: str) -> dict:
    url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={num_cards}"
    response = requests.get(url)
    return response.json()

def check_cards(cards: dict, deck_id: str) -> dict:
    id = 0  # Initialize the index
    remaining_cards = len(cards["cards"])

    while id < remaining_cards:
        card = cards["cards"][id]
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

def init_game() -> str:
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    return response.json()["deck_id"]

deck_id = init_game()

# Определите, сколько карт нужно для каждой руки
num_cards_per_hand = 26
response = draw_cards(deck_id, str(num_cards_per_hand * 2))  # Запросите двойное количество карт

if "cards" in response:
    player1_hand = [val["code"] for val in check_cards(response, deck_id)["cards"][:num_cards_per_hand]]
    player2_hand = [val["code"] for val in check_cards(response, deck_id)["cards"][num_cards_per_hand:]]
else:
    print("Недостаточно карт в колоде.")
last_hand_1 = get_cards_without_pairs(player1_hand)
last_hand_2 = get_cards_without_pairs(player2_hand)
# Теперь у вас есть карты для обеих рук
print("Игрок 1:", last_hand_1)
print("Игрок 2:", last_hand_2)
