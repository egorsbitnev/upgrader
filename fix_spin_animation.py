with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix 1: When openCaseModal is called:
# Make sure display = 'flex' happens FIRST, then buildReels and updateCaseOpenBtn
old_open_modal = """    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      selectedCaseQty = 1;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      setCaseQty(1, document.querySelector('.qty-pill'));
      populateTape(caseData);
      document.getElementById('caseModal').style.display = 'flex';
    }"""

new_open_modal = """    function openCaseModal(caseData) {
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      selectedCaseQty = 1;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      document.getElementById('caseModal').style.display = 'flex';
      setCaseQty(1, document.querySelector('.qty-pill'));
      updateCaseOpenBtn();
    }"""

html = html.replace(old_open_modal, new_open_modal)

# Fix 2: In spinCase, ensure animation triggers reliably across browser engines by forcing reflow:
old_spin_loop = """      // Start spinning all reels at once with slight natural variances
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
      }"""

new_spin_loop = """      // Collect winning items and start spinning
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
        const duration = (4.4 + Math.random() * 0.4).toFixed(2);

        // Reset track position first without transition
        track.style.transition = 'none';
        track.style.transform = 'translateX(0px)';
        void track.offsetWidth; // Force DOM browser reflow

        // Start smooth CSS transform spin
        requestAnimationFrame(() => {
          track.style.transition = `transform ${duration}s cubic-bezier(0.12, 0.85, 0.22, 1)`;
          track.style.transform = `translateX(-${targetOffset}px)`;
        });
      }"""

html = html.replace(old_spin_loop, new_spin_loop)

# Fix 3: In updateCaseOpenBtn, don't leave button disabled if user has enough coins!
# Also make sure the button has an obvious active state
old_update_btn = """      const btn = document.getElementById('caseOpenSelectedBtn');
      if (btn && state.activeCase) {
        const total = state.activeCase.price * selectedCaseQty;
        btn.textContent = `ОТКРЫТЬ (${selectedCaseQty}x) ЗА 🪙 ${total.toLocaleString('ru-RU')}`;
        btn.disabled = (state.balance < total);
      }"""

new_update_btn = """      const btn = document.getElementById('caseOpenSelectedBtn');
      if (btn && state.activeCase) {
        const total = state.activeCase.price * selectedCaseQty;
        const canAfford = (state.balance >= total);
        btn.textContent = `ОТКРЫТЬ (${selectedCaseQty}x) ЗА 🪙 ${total.toLocaleString('ru-RU')}`;
        btn.disabled = !canAfford;
        if (!canAfford) {
          btn.textContent += ' (НЕДОСТАТОЧНО МОНЕТ)';
        }
      }"""

html = html.replace(old_update_btn, new_update_btn)

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Fixed case spinning animation reflow and modal initialization!")
