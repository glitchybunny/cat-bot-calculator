import random

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


def open_pack(pack_id):
    """
    if interaction.user != message.user:
        await do_funny(interaction)
        return
    await interaction.response.defer()
    """
    pack = pack_id
    #user = get_profile(message.guild.id, message.user.id)
    level = next((i for i, p in enumerate(pack_data) if p["name"] == pack), 0)
    #reward_texts = []
    #build_string = ""

    # bump rarity
    try_bump = True
    while try_bump:
        if random.randint(1, 100) <= pack_data[level]["upgrade"]:
            #reward_texts.append(f"{get_emoji(pack_data[level]['name'].lower() + 'pack')} {pack_data[level]['name']}\n" + build_string)
            #build_string = f"Upgraded from {get_emoji(pack_data[level]['name'].lower() + 'pack')} {pack_data[level]['name']}! (30%)\n" + build_string
            level += 1
            #user.pack_upgrades += 1
        else:
            try_bump = False
    final_level = pack_data[level]
    #reward_texts.append(f"{get_emoji(final_level['name'].lower() + 'pack')} {final_level['name']}\n" + build_string)

    # select cat type
    goal_value = final_level["value"]
    lower_bound, upper_bound = goal_value * 0.85, goal_value * 1.15
    found = []
    while not found:
        test_type = random.choice(cattypes)
        value_per_type = len(CAT_TYPES) / type_dict[test_type]
        n = 0
        while True:
            n += 1
            if value_per_type * n < lower_bound:
                continue
            if value_per_type * n > upper_bound:
                break
            found.append([test_type, n])
    reward = random.choice(found)

    """
    user[f"cat_{reward[0]}"] += reward[1]
    user.packs_opened += 1
    user[f"pack_{pack.lower()}"] -= 1
    user.save()
    reward_texts.append(reward_texts[-1] + f"\nYou got {get_emoji(reward[0].lower() + 'cat')} {reward[1]} {reward[0]} cats!")

    embed = discord.Embed(title=reward_texts[0], color=0x6E593C)
    await interaction.edit_original_response(embed=embed, view=None)
    for reward_text in reward_texts[1:]:
        await asyncio.sleep(1)
        things = reward_text.split("\n")
        embed = discord.Embed(title=things[0], description="\n".join(things[1:]), color=0x6E593C)
        await interaction.edit_original_response(embed=embed)
    await asyncio.sleep(1)
    await interaction.edit_original_response(view=gen_view(user))
    
    description = "Each pack starts at one of eight tiers of increasing value - Wooden, Stone, Bronze, Silver, Gold, Platinum, Diamond, or Celestial - and can repeatedly move up tiers with a 30% chance per upgrade. This means that even a pack starting at Wooden, through successive upgrades, can reach the Celestial tier.\n\nClick the buttons below to start opening packs!"
    embed = discord.Embed(title="Packs", description=description, color=0x6E593C)
    user = get_profile(message.guild.id, message.user.id)
    await message.response.send_message(embed=embed, view=gen_view(user))
    """

    return (pack, final_level['name'], reward[1], reward[0])