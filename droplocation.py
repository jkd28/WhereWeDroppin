import random

def get_locations():
    drop_locations = [
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
    ]
    return drop_locations

def get_drop_location(possible_locations):
    random.shuffle(possible_locations)
    random_loc = random.randrange(0,len(possible_locations))
    return possible_locations[random_loc]

def main():
    possible_locations = get_locations()
    drop_location = get_drop_location(possible_locations)
    print("Drop Location: \n\r    " + drop_location)


if __name__ == "__main__":
    main()
