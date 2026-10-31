with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace buildReels and spinCase with super lightweight and rock-solid implementation
new_reels_and_spin = """    let multiTapeData = [];

    function buildReels(count) {
      const area = document.getElementById('reelsArea');
      if (!area) return;
      area.innerHTML = '';
      multiTapeData = [];

      const pool = (state.activeCase && state.activeCase.items) ? state.activeCase.items : [];
      if (pool.length === 0) return;

      const frag = document.createDocumentFragment();

      for (let r = 0; r < count; r++) {
        const reelRow = document.createElement('div');
        reelRow.className = 'single-reel-row';

        const pointer = document.createElement('div');
        pointer.className = 'reel-pointer';
        reelRow.appendChild(pointer);

        const track = document.createElement('div');
        track.className = 'reel-track';
        track.id = `reel-track-${r}`;

        const tapeItems = [];
        let innerHtml = '';

        // 38 items is optimal and super fast to render
        for (let i = 0; i < 38; i++) {
          const item = rollRandomItem(pool);
          tapeItems.push(item);
          innerHtml += `<div class="reel-item rare-${item.rarity}"><div class="reel-item-img"><img src="${item.image}" alt="${item.name}"></div><div class="reel-item-name">${item.name}</div></div>`;
        }

        track.innerHTML = innerHtml;
        multiTapeData.push(tapeItems);
        reelRow.appendChild(track);
        frag.appendChild(reelRow);
      }

      area.appendChild(frag);
    }

    function populateTape(caseData) {
      buildReels(selectedCaseQty || 1);
    }

    function spinCase() {
      if (state.isOpeningCase || !state.activeCase) return;
      const count = selectedCaseQty;
      const totalCost = state.activeCase.price * count;

      if (state.balance < totalCost) {
        alert("Недостаточно монет! Нажмите '+' возле баланса.");
        return;
      }

      state.balance -= totalCost;
      updateBalance();

      state.isOpeningCase = true;
      const openBtn = document.getElementById('caseOpenSelectedBtn');
      if (openBtn) openBtn.disabled = true;

      // Ensure reels are ready
      if (!multiTapeData || multiTapeData.length !== count) {
        buildReels(count);
      }

      const itemWidth = 80;
      const firstRow = document.querySelector('.single-reel-row');
      const containerWidth = firstRow ? firstRow.offsetWidth : 360;

      const wonItems = [];
      let totalValue = 0;

      // Calculate winning targets (around index 32)
      const winIndex = 32;

      for (let r = 0; r < count; r++) {
        const tape = multiTapeData[r];
        const wonSkin = (tape && tape[winIndex]) ? tape[winIndex] : state.activeCase.items[0];
        const wonItem = { uid: Date.now() + r + Math.random(), ...wonSkin };
        wonItems.push(wonItem);
        state.inventory.unshift(wonItem);
        totalValue += wonItem.price;

        const jitter = (Math.random() * 26) - 13;
        const targetOffset = (winIndex * itemWidth) + (itemWidth / 2) - (containerWidth / 2) + jitter;
        const duration = (4.0 + Math.random() * 0.4).toFixed(2);

        const track = document.getElementById(`reel-track-${r}`);
        if (track) {
          track.style.transition = `transform ${duration}s cubic-bezier(0.12, 0.85, 0.22, 1)`;
          track.style.transform = `translateX(-${targetOffset}px)`;
        }
      }

      AudioEngine.playRollStart();

      let tickCount = 0;
      const maxTicks = 28;
      let tickInterval = 70;
      function runTicks() {
        if (tickCount < maxTicks && state.isOpeningCase) {
          AudioEngine.playTick(1.2);
          tickCount++;
          tickInterval = Math.min(280, tickInterval * 1.08);
          setTimeout(runTicks, tickInterval);
        }
      }
      setTimeout(runTicks, 100);

      setTimeout(() => {
        state.isOpeningCase = false;
        document.getElementById('caseModal').style.display = 'none';

        updateBalance();
        renderInventory();
        renderMarket();
        AudioEngine.playWin();

        if (count === 1) {
          showUpgradeResult(true);
          const singleWon = wonItems[0];
          document.getElementById('resTitle').textContent = '🎁 ВЫПАЛ СКИН!';
          document.getElementById('resImg').src = singleWon.image;
          document.getElementById('resName').textContent = `${singleWon.type} | ${singleWon.name}`;
          document.getElementById('resPrice').textContent = `🪙 +${singleWon.price.toLocaleString('ru-RU')}`;
        } else {
          const modal = document.getElementById('multiCaseModal');
          const grid = document.getElementById('multiCaseGrid');
          const title = document.getElementById('multiModalTitle');
          const totalEl = document.getElementById('multiModalTotal');

          title.textContent = `🎁 ДРОП ИЗ ${count} КЕЙСОВ`;
          totalEl.textContent = `+🪙 ${totalValue.toLocaleString('ru-RU')}`;
          grid.innerHTML = '';

          wonItems.forEach(item => {
            const card = document.createElement('div');
            card.className = `mini-card rare-${item.rarity}`;
            card.innerHTML = `
              <div class="mini-card-img">
                <img src="${item.image}" alt="${item.name}">
              </div>
              <div class="mini-card-name">${item.name}</div>
              <div class="mini-card-price">🪙 ${item.price.toLocaleString('ru-RU')}</div>
            `;
            grid.appendChild(card);
          });

          modal.style.display = 'flex';
        }
      }, 4600);
    }"""

start_str = "let multiTapeData = [];"
end_str = "function closeMultiCaseModal()"
s_idx = html.find(start_str)
e_idx = html.find(end_str)

html = html[:s_idx] + new_reels_and_spin + "\n\n    " + html[e_idx:]

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Optimized DOM generation and fixed freeze on spin!")
