with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add CSS for sell buttons
sell_css = """
    /* SELL SKINS STYLES */
    .mini-card-sell-btn {
      margin-top: 4px;
      width: 100%;
      padding: 3px 0;
      background: #22151c;
      border: 1px solid #7f1d1d;
      color: #fca5a5;
      font-size: 9px;
      font-weight: 800;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s;
    }
    .mini-card-sell-btn:hover {
      background: #991b1b;
      color: #fff;
    }
    .sell-all-btn {
      background: #7f1d1d;
      border: none;
      color: #fff;
      font-size: 10px;
      font-weight: 800;
      padding: 2px 7px;
      border-radius: 4px;
      cursor: pointer;
      margin-left: 6px;
    }
    .sell-all-btn:hover {
      background: #b91c1c;
    }
"""

html = html.replace("/* SKIN CARDS (CLEAN UPGRADER LOOK) */", sell_css + "\n    /* SKIN CARDS (CLEAN UPGRADER LOOK) */")

# Add "Sell All" button to Inventory Panel Header
old_inv_header = """          <div class="panel-header">
            <span class="panel-title">🎒 Инвентарь</span>
            <span class="panel-badge"><span id="invCount">0</span> предм.</span>
          </div>"""

new_inv_header = """          <div class="panel-header">
            <span class="panel-title">🎒 Инвентарь</span>
            <div style="display: flex; align-items: center;">
              <span class="panel-badge"><span id="invCount">0</span> предм.</span>
              <button class="sell-all-btn" title="Продать все скины" onclick="sellAllSkins()">Продать все</button>
            </div>
          </div>"""

html = html.replace(old_inv_header, new_inv_header)

# Add sellSkin and sellAllSkins methods & update renderInventory
sell_js = """
    function sellSkin(uid, event) {
      if (event) event.stopPropagation();
      const idx = state.inventory.findIndex(it => it.uid === uid);
      if (idx === -1) return;

      const item = state.inventory[idx];
      const payout = item.price;

      state.balance += payout;
      state.inventory.splice(idx, 1);

      // If current selected source was this item, reset to coin bet
      if (state.selectedSource && state.selectedSource.uid === uid) {
        state.selectedSource = null;
        selectCoinBet(state.coinBet || 100);
      }

      AudioEngine.playCoins();
      updateBalance();
      renderInventory();
      renderMarket();
      recalcChance();
    }

    function sellAllSkins() {
      if (state.inventory.length === 0) {
        alert("Инвентарь пуст!");
        return;
      }

      const totalVal = state.inventory.reduce((acc, it) => acc + it.price, 0);
      if (!confirm(`Продать все ${state.inventory.length} предметов за 🪙 ${totalVal.toLocaleString('ru-RU')} монет?`)) {
        return;
      }

      state.balance += totalVal;
      state.inventory = [];
      state.selectedSource = null;
      selectCoinBet(state.coinBet || 100);

      AudioEngine.playCoins();
      updateBalance();
      renderInventory();
      renderMarket();
      recalcChance();
    }
"""

# Inject sell functions before renderInventory
html = html.replace("function renderInventory() {", sell_js + "\n    function renderInventory() {")

# Update renderInventory card template to include Sell button
old_inv_card = """      state.inventory.forEach(item => {
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${item.uid}`;
        card.className = `mini-card rare-${item.rarity} ${isSelected ? 'selected' : ''}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${item.image}" alt="${item.name}" loading="lazy">
          </div>
          <div class="mini-card-name">${item.name}</div>
          <div class="mini-card-type">${item.type}</div>
          <div class="mini-card-price">🪙 ${item.price.toLocaleString('ru-RU')}</div>
        `;
        grid.appendChild(card);
      });"""

new_inv_card = """      state.inventory.forEach(item => {
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${item.uid}`;
        card.className = `mini-card rare-${item.rarity} ${isSelected ? 'selected' : ''}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${item.image}" alt="${item.name}" loading="lazy">
          </div>
          <div class="mini-card-name">${item.name}</div>
          <div class="mini-card-type">${item.type}</div>
          <div class="mini-card-price">🪙 ${item.price.toLocaleString('ru-RU')}</div>
          <button class="mini-card-sell-btn" onclick="sellSkin(${item.uid}, event)">Продать</button>
        `;
        grid.appendChild(card);
      });"""

html = html.replace(old_inv_card, new_inv_card)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added skin selling logic and UI to index.html successfully!")
