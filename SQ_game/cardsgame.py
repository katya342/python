import random
import requests
from collections import Counter
from api.deskforcards import init_game, draw_cards, adding_to_piles, listing_cards_in_piles

suits = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
ranks = ["6", "7", "8", "9", "0", "J", "Q", "K", "A"]

# def check_cards(cards: dict, deck_id: str) -> dict:
#     id = 0  # Initialize the index
#     while id < len(cards["cards"]):
#         card = cards["cards"][id]
#         while card["code"][0] not in ranks:
#             new_cards = draw_cards(deck_id, str(1))["cards"]
#             if not new_cards:
#                 break  # No more cards in the deck
#             new_card = new_cards[0]
#             new_card["code"] = ("10" if new_card["code"][0] == "0" else new_card["code"][0]) + suits[new_card["code"][1]]
#             cards["cards"][id] = new_card
#             card = new_card
#         id += 1  # Increment the index

#     return cards
def check_cards(cards: dict, deck_id: str) -> dict:
    id = 0  # Initialize the index
    while id < len(cards["cards"]):
        card = cards["cards"][id]
        if card["code"][0] not in ranks:
            cards["cards"].pop(id)  # Удалить карту, которая не входит в ranks
            continue

        # Проверка на даму (королеву) другой масти и удаление её
        if card["code"] == "QD" or card["code"] == "QC" or card["code"] == "QH":
            cards["cards"].pop(id)
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


def get_similar_cards(player_hand):
    similar_cards = []
    seen_ranks = set()  # To keep track of seen ranks

    for i in range(len(player_hand)):
        card1 = player_hand[i]
        rank1 = card1[0]

        if rank1 not in seen_ranks:
            for j in range(i + 1, len(player_hand)):
                card2 = player_hand[j]
                rank2 = card2[0]

                if rank1 == rank2:
                    similar_cards.append((card1, card2))
                    break  # Add only one pair for each rank
            seen_ranks.add(rank1)

    return similar_cards

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
   
    return cards_by_value                      # Returns dictionary

        

   
    


if __name__ == "__main__":
    deck_id = init_game()

    player1_hand = [
        val["code"] for val in check_cards(draw_cards(deck_id, str(26)), deck_id)["cards"]
    ]
    
    player2_hand = [
        val["code"] for val in check_cards(draw_cards(deck_id, str(26)), deck_id)["cards"]
    ]
    
 
    player1_hand_last = get_cards_without_pairs(player1_hand)
    player2_hand_last = get_cards_without_pairs(player2_hand)
   
    

    

    # Ход игры
    current_player = "player"
    while len(player1_hand_last) > 0 and len(player2_hand_last) > 0:
        if current_player == "player":
            # Ход игрока
            player1_hand_last = get_cards_without_pairs(player1_hand_last)
            print("Ваша рука:", player1_hand_last)
            
            card_to_play = input("Выберите карту для хода: ")
            if card_to_play in player1_hand_last:
                player1_hand_last.remove(card_to_play)
                player2_hand_last.append(card_to_play)
                current_player = "computer"
              
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        else:
            # Ход компьютера
            # print("Computer: ", player2_hand_last)
            player2_hand_last = get_cards_without_pairs(player2_hand_last)
            card_to_play = random.choice(player2_hand_last)
            print(card_to_play)
            player2_hand_last.remove(card_to_play)
            player1_hand_last.append(card_to_play)
            current_player = "player"
            
    # Проверка условий победы
    if len(player1_hand_last) == 0:
        print("Вы победили! У вас не осталось карт в руке.")
    else:
        print("Компьютер победил! У вас осталось", len(player1_hand_last), "карт в руке.")
