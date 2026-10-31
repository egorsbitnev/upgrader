with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update grantFreeCoins so it also updates modal button if open
old_grant = """    function grantFreeCoins() {
      AudioEngine.playCoins();
      state.balance += 1000;
      updateBalance();
      recalcChance();
    }"""

new_grant = """    function grantFreeCoins() {
      AudioEngine.playCoins();
      state.balance += 2000;
      updateBalance();
      recalcChance();
      updateCaseOpenBtn();
    }"""

html = html.replace(old_grant, new_grant)

# 2. Add quick deposit inside case modal header so user never gets stuck with 0 coins
old_modal_header = """      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-weight: 800; font-size: 15px;" id="caseModalTitle">Кейс</span>
        <span style="cursor: pointer; color: var(--text-muted); font-size: 18px;" onclick="closeCaseModal()">✕</span>
      </div>"""

new_modal_header = """      <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <span style="font-weight: 800; font-size: 15px;" id="caseModalTitle">Кейс</span>
          <button onclick="grantFreeCoins()" style="background:var(--accent-green); border:none; border-radius:4px; font-weight:900; font-size:11px; padding:2px 8px; cursor:pointer; color:#000;">+2,000 🪙</button>
        </div>
        <span style="cursor: pointer; color: var(--text-muted); font-size: 18px; padding: 2px 6px;" onclick="closeCaseModal()">✕</span>
      </div>"""

html = html.replace(old_modal_header, new_modal_header)

# 3. Add vibrant active CSS styling to .btn-open-selected
old_btn_css = """.btn-open-selected {
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
    }"""

new_btn_css = """.btn-open-selected {
      width: 100%;
      padding: 12px 0;
      background: #00c74d;
      border: none;
      border-radius: 8px;
      color: #080d16;
      font-size: 14px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 199, 77, 0.35);
      transition: background 0.15s, transform 0.1s;
    }
    .btn-open-selected:active:not(:disabled) {
      transform: scale(0.98);
    }
    .btn-open-selected:disabled {
      background: #1e293b !important;
      color: #64748b !important;
      box-shadow: none !important;
      cursor: not-allowed;
    }"""

html = html.replace(old_btn_css, new_btn_css)

# 4. Make sure openCaseModal re-enables button and updates balance
old_open_case = """    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      selectedCaseQty = 1;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      document.getElementById('caseModal').style.display = 'flex';
      setCaseQty(1, document.querySelector('.qty-pill'));
      updateCaseOpenBtn();
    }"""

new_open_case = """    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      selectedCaseQty = 1;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      document.getElementById('caseModal').style.display = 'flex';
      
      const firstPill = document.querySelector('.qty-pill');
      setCaseQty(1, firstPill);
      updateCaseOpenBtn();
    }"""

html = html.replace(old_open_case, new_open_case)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed case open button, added in-modal coin deposit and active styling!")
