with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS for dynamic multi-tape reels
multi_tape_css = """
    /* MULTI-TAPE CONTAINER STYLES (SIMULTANEOUS SPINS) */
    .reels-scroll-area {
      width: 100%;
      max-height: 52vh;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin: 8px 0;
      padding-right: 2px;
    }
    .reels-scroll-area::-webkit-scrollbar {
      width: 4px;
    }
    .reels-scroll-area::-webkit-scrollbar-thumb {
      background: #2563eb;
      border-radius: 4px;
    }
    .single-reel-row {
      width: 100%;
      height: 72px;
      background: #090c14;
      border: 1px solid var(--border);
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      flex-shrink: 0;
    }
    .reel-track {
      display: flex;
      height: 100%;
      position: absolute;
      left: 0; top: 0;
      will-change: transform;
    }
    .reel-pointer {
      position: absolute;
      top: 0; bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 2px;
      background: var(--accent-yellow);
      z-index: 10;
    }
    .reel-pointer::before {
      content: '';
      position: absolute;
      top: 0; left: 50%;
      transform: translateX(-50%);
      border-left: 5px solid transparent;
      border-right: 5px solid transparent;
      border-top: 6px solid var(--accent-yellow);
    }
    .reel-item {
      width: 80px;
      height: 100%;
      background: #111722;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 3px;
      flex-shrink: 0;
      box-sizing: border-box;
    }
    .reel-item.rare-gold { border-bottom: 2px solid #ffd700; }
    .reel-item.rare-covert { border-bottom: 2px solid #eb4b4b; }
    .reel-item.rare-classified { border-bottom: 2px solid #d32ce6; }
    .reel-item.rare-restricted { border-bottom: 2px solid #8847ff; }
    .reel-item.rare-milspec { border-bottom: 2px solid #4b69ff; }
    .reel-item-img {
      width: 42px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .reel-item-img img {
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }
    .reel-item-name {
      font-size: 8px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      text-align: center;
      margin-top: 1px;
    }
"""

html = html.replace("/* CASE MODAL */", multi_tape_css + "\n    /* CASE MODAL */")

# 2. Update caseModal HTML: replace single tape-container with dynamic reels-scroll-area
old_tape_html = """      <div class="tape-container">
        <div class="tape-pointer"></div>
        <div class="tape-track" id="tapeTrack"></div>
      </div>"""

new_tape_html = """      <!-- Dynamic multi-reels scroll area: shows 1 to 10 spinning tapes -->
      <div class="reels-scroll-area" id="reelsArea"></div>"""

html = html.replace(old_tape_html, new_tape_html)

# Adjust caseModalBox max-width so multiple tapes fit comfortably
html = html.replace("max-width: 380px;", "max-width: 460px;")

# 3. Replace JS populateTape & spinCase with multi-tape simultaneous generation and spinning
old_populate_and_spin = """    function populateTape(caseData) {
      const track = document.getElementById('tapeTrack');
      track.style.transition = 'none';
      track.style.transform = 'translateX(0px)';
      track.innerHTML = '';

      generatedItemsTape = [];
      const pool = caseData.items;

      for (let i = 0; i < 50; i++) {
        const item = rollRandomItem(pool);
        generatedItemsTape.push(item);

        const el = document.createElement('div');
        el.className = `tape-item rare-${item.rarity}`;
        el.innerHTML = `
          <div class="tape-item-img">
            <img src="${item.image}" alt="${item.name}">
          </div>
          <div class="tape-item-name">${item.name}</div>
        `;
        track.appendChild(el);
      }
    }"""

