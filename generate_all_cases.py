import urllib.request
import json
import random

url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/crates.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
print("Downloading cases list...")
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

all_cases = [c for c in data if c.get('type') == 'Case' and len(c.get('contains', [])) > 0]
print(f"Found {len(all_cases)} official CS2 cases.")

# Famous case prices
case_prices = {
    "weapon case": 7500,
    "bravo": 3800,
    "hydra": 1800,
    "cobblestone": 85000,
    "breakout": 450,
    "huntsman": 650,
    "phoenix": 350,
    "vanguard": 300,
    "glove": 550,
    "gamma": 220,
    "chroma": 190,
    "spectrum": 210,
    "clutch": 90,
    "horizon": 80,
    "danger zone": 75,
    "prisma": 85,
    "cs20": 95,
    "fracture": 120,
    "snakebite": 90,
    "riptide": 480,
    "dreams & nightmares": 150,
    "recoil": 140,
    "revolution": 180,
    "kilowatt": 250,
    "gallery": 320
}

knife_images = [
    "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XuWbwcuyMESA4Fdl-4nnpU7iQA3-kKnr8ytd6s2lfa9_Kb6VXmPGwuogsbNvSyi3zR4jsTnQztyqdS6QP1IoXpoiEeAC5Be5l9CxKaq8sIvgdE5J",
    "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGIGz3UqlXOLrxM-vMGmW8VNxu5Dx60noTyLkjYbf7itX6vytbbZSI-WsG3SA_u1jpN5lRi67gVNz4G7Qm938cS_Da1AhXpB1EeVb4xm4mtDjN7vj4A3b2NpGyCr52i4Y8G81tMzdoYZ7",
    "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XuWbwcuyMESA4Fdl-4nnpU7iQA3-kKnr8ytd6s29Y6FhJeScACnDkL8j6LU8GS3mwUh24G-Bno2tIymeblMgC5R3F-ECsBK6k4XuN-Lh-UWA3P3GyEv9"
]

processed_cases = []

for c in all_cases:
    c_name = c.get('name', '')
    img = c.get('image', '')
    if not img:
        continue

    # Determine price
    price = 150
    for key, p in case_prices.items():
        if key in c_name.lower():
            price = p
            break

    # Process skins inside
    items = []
    for it in c.get('contains', []):
        r_obj = it.get('rarity', {})
        r_name = r_obj.get('name', '').lower() if isinstance(r_obj, dict) else ''
        
        rarity = 'milspec'
        item_price = random.randint(15, 35)
        if 'covert' in r_name:
            rarity = 'covert'
            item_price = random.randint(950, 4500)
        elif 'classified' in r_name:
            rarity = 'classified'
            item_price = random.randint(220, 850)
        elif 'restricted' in r_name:
            rarity = 'restricted'
            item_price = random.randint(55, 180)
        elif 'extraordinary' in r_name or 'gold' in r_name:
            rarity = 'gold'
            item_price = random.randint(14000, 48000)

        full_name = it.get('name', '')
        parts = full_name.split(' | ')
        w_type = parts[0] if len(parts) > 1 else 'Оружие'
        s_name = parts[1] if len(parts) > 1 else full_name

        items.append({
            "id": it.get('id'),
            "name": s_name,
            "type": w_type,
            "price": item_price,
            "rarity": rarity,
            "image": it.get('image')
        })

    # Add rare special knife to every case
    items.append({
        "id": f"gold-{c.get('id')}",
        "name": "★ Редкий нож / перчатки",
        "type": "★ Special Item",
        "price": random.randint(18000, 52000),
        "rarity": "gold",
        "image": random.choice(knife_images)
    })

    processed_cases.append({
        "id": c.get('id'),
        "name": c_name.replace("CS:GO ", "").replace("Weapon Case", "Кейс"),
        "price": price,
        "image": img,
        "items": items
    })

# Sort by price descending
processed_cases.sort(key=lambda x: x["price"], reverse=True)

print(f"Prepared {len(processed_cases)} complete cases with loot tables!")

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\cases.json", "w", encoding="utf-8") as f:
    json.dump(processed_cases, f, ensure_ascii=False, indent=2)

print("Saved complete cases.json!")
