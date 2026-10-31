import json
import urllib.request

url = "https://raw.githubusercontent.com/ByMykel/CSGO-API/main/public/api/en/skins.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

print("Downloading skins list...")
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))

print(f"Loaded {len(data)} skins. Processing wanted items...")

wanted = [
    {"search": "P250 | Sand Dune", "name": "Песчаная буря", "type": "P250", "price": 10, "rarity": "milspec"},
    {"search": "Glock-18 | High Beam", "name": "Дальний свет", "type": "Glock-18", "price": 25, "rarity": "milspec"},
    {"search": "Glock-18 | Water Elemental", "name": "Водяной", "type": "Glock-18", "price": 60, "rarity": "classified"},
    {"search": "USP-S | Cortex", "name": "Извилины", "type": "USP-S", "price": 120, "rarity": "classified"},
    {"search": "USP-S | Printstream", "name": "Поток информации", "type": "USP-S", "price": 650, "rarity": "covert"},
    {"search": "Desert Eagle | Light Rail", "name": "Рельсотрон", "type": "Desert Eagle", "price": 90, "rarity": "restricted"},
    {"search": "Desert Eagle | Code Red", "name": "Код красного", "type": "Desert Eagle", "price": 280, "rarity": "covert"},
    {"search": "Desert Eagle | Printstream", "name": "Поток информации", "type": "Desert Eagle", "price": 750, "rarity": "covert"},
    {"search": "M4A4 | Neo-Noir", "name": "Нео-нуар", "type": "M4A4", "price": 450, "rarity": "covert"},
    {"search": "M4A4 | The Emperor", "name": "Император", "type": "M4A4", "price": 950, "rarity": "covert"},
    {"search": "M4A4 | Howl", "name": "Вой", "type": "M4A4", "price": 85000, "rarity": "contraband"},
    {"search": "M4A1-S | Hyper Beast", "name": "Скоростной зверь", "type": "M4A1-S", "price": 800, "rarity": "covert"},
    {"search": "M4A1-S | Player Two", "name": "Второй игрок", "type": "M4A1-S", "price": 1400, "rarity": "covert"},
    {"search": "M4A1-S | Printstream", "name": "Поток информации", "type": "M4A1-S", "price": 2400, "rarity": "covert"},
    {"search": "AK-47 | Slate", "name": "Фантомный вредитель", "type": "AK-47", "price": 150, "rarity": "restricted"},
    {"search": "AK-47 | Redline", "name": "Красная линия", "type": "AK-47", "price": 350, "rarity": "classified"},
    {"search": "AK-47 | Asiimov", "name": "Азимов", "type": "AK-47", "price": 1600, "rarity": "covert"},
    {"search": "AK-47 | Vulcan", "name": "Вулкан", "type": "AK-47", "price": 2800, "rarity": "covert"},
    {"search": "AK-47 | Case Hardened", "name": "Поверхностная закалка", "type": "AK-47", "price": 4500, "rarity": "classified"},
    {"search": "AK-47 | Fire Serpent", "name": "Огненный змей", "type": "AK-47", "price": 16000, "rarity": "covert"},
    {"search": "AWP | Atheris", "name": "Древесная гадюка", "type": "AWP", "price": 95, "rarity": "restricted"},
    {"search": "AWP | Mortis", "name": "Мортис", "type": "AWP", "price": 180, "rarity": "classified"},
    {"search": "AWP | Wildfire", "name": "Дикое пламя", "type": "AWP", "price": 1900, "rarity": "covert"},
    {"search": "AWP | Asiimov", "name": "Азимов", "type": "AWP", "price": 3100, "rarity": "covert"},
    {"search": "AWP | Oni Taiji", "name": "Они Тайдзи", "type": "AWP", "price": 6800, "rarity": "covert"},
    {"search": "AWP | Medusa", "name": "Медуза", "type": "AWP", "price": 36000, "rarity": "covert"},
    {"search": "AWP | Dragon Lore", "name": "История о драконе", "type": "AWP", "price": 95000, "rarity": "covert"},
    {"search": "AWP | Gungnir", "name": "Гунгнир", "type": "AWP", "price": 110000, "rarity": "covert"},
    {"search": "Karambit | Doppler", "name": "Волны (Doppler)", "type": "Керамбит", "price": 18000, "rarity": "gold"},
    {"search": "Karambit | Fade", "name": "Градиент (Fade)", "type": "Керамбит", "price": 26000, "rarity": "gold"},
    {"search": "Butterfly Knife | Slaughter", "name": "Убийство (Slaughter)", "type": "Нож-бабочка", "price": 28000, "rarity": "gold"},
    {"search": "Butterfly Knife | Fade", "name": "Градиент (Fade)", "type": "Нож-бабочка", "price": 46000, "rarity": "gold"},
    {"search": "M9 Bayonet | Gamma Doppler", "name": "Гамма-волны", "type": "M9 Штык-нож", "price": 23000, "rarity": "gold"},
    {"search": "Skeleton Knife | Fade", "name": "Градиент (Fade)", "type": "Скелетный нож", "price": 24000, "rarity": "gold"},
    {"search": "Sport Gloves | Vice", "name": "Порок (Vice)", "type": "Спортивные перчатки", "price": 49000, "rarity": "gold"},
    {"search": "Specialist Gloves | Crimson Web", "name": "Кровавая паутина", "type": "Перчатки спецназа", "price": 15000, "rarity": "gold"}
]

catalog = []
for item in wanted:
    # Match in skins
    match = None
    for skin in data:
        s_name = skin.get('name', '')
        if item['search'].lower() in s_name.lower():
            match = skin
            break
    if match:
        catalog.append({
            "id": match.get('id', item['search'].replace(' ', '_').lower()),
            "type": item["type"],
            "name": item["name"],
            "price": item["price"],
            "rarity": item["rarity"],
            "image": match.get('image')
        })
        print(f"Matched: {item['type']} | {item['name']}")
    else:
        print(f"MISSING: {item['search']}")

out_path = r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\catalog.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Done! Saved {len(catalog)} skins to catalog.json")
