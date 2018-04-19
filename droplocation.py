import random

def get_locations():
    drop_locations = {
        "Junk Junction",
        "Haunted Hills",
        "Pleasant Park",
        "Snobby Shores",
        "Greasy Grove",
        "Shifty Shafts",
        "Flush Factory",
        "Tilted Towers",
        "Loot Lake",
        "Flush Factory",
        "Anarchy Acres",
        "Tomato Town",
        "Dusty Depot",
        "Salty Springs",
        "Lucky Landing",
        "Fatal Fields",
        "Moisty Mire",
        "Retail Row",
        "Wailing Woods",
        "Lonely Lodge"
    }
    return drop_locations

def main():
    possible_locations = get_locations()
    print(possible_locations)



if __name__ == "__main__":
    main()
