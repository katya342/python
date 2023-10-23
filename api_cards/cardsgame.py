from deskforcards import init_game, draw_cards, partial_deck
from collections import Counter

# лист для сохранения итоговых разданных карт каждому игроку
player_hand_cards_1 = []
player_hand_cards_2 = []
player_hand_cards_3 = []

def remove_all_duplicates(player_hand_cards) -> list:
    unique_player_hand_cards = []
    card_strings = set()  # Use a set to keep track of unique card strings

    for card in player_hand_cards:
        card_str = f'{card["value"]} {card["suit"]}'  # Create a string representation of the card
        if card_str not in card_strings:
            unique_player_hand_cards.append(card)
            card_strings.add(card_str)

    return unique_player_hand_cards

         
if __name__ == "__main__":
    # Создаю изначально колоду с нужными 36 картами: 6,7...валет, король, дама... всех мастей
    part_deck = partial_deck("6S,6C,6H,6D,7S,7C,7H,7D,8S,8C,8H,8D,9S,9C,9H,9D,0S,0C,0H,0D,JS,JC,JH,JD,QS,QC,QH,QD,KS,KC,KH,KD,AS,AC,AH,AD")
    # Получаю айди этой колоды с нужными нам картами
    part_deck_id = part_deck["deck_id"]
    #print("Partitial deck card id is: " + part_deck_id)
    #Для того, чтобы получить ключ-значения обращаюсь к draw_cards и передаю туда айди той самой колоды
    while True:
         player_hand_1 = draw_cards(part_deck_id, "1")
         player_hand_2 = draw_cards(part_deck_id, "1")
         player_hand_3 = draw_cards(part_deck_id, "1")
         player_hand_cards_1.extend(player_hand_1["cards"])
         player_hand_cards_2.extend(player_hand_2["cards"])
         player_hand_cards_3.extend(player_hand_3["cards"])
        #  print("Player_1 cards are:")
        #  for card in player_hand_1["cards"]:
        #     print(f'{card["value"]} {card["suit"]}')
         if player_hand_1["remaining"] == 0: break
        # print(f'Remaining cards in the deck : {player_hand_1["remaining"]}')
    
    
    print("Player_1 final cards are:")
    for card in player_hand_cards_1:
        print(f'{card["value"]} {card["suit"]}')

    # Удаление всех повторяющихся карт из колоды игрока 1
    print("Rezult")
    rez_player_hand_cards_1 = remove_all_duplicates(player_hand_cards_1)
    for cards in rez_player_hand_cards_1:
        print(f'{cards["value"]} {cards["suit"]}')
# Вывод уникальных карт для игрока 1 (без повторов)
    # print("Player 1 cards after removing all duplicates:")
    # for card in rez_player_hand_cards_1:
    #     print(f'{card["value"]} {card["suit"]}')
    # print("Player_2 final cards are: ")
    # for card in player_hand_cards_2:
    #     print(f'{card["value"]} {card["suit"]}')
    
    # print("Player 3 final cards are:")
    # for card in player_hand_cards_3:
    #     print(f'{card["value"]} {card["suit"]}')
    

   

    

   
   
    


  
  
  
  
  
 

   

