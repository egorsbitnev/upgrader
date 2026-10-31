import urllib.request
import json
import random

url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/skins.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print("Downloading CS2 skins database from ByMykel API...")
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print(f"Total raw skins: {len(data)}")

# Rarity price tier multipliers realistic to Steam Market / Upgrader.best
tier_pricing = {
    "covert": (800, 15000),
    "classified": (150, 950),
    "restricted": (40, 220),
    "milspec": (10, 45),
    "gold": (12000, 95000)
}

# Famous expensive god-tier skins overrides
god_tier = {
    "Dragon Lore": 95000,
    "Gungnir": 85000,
    "Howl": 75000,
    "Fire Serpent": 28000,
    "Medusa": 36000,
    "Wild Lotus": 68000,
    "Gold Arabesque": 42000,
    "Printstream": 3200,
    "Vulcan": 4500,
    "Asiimov": 3800,
    "Case Hardened": 5500,
    "Doppler": 22000,
    "Fade": 34000,
    "Gamma Doppler": 25000,
    "Tiger Tooth": 16000,
    "Marble Fade": 28000,
    "Crimson Web": 19000,
    "Slaughter": 21000,
    "Lore": 24000,
    "Vice": 48000,
    "Pandora's Box": 75000,
    "King Snake": 32000,
    "Amphibious": 26000,
    "Spearmint": 45000
}

curated = []
seen_names = set()

# Filter out pure low-tier duplicates, select top weapons, knives, gloves, classified & covert
for s in data:
    name = s.get('name', '')
    if not name or name in seen_names:
        continue
    
    cat = s.get('category', {}).get('id', '')
    is_knife = cat == 'sfui_invpanel_filter_melee'
    is_glove = cat == 'sfui_invpanel_filter_gloves'
    
    rarity_name = s.get('rarity', {}).get('name', '').lower()
    
    rarity = 'milspec'
    if is_knife or is_glove or 'extraordinary' in rarity_name:
        rarity = 'gold'
    elif 'covert' in rarity_name:
        rarity = 'covert'
    elif 'classified' in rarity_name:
        rarity = 'classified'
    elif 'restricted' in rarity_name:
        rarity = 'restricted'

    # Filter out trash milspecs (only keep iconic weapons)
    weapon_name = s.get('weapon', {}).get('name', '')
    is_top_weapon = any(w in weapon_name.lower() for w in ['ak-47', 'm4a4', 'm4a1-s', 'awp', 'desert eagle', 'usp-s', 'glock-18'])

    # Skip boring low tier skins to keep market premium
    if rarity in ['milspec', 'restricted'] and not is_top_weapon:
        continue

    # Clean name
    clean_name = name.replace("★ ", "").replace("StatTrak™ ", "")
    parts = clean_name.split(" | ")
    w_type = parts[0] if len(parts) > 1 else weapon_name
    s_name = parts[1] if len(parts) > 1 else clean_name

    # Calculate realistic price
    base_price = 100
    for gt, price in god_tier.items():
        if gt.lower() in clean_name.lower():
            base_price = price
            break
    else:
        if rarity == 'gold':
            base_price = random.randint(14000, 48000)
        elif rarity == 'covert':
            base_price = random.randint(950, 4200)
        elif rarity == 'classified':
            base_price = random.randint(220, 850)
        elif rarity == 'restricted':
            base_price = random.randint(60, 200)
        else:
            base_price = random.randint(25, 55)

    curated.append({
        "id": s.get("id"),
        "type": w_type,
        "name": s_name,
        "price": base_price,
        "rarity": rarity,
        "image": s.get("image")
    })
    seen_names.add(name)

# Sort by price ascending
curated.sort(key=lambda x: x["price"])

print(f"Generated {len(curated)} premium CS2 skins catalog (no junk).")

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\catalog.json", "w", encoding="utf-8") as f:
    json.dump(curated, f, ensure_ascii=False, indent=2)

print("Saved clean catalog.json!")
