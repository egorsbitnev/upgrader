with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update CSS for quantity selector
qty_css = """
    /* CASE QUANTITY SELECTOR */
    .case-qty-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      background: #111723;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 4px 8px;
      margin-bottom: 10px;
    }
    .qty-btn {
      width: 28px;
      height: 28px;
      background: #1e283b;
      border: 1px solid var(--border);
      color: #fff;
      font-weight: 900;
      font-size: 14px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .qty-btn:active { background: #334155; }
    .qty-pills {
      display: flex;
      gap: 4px;
    }
    .qty-pill {
      padding: 3px 7px;
      font-size: 10px;
      font-weight: 800;
      background: #192233;
      border: 1px solid var(--border);
      border-radius: 4px;
      color: var(--text-muted);
      cursor: pointer;
    }
    .qty-pill.active {
      background: #2563eb;
      color: #fff;
      border-color: #2563eb;
    }
    .btn-open-selected {
      width: 100%;
      padding: 11px 0;
      background: linear-gradient(135deg, #00c74d, #009d3c);
      border: none;
      border-radius: 8px;
      color: #0b111a;
      font-size: 14px;
      font-weight: 900;
      cursor: pointer;
    }
    .btn-open-selected:disabled {
      background: #1e293b;
      color: #475569;
      cursor: not-allowed;
    }

    /* MULTI RESULT 1-10 GRID MODAL */
    .multi-res-modal {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(4px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1200;
      padding: 16px;
    }
    .multi-res-box {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      width: 100%;
      max-width: 440px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .multi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(85px, 1fr));
      gap: 6px;
      width: 100%;
      overflow-y: auto;
      max-height: 55vh;
      padding: 4px 0;
      margin: 8px 0;
    }
"""

html = html.replace("/* CASE MODAL */", qty_css + "\n    /* CASE MODAL */")

# 2. Update HTML of Case Modal to have dynamic 1-10 selector
old_modal_html = """      <div class="tape-container">
        <div class="tape-pointer"></div>
        <div class="tape-track" id="tapeTrack"></div>
      </div>

      <div class="case-actions">
        <button class="case-btn case-btn-1x" id="caseOpen1xBtn" onclick="spinCase(1)">1x</button>
        <button class="case-btn case-btn-10x" id="caseOpen10xBtn" onclick="spinCase(10)">⚡ 10x</button>
      </div>"""

new_modal_html = """      <div class="tape-container">
        <div class="tape-pointer"></div>
        <div class="tape-track" id="tapeTrack"></div>
      </div>

      <!-- Quantity Selector 1 - 10 -->
      <div class="case-qty-row">
        <div style="font-size: 11px; font-weight: 800; color: var(--text-muted);">Количество:</div>
        <div class="qty-pills">
          <div class="qty-pill active" onclick="setCaseQty(1, this)">1x</div>
          <div class="qty-pill" onclick="setCaseQty(2, this)">2x</div>
          <div class="qty-pill" onclick="setCaseQty(3, this)">3x</div>
          <div class="qty-pill" onclick="setCaseQty(5, this)">5x</div>
          <div class="qty-pill" onclick="setCaseQty(10, this)">10x</div>
        </div>
        <div style="display: flex; align-items: center; gap: 4px;">
          <button class="qty-btn" onclick="adjustCaseQty(-1)">-</button>
          <span style="font-size: 13px; font-weight: 900; min-width: 20px; text-align: center;" id="caseQtyVal">1</span>
          <button class="qty-btn" onclick="adjustCaseQty(1)">+</button>
        </div>
      </div>

      <button class="btn-open-selected" id="caseOpenSelectedBtn" onclick="spinCase()">
        ОТКРЫТЬ (1x) ЗА 🪙 250
      </button>"""

html = html.replace(old_modal_html, new_modal_html)

# 3. Add Multi-Drop Modal for counts > 1
multi_modal_html = """
  <!-- MULTI CASE DROPS MODAL (1-10 ITEMS) -->
  <div class="multi-res-modal" id="multiCaseModal">
    <div class="multi-res-box">
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-size: 14px; font-weight: 900;" id="multiModalTitle">🎁 ВЫПАВШИЕ СКИНЫ</span>
        <span style="font-size: 13px; font-weight: 800; color: var(--accent-yellow);" id="multiModalTotal">+🪙 0</span>
      </div>
      <div class="multi-grid" id="multiCaseGrid"></div>
      <button class="btn-open-selected" style="background:#2563eb; color:#fff;" onclick="closeMultiCaseModal()">ЗАБРАТЬ ВСЕ</button>
    </div>
  </div>
"""

html = html.replace("<!-- RESULT OVERLAY -->", multi_modal_html + "\n  <!-- RESULT OVERLAY -->")

# 4. Update JS for quantity state and dynamic spinCase
old_open_modal_js = """    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      document.getElementById('caseOpen1xBtn').textContent = `1x 🪙 ${caseData.price.toLocaleString('ru-RU')}`;
      document.getElementById('caseOpen10xBtn').textContent = `⚡ 10x 🪙 ${(caseData.price * 10).toLocaleString('ru-RU')}`;
      populateTape(caseData);
      document.getElementById('caseModal').style.display = 'flex';
    }"""