new_populate_and_spin = """    let multiTapeData = []; // Array of arrays of 50 items for each spinning reel

    function buildReels(count) {
      const area = document.getElementById('reelsArea');
      area.innerHTML = '';
      multiTapeData = [];

      const pool = state.activeCase ? state.activeCase.items : [];
      if (!pool || pool.length === 0) return;

      for (let r = 0; r < count; r++) {
        const reelRow = document.createElement('div');
        reelRow.className = 'single-reel-row';
        reelRow.id = `reel-row-${r}`;

        const pointer = document.createElement('div');
        pointer.className = 'reel-pointer';
        reelRow.appendChild(pointer);

        const track = document.createElement('div');
        track.className = 'reel-track';
        track.id = `reel-track-${r}`;

        const tapeItems = [];
        for (let i = 0; i < 50; i++) {
          const item = rollRandomItem(pool);
          tapeItems.push(item);

          const el = document.createElement('div');
          el.className = `reel-item rare-${item.rarity}`;
          el.innerHTML = `
            <div class="reel-item-img">
              <img src="${item.image}" alt="${item.name}">
            </div>
            <div class="reel-item-name">${item.name}</div>
          `;
          track.appendChild(el);
        }

        multiTapeData.push(tapeItems);
        reelRow.appendChild(track);
        area.appendChild(reelRow);
      }
    }

    function populateTape(caseData) {
      buildReels(selectedCaseQty || 1);
    }"""

html = html.replace(old_populate_and_spin, new_populate_and_spin)

# When user changes case qty, rebuild reels live in modal
html = html.replace("updateCaseOpenBtn();\n    }", "updateCaseOpenBtn();\n      buildReels(selectedCaseQty);\n    }")

# 4. Update spinCase to spin all tracks simultaneously!
old_spin_case_all = """    function spinCase() {
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

      if (count === 1) {"""

# Replace entire spinCase function
spin_case_replacement = """    function spinCase() {
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

      // Re-ensure reels are populated
      if (multiTapeData.length !== count) {
        buildReels(count);
      }

      const itemWidth = 80;
      const containerWidth = document.querySelector('.single-reel-row') ? document.querySelector('.single-reel-row').offsetWidth : 400;

      const wonItems = [];
      let totalValue = 0;

      // Start spinning all reels at once with slight natural variances
      for (let r = 0; r < count; r++) {
        const track = document.getElementById(`reel-track-${r}`);
        if (!track) continue;

        const winIndex = 36;
        const wonSkin = multiTapeData[r][winIndex];
        const wonItem = { uid: Date.now() + r + Math.random(), ...wonSkin };
        wonItems.push(wonItem);
        state.inventory.unshift(wonItem);
        totalValue += wonItem.price;

        const jitter = (Math.random() * 30) - 15;
        const targetOffset = (winIndex * itemWidth) + (itemWidth / 2) - (containerWidth / 2) + jitter;

        // Vary spin duration slightly (4.3s - 4.8s) for ultra realistic feel
        const duration = (4.4 + Math.random() * 0.4).toFixed(2);
        track.style.transition = `transform ${duration}s cubic-bezier(0.1, 0.9, 0.2, 1)`;
        track.style.transform = `translateX(-${targetOffset}px)`;
      }

      AudioEngine.playRollStart();

      let caseElapsed = 0;
      let caseDelay = 65;
      function scheduleCaseTicks() {
        if (caseElapsed < 4200) {
          AudioEngine.playTick(1.2);
          caseElapsed += caseDelay;
          caseDelay = Math.min(320, caseDelay * 1.08);
          setTimeout(scheduleCaseTicks, caseDelay);
        }
      }
      setTimeout(scheduleCaseTicks, 100);

      // Finish when longest spin stops (~4.9s)
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
          // Render multi-result grid
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
      }, 5100);
    }"""

# Find spinCase function bounds and replace
start_idx = html.find("function spinCase()")
end_idx = html.find("function closeMultiCaseModal()")
# Also let's inspect where old spinCase ends
old_spin_sample = html[start_idx:start_idx+2800]
# replace old spinCase block
html = html[:start_idx] + spin_case_replacement + "\n\n    function closeMultiCaseModal() {\n      document.getElementById('multiCaseModal').style.display = 'none';\n    }\n" + html[html.find("function closeMultiCaseModal()") + len("function closeMultiCaseModal() {\n      document.getElementById('multiCaseModal').style.display = 'none';\n    }\n"):]

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added simultaneous multi-reels spinning animation for all 1-10 cases!")
