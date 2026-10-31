with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update recalcChance: chance must be <= 85%
old_rule2 = """      // RULE 2: Minimum chance must be at least 85%
      if (chance < 85) {
        btn.disabled = true;
        btn.textContent = "НУЖЕН ШАНС ОТ 85%";
      } else if (!state.selectedSource && state.balance < state.coinBet) {
        btn.disabled = true;
        btn.textContent = "НЕДОСТАТОЧНО МОНЕТ";
      } else {
        btn.disabled = false;
        btn.textContent = "СДЕЛАТЬ АПГРЕЙД";
      }"""

new_rule2 = """      // RULE 2: Maximum chance must be UP TO 85% (chance <= 85%)
      if (chance > 85) {
        btn.disabled = true;
        btn.textContent = "МАКС. ШАНС ДО 85%";
      } else if (!state.selectedSource && state.balance < state.coinBet) {
        btn.disabled = true;
        btn.textContent = "НЕДОСТАТОЧНО МОНЕТ";
      } else {
        btn.disabled = false;
        btn.textContent = "СДЕЛАТЬ АПГРЕЙД";
      }"""

html = html.replace(old_rule2, new_rule2)

# 2. Update startUpgrade validation
old_start_check = """      let checkChance = (sourceVal / targetVal) * 95;
      if (checkChance < 85) {
        alert("Минимальный шанс для апгрейда должен быть не менее 85%!");
        return;
      }"""

new_start_check = """      let checkChance = (sourceVal / targetVal) * 95;
      if (checkChance > 85) {
        alert("Шанс для апгрейда должен быть не более 85%!");
        return;
      }"""

html = html.replace(old_start_check, new_start_check)

# 3. Update market card dimming logic:
# Skin is too easy / over 85% if (curSourceVal / skin.price) * 95 > 85
old_card_check = """        const skinChance = (curSourceVal / skin.price) * 95;
        const isTooLowChance = skinChance < 85;

        card.className = `mini-card rare-${skin.rarity} ${isSelected ? 'target-selected' : ''}`;
        if (isTooLowChance) {
          card.style.opacity = '0.45';
        }"""

new_card_check = """        const skinChance = (curSourceVal / skin.price) * 95;
        const isTooHighChance = skinChance > 85;

        card.className = `mini-card rare-${skin.rarity} ${isSelected ? 'target-selected' : ''}`;
        if (isTooHighChance) {
          card.style.opacity = '0.45';
        }"""

html = html.replace(old_card_check, new_card_check)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Changed chance rule to MAX 85% (chance <= 85%)!")