new_open_modal_js = """    let selectedCaseQty = 1;

    function setCaseQty(qty, el) {
      selectedCaseQty = Math.max(1, Math.min(10, qty));
      document.querySelectorAll('.qty-pill').forEach(p => p.classList.remove('active'));
      if (el) el.classList.add('active');
      updateCaseOpenBtn();
    }

    function adjustCaseQty(delta) {
      selectedCaseQty = Math.max(1, Math.min(10, selectedCaseQty + delta));
      document.querySelectorAll('.qty-pill').forEach(p => {
        p.classList.toggle('active', parseInt(p.textContent) === selectedCaseQty);
      });
      updateCaseOpenBtn();
    }

    function updateCaseOpenBtn() {
      const qVal = document.getElementById('caseQtyVal');
      if (qVal) qVal.textContent = selectedCaseQty;
      const btn = document.getElementById('caseOpenSelectedBtn');
      if (btn && state.activeCase) {
        const total = state.activeCase.price * selectedCaseQty;
        btn.textContent = `ОТКРЫТЬ (${selectedCaseQty}x) ЗА 🪙 ${total.toLocaleString('ru-RU')}`;
        btn.disabled = (state.balance < total);
      }
    }

    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      selectedCaseQty = 1;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      setCaseQty(1, document.querySelector('.qty-pill'));
      populateTape(caseData);
      document.getElementById('caseModal').style.display = 'flex';
    }"""

html = html.replace(old_open_modal_js, new_open_modal_js)

# 5. Update spinCase to support selectedCaseQty
old_spin_case_js = """    function spinCase(count = 1) {
      if (state.isOpeningCase || !state.activeCase) return;
      const totalCost = state.activeCase.price * count;

      if (state.balance < totalCost) {
        alert("Недостаточно монет! Нажмите '+' возле баланса.");
        return;
      }

      state.balance -= totalCost;
      updateBalance();

      state.isOpeningCase = true;
      document.getElementById('caseOpen1xBtn').disabled = true;
      document.getElementById('caseOpen10xBtn').disabled = true;

      const winIndex = 36;
      const wonSkin = generatedItemsTape[winIndex];

      const itemWidth = 90;
      const containerWidth = document.querySelector('.tape-container').offsetWidth;
      const jitter = (Math.random() * 40) - 20;
      const targetOffset = (winIndex * itemWidth) + (itemWidth / 2) - (containerWidth / 2) + jitter;

      const track = document.getElementById('tapeTrack');
      track.style.transition = 'transform 4.5s cubic-bezier(0.1, 0.9, 0.2, 1)';
      track.style.transform = `translateX(-${targetOffset}px)`;

      setTimeout(() => {
        state.isOpeningCase = false;
        document.getElementById('caseModal').style.display = 'none';

        const finalWonItem = { uid: Date.now(), ...wonSkin };
        state.inventory.unshift(finalWonItem);
        updateBalance();
        renderInventory();

        showUpgradeResult(true);
        document.getElementById('resTitle').textContent = '🎁 ВЫПАЛ СКИН!';
        document.getElementById('resImg').src = finalWonItem.image;
        document.getElementById('resName').textContent = `${finalWonItem.type} | ${finalWonItem.name}`;
        document.getElementById('resPrice').textContent = `🪙 +${finalWonItem.price.toLocaleString('ru-RU')}`;
      }, 4700);
    }"""

new_spin_case_js = """    function closeMultiCaseModal() {
      document.getElementById('multiCaseModal').style.display = 'none';
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

      if (count === 1) {
        // Single roll animation
        const winIndex = 36;
        const wonSkin = generatedItemsTape[winIndex];

        const itemWidth = 90;
        const containerWidth = document.querySelector('.tape-container').offsetWidth;
        const jitter = (Math.random() * 40) - 20;
        const targetOffset = (winIndex * itemWidth) + (itemWidth / 2) - (containerWidth / 2) + jitter;

        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 4.5s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = `translateX(-${targetOffset}px)`;
        AudioEngine.playRollStart();

        let caseElapsed = 0;
        let caseDelay = 70;
        function scheduleCaseTick() {
          if (caseElapsed < 4200) {
            AudioEngine.playTick(1.2);
            caseElapsed += caseDelay;
            caseDelay = Math.min(350, caseDelay * 1.08);
            setTimeout(scheduleCaseTick, caseDelay);
          }
        }
        setTimeout(scheduleCaseTick, 100);

        setTimeout(() => {
          state.isOpeningCase = false;
          document.getElementById('caseModal').style.display = 'none';

          const finalWonItem = { uid: Date.now(), ...wonSkin };
          state.inventory.unshift(finalWonItem);
          updateBalance();
          renderInventory();
          renderMarket();

          AudioEngine.playWin();
          showUpgradeResult(true);
          document.getElementById('resTitle').textContent = '🎁 ВЫПАЛ СКИН!';
          document.getElementById('resImg').src = finalWonItem.image;
          document.getElementById('resName').textContent = `${finalWonItem.type} | ${finalWonItem.name}`;
          document.getElementById('resPrice').textContent = `🪙 +${finalWonItem.price.toLocaleString('ru-RU')}`;
        }, 4700);

      } else {
        // Quick spin preview for multi-cases (2 to 10)
        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 1.4s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = 'translateX(-1600px)';
        AudioEngine.playRollStart();

        setTimeout(() => {
          state.isOpeningCase = false;
          document.getElementById('caseModal').style.display = 'none';

          const wonItems = [];
          let totalValue = 0;
          for (let i = 0; i < count; i++) {
            const it = rollRandomItem(state.activeCase.items);
            const won = { uid: Date.now() + i + Math.random(), ...it };
            wonItems.push(won);
            state.inventory.unshift(won);
            totalValue += won.price;
          }

          updateBalance();
          renderInventory();
          renderMarket();

          AudioEngine.playWin();

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
        }, 1500);
      }
    }"""

html = html.replace(old_spin_case_js, new_spin_case_js)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added 1 to 10 flexible case opening selector!")
