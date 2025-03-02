type_dict = {
    "Fine": 1000,
    "Nice": 750,
    "Good": 500,
    "Rare": 350,
    "Wild": 275,
    "Baby": 230,
    "Epic": 200,
    "Sus": 175,
    "Brave": 150,
    "Rickroll": 125,
    "Reverse": 100,
    "Superior": 80,
    "Trash": 50,
    "Legendary": 35,
    "Mythic": 25,
    "8bit": 20,
    "Corrupt": 15,
    "Professor": 10,
    "Divine": 8,
    "Real": 5,
    "Ultimate": 3,
    "eGirl": 2,
}

# create a huge list where each cat type is multipled the needed amount of times
CAT_TYPES = []
for k, v in type_dict.items():
    CAT_TYPES.extend([k] * v)

# this list stores unique non-duplicate cattypes
cattypes = list(type_dict.keys())

# pack data
pack_data = [
    {"name": "Wooden", "value": 65, "upgrade": 30, "totalvalue": 75},
    {"name": "Stone", "value": 90, "upgrade": 30, "totalvalue": 100},
    {"name": "Bronze", "value": 100, "upgrade": 30, "totalvalue": 130},
    {"name": "Silver", "value": 115, "upgrade": 30, "totalvalue": 200},
    {"name": "Gold", "value": 230, "upgrade": 30, "totalvalue": 400},
    {"name": "Platinum", "value": 630, "upgrade": 30, "totalvalue": 800},
    {"name": "Diamond", "value": 860, "upgrade": 30, "totalvalue": 1200},
    {"name": "Celestial", "value": 2000, "upgrade": 0, "totalvalue": 2000},  # is that a madeline celeste reference????
]