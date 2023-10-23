import json
import requests

MAIN_URL = "https://www.deckofcardsapi.com/api/deck/"

def new_desk() -> requests.Response:
    return requests.get(MAIN_URL + "new/shuffle/?deck_count=1")

def init_game() -> str:
    desk = new_desk()
    get_json = json.loads(desk.content.decode("utf-8"))
    if get_json["success"]:
        return get_json["deck_id"]
    return None


def draw_cards(desk_id, cards = None) -> dict:
    if cards is not None:
        cards = requests.get(MAIN_URL + desk_id + "/draw/?count=" + cards)
    else:
        cards = requests.get(MAIN_URL + desk_id + "/draw/?count=50")
    if cards.status_code != 200:
        print(cards.status_code, "ServerError")
        exit()
    return json.loads(cards.content.decode("utf-8"))


def partial_deck(card_codes) -> dict:
    cards = requests.get(MAIN_URL + "/new/shuffle/?cards=" + card_codes)
    return json.loads(cards.content.decode("utf-8"))