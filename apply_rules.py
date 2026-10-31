with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update recalcChance()
old_recalc = """      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      if (sourceVal >= targetVal) {
        chanceText.textContent = "100%";
        multText.textContent = "x1.00";
        winArc.style.strokeDashoffset = 0;
        btn.disabled = (!state.selectedSource && state.balance < state.coinBet);
        return;
      }

      // Standard casino house edge 95%
      let chance = (sourceVal / targetVal) * 95;
      if (chance > 95) chance = 95;
      if (chance < 0.2) chance = 0.2;

      const mult = (targetVal / sourceVal).toFixed(2);

      chanceText.textContent = chance.toFixed(1) + "%";
      multText.textContent = "x" + mult;

      // Arc offset proportional to actual win chance
      const offset = CIRCLE_CIRCUMFERENCE - (CIRCLE_CIRCUMFERENCE * (chance / 100));
      winArc.style.strokeDashoffset = offset;

      if (!state.selectedSource && state.balance < state.coinBet) {
        btn.disabled = true;
      } else {
        btn.disabled = false;
      }"""

new_recalc = """      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      // RULE 1: Cannot upgrade to skins cheaper than or equal to source
      if (targetVal <= sourceVal) {
        chanceText.textContent = "0%";
        multText.textContent = "x0.00";
        winArc.style.strokeDashoffset = CIRCLE_CIRCUMFERENCE;
        btn.disabled = true;
        btn.textContent = "ВЫБЕРИТЕ СКИН ДОРОЖЕ";
        return;
      }

      // Standard casino house edge 95%
      let chance = (sourceVal / targetVal) * 95;
      if (chance > 95) chance = 95;
      if (chance < 0.2) chance = 0.2;

      const mult = (targetVal / sourceVal).toFixed(2);

      chanceText.textContent = chance.toFixed(1) + "%";
      multText.textContent = "x" + mult;

      // Arc offset proportional to actual win chance
      const offset = CIRCLE_CIRCUMFERENCE - (CIRCLE_CIRCUMFERENCE * (chance / 100));
      winArc.style.strokeDashoffset = offset;

      // RULE 2: Minimum chance must be at least 85%
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

html = html.replace(old_recalc, new_recalc)

# 2. In startUpgrade: check rules as well
old_start = """      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      if (!state.selectedSource) {"""

new_start = """      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      if (targetVal <= sourceVal) {
        alert("Нельзя апгрейдить на скин дешевле вашей ставки!");
        return;
      }

      let checkChance = (sourceVal / targetVal) * 95;
      if (checkChance < 85) {
        alert("Минимальный шанс для апгрейда должен быть не менее 85%!");
        return;
      }

      if (!state.selectedSource) {"""

html = html.replace(old_start, new_start)

# 3. Add visual opacity / disable to market cards that don't meet criteria
old_render_market_card = """      filtered.forEach(skin => {
        const isSelected = state.selectedTarget && state.selectedTarget.id === skin.id;
        const card = document.createElement('div');
        card.id = `target-card-${skin.id}`;
        card.className = `mini-card rare-${skin.rarity} ${isSelected ? 'target-selected' : ''}`;
        card.onclick = () => selectTarget(skin);"""

new_render_market_card = """      const curSourceVal = getSourceValue();
      filtered.forEach(skin => {
        const isSelected = state.selectedTarget && state.selectedTarget.id === skin.id;
        const card = document.createElement('div');
        card.id = `target-card-${skin.id}`;
        
        // Check if skin is cheaper or chance < 85%
        const isCheaper = skin.price <= curSourceVal;
        const skinChance = (curSourceVal / skin.price) * 95;
        const isTooLowChance = skinChance < 85;
        const isInvalid = isCheaper || isTooLowChance;

        card.className = `mini-card rare-${skin.rarity} ${isSelected ? 'target-selected' : ''}`;
        if (isInvalid) {
          card.style.opacity = '0.45';
        }
        card.onclick = () => selectTarget(skin);"""

html = html.replace(old_render_market_card, new_render_market_card)

# Re-render market whenever source or coin bet changes so user sees eligible skins
html = html.replace("function selectSourceItem(item) {\n      AudioEngine.playClick();", "function selectSourceItem(item) {\n      AudioEngine.playClick();\n      setTimeout(renderMarket, 50);")
html = html.replace("function selectCoinBet(amount) {", "function selectCoinBet(amount) {\n      setTimeout(renderMarket, 50);")

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with restriction: target > source and chance >= 85%!")
