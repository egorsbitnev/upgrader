import urllib.request
import json

url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/crates.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

# Pick 6 iconic cases
targets = [
    {"search": "Kilowatt Case", "ru_name": "Кейс «Киловатт»", "price": 250},
    {"search": "Revolution Case", "ru_name": "Кейс «Революция»", "price": 180},
    {"search": "Dreams & Nightmares Case", "ru_name": "Кейс «Грёзы и кошмары»", "price": 150},
    {"search": "Fracture Case", "ru_name": "Кейс «Разлом»", "price": 120},
    {"search": "Clutch Case", "ru_name": "Кейс «Решающий момент»", "price": 90},
    {"search": "Operation Bravo Case", "ru_name": "Кейс операции «Браво»", "price": 3500}
]

cases_list = []
for t in targets:
    match = next((c for c in data if t["search"].lower() in c.get("name", "").lower()), None)
    if match:
        # process items inside case
        items = []
        for it in match.get("contains", []):
            rarity_id = "milspec"
            rarity_obj = it.get("rarity", {})
            r_name = rarity_obj.get("name", "").lower() if isinstance(rarity_obj, dict) else ""
            if "covert" in r_name:
                rarity_id = "covert"
            elif "classified" in r_name:
                rarity_id = "classified"
            elif "restricted" in r_name:
                rarity_id = "restricted"
            elif "extraordinary" in r_name or "gold" in r_name:
                rarity_id = "gold"

            # assign price approximation based on rarity
            base_price = 15
            if rarity_id == "restricted": base_price = 70
            elif rarity_id == "classified": base_price = 350
            elif rarity_id == "covert": base_price = 2200
            elif rarity_id == "gold": base_price = 18000

            full_name = it.get("name", "")
            parts = full_name.split(" | ")
            weapon_type = parts[0] if len(parts) > 1 else "Оружие"
            skin_name = parts[1] if len(parts) > 1 else full_name

            items.append({
                "id": it.get("id"),
                "name": skin_name,
                "type": weapon_type,
                "price": base_price,
                "rarity": rarity_id,
                "image": it.get("image")
            })

        # Add rare special item (knife/gloves) to each case
        items.append({
            "id": f"knife-{match['id']}",
            "name": "★ Редкий особый предмет (Нож)",
            "type": "★ Нож / Перчатки",
            "price": 25000,
            "rarity": "gold",
            "image": "https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XuWbwcuyMESA4Fdl-4nnpU7iQA3-kKnr8ytd6s2lfa9_Kb6VXmPGwuogsbNvSyi3zR4jsTnQztyqdS6QP1IoXpoiEeAC5Be5l9CxKaq8sIvgdE5J"
        })

        cases_list.append({
            "id": match.get("id"),
            "name": t["ru_name"],
            "price": t["price"],
            "image": match.get("image"),
            "items": items
        })

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\cases.json", "w", encoding="utf-8") as f:
    json.dump(cases_list, f, ensure_ascii=False, indent=2)

print(f"Saved {len(cases_list)} cases with their loot tables!")
