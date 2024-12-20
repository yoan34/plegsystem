import json
import os

with open("data.json", "r") as f:
    plegsystem = json.load(f)
    
CATEGORIES = ["personnage", "animaux", "plantes", "métiers", "science", "lieux", "verbe", "adjectifs", "autres"]

def manage_menu_range(sub_pleg):
    os.system("clear")
    print(f"CHOIX A RANGE".center(40, "-"))
    ranges = list(map(int, list(sub_pleg.keys())))
    ranges.sort()
    print(f"\n       START RANGE {ranges[0]} - END RANGE {ranges[-1]}")
    choice = input("            > ")
    choice = choice.split('-')
    if len(choice) == 3:
        range_inf, range_sup, format = choice[0], choice[1], choice[2]
    else:
        print("You must enter a valid range. format: RANGE_INF-RANGE_SUP")
        return
    try:
        range_inf = int(range_inf)
        range_sup = int(range_sup)
    except Exception:
        print("You must enter a valid range. format:RANGE_INF-RANGE_SUP")
    return choice
    

def show_not_randomly_game(sub_pleg, inf, sup):
    L = len(list(sub_pleg.keys()))
    print("")

def manage_menu():
    os.system("clear")
    print(f"CHOIX CATEGORIE".center(40, "-"))
    print()
    print("            1 - personnages")
    print("            2 - animaux")
    print("            3 - plantes")
    print("            4 - métiers")
    print("            5 - science")
    print("            6 - lieux")
    print("            7 - verbe")
    print("            8 - adjectifs")
    print("            9 - autres\n")
    print("-"*40)
    choice = input("            > ")
    try:
        choice = int(choice)
    except Exception:
        print(f"You must enter a valid number between [1, 9]")
        return
    if choice > 9 or choice < 1:
        print("Enter number between [1, 9]")
    return choice
   
   
while True: 
    
    user_choice = manage_menu()
    if user_choice is not None:
        sub_pleg = plegsystem[CATEGORIES[user_choice-1]]
        user_choice = manage_menu_range(sub_pleg)
        if user_choice is not None:
            inf, sup, format = user_choice[0], user_choice[1], user_choice[2]
            if format == "s": #show
                show_not_randomly_game(sub_pleg=sub_pleg, inf, sup)
            if format == "r": #random
                pass
            if format == "rs" or format == "sr": #show and random
                pass
            if format == "nr" or format == "rn": # not show and now random
                pass
            
            
            
        
            
            

