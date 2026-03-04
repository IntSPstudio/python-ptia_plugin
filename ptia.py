#|==============================================================|#
# Made by IntSPstudio
# Thank you for using this plugin!
# Version: 0.0.2.110403
# ID: 980007009
#|==============================================================|#

#LIBRARIES
import json
from os import system, name
#LOAD DATA
def load_menu(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
#MENU LOOP
def show_menu(menu, start_page="P01"):
    current_page = start_page
    continuity = 1
    while continuity == 1:
        #SCREEN CLEAR
        if name == 'nt':
            system('cls')
        else:
            system('clear')
        #TA
        page = menu.get(current_page, {})
        title = page.get("Title", "Unknown")
        print(f"==] ======== {title} ========")
        #TB
        rows = [(key, val) for key, val in page.items() if key.startswith("R")]
        rows.sort()
        if not rows:
            pa = input("")
        #SHOW MENU
        for idx, (key, item) in enumerate(rows, start=1):
            print(f"{idx} ] {item['Title']}")
        #INPUT
        try:
            user_input = int(input("==] "))
            if user_input < 1 or user_input > len(rows):
                continue
            elif user_input == "":
                continuity
        except ValueError:
            continue
        #SELECTED ROW
        _, selected_item = rows[user_input - 1]
        next_page = selected_item.get("Link")
        if next_page and next_page in menu:
            current_page = next_page
        elif next_page == "P00":
            continuity =0
        else:
            current_page = start_page
#START
if __name__ == "__main__":
    menu = load_menu("example.json")
    show_menu(menu, "P01")