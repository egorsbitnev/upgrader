with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Filter out all skins with price <= curSourceVal in renderMarket
old_market_fn = """function renderMarket() {
      const grid = document.getElementById('marketGrid');
      grid.innerHTML = '';
      
      const filtered = CATALOG.filter(skin => {
        if (state.currentFilter === 'knife') return skin.type.includes('Нож') || skin.type.includes('Керамбит') || skin.type.includes('перчатки');
        if (state.currentFilter === 'rifle') return skin.type.includes('AK-47') || skin.type.includes('M4A') || skin.type.includes('AWP');
        if (state.currentFilter === 'pistol') return skin.type.includes('P250') || skin.type.includes('Glock') || skin.type.includes('USP') || skin.type.includes('Eagle');
        if (state.currentFilter === 'cheap') return skin.price <= 1000;
        return true;
      });

      const curSourceVal = getSourceValue();
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
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${skin.image}" alt="${skin.name}" loading="lazy">
          </div>
          <div class="mini-card-name">${skin.name}</div>
          <div class="mini-card-type">${skin.type}</div>
          <div class="mini-card-price">🪙 ${skin.price.toLocaleString('ru-RU')}</div>
        `;
        grid.appendChild(card);
      });
    }"""

new_market_fn = """function renderMarket() {
      const grid = document.getElementById('marketGrid');
      grid.innerHTML = '';
      const curSourceVal = getSourceValue();
      
      // Filter by category AND strictly exclude any skin cheaper than or equal to current bet
      const filtered = CATALOG.filter(skin => {
        // Exclude skins cheaper than or equal to current bet
        if (skin.price <= curSourceVal) return false;

        if (state.currentFilter === 'knife') return skin.type.includes('Нож') || skin.type.includes('Керамбит') || skin.type.includes('перчатки');
        if (state.currentFilter === 'rifle') return skin.type.includes('AK-47') || skin.type.includes('M4A') || skin.type.includes('AWP');
        if (state.currentFilter === 'pistol') return skin.type.includes('P250') || skin.type.includes('Glock') || skin.type.includes('USP') || skin.type.includes('Eagle');
        if (state.currentFilter === 'cheap') return skin.price <= 1000;
        return true;
      });

      // Update counter in market header
      const mCount = document.getElementById('marketCount');
      if (mCount) mCount.textContent = filtered.length;

      if (filtered.length === 0) {
        grid.innerHTML = '<div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); font-size: 11px; padding: 20px;">Нет доступных скинов дороже вашей ставки</div>';
        return;
      }

      // If current target is now cheaper than current bet, auto-switch to first valid skin
      if (state.selectedTarget && state.selectedTarget.price <= curSourceVal) {
        selectTarget(filtered[0]);
      }

      filtered.forEach(skin => {
        const isSelected = state.selectedTarget && state.selectedTarget.id === skin.id;
        const card = document.createElement('div');
        card.id = `target-card-${skin.id}`;
        
        const skinChance = (curSourceVal / skin.price) * 95;
        const isTooLowChance = skinChance < 85;

        card.className = `mini-card rare-${skin.rarity} ${isSelected ? 'target-selected' : ''}`;
        if (isTooLowChance) {
          card.style.opacity = '0.45';
        }
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${skin.image}" alt="${skin.name}" loading="lazy">
          </div>
          <div class="mini-card-name">${skin.name}</div>
          <div class="mini-card-type">${skin.type}</div>
          <div class="mini-card-price">🪙 ${skin.price.toLocaleString('ru-RU')}</div>
        `;
        grid.appendChild(card);
      });
    }"""

html = html.replace(old_market_fn, new_market_fn)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updated renderMarket to strictly hide skins <= current bet value!")
