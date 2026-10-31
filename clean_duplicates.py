import re

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Locate where the first spinCase starts
first_spincase_idx = html.find("function spinCase()")

# The clean, single spinCase implementation
clean_spincase_and_end = """function spinCase() {
      if (state.isOpeningCase || !state.activeCase) return;
      const count = selectedCaseQty || 1;
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

      // Ensure reels are created
      if (!multiTapeData || multiTapeData.length !== count) {
        buildReels(count);
      }

      const itemWidth = 80;
      const firstRow = document.querySelector('.single-reel-row');
      const containerWidth = firstRow ? firstRow.offsetWidth : 360;

      const wonItems = [];
      let totalValue = 0;
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
    }

    function closeMultiCaseModal() {
      document.getElementById('multiCaseModal').style.display = 'none';
    }

    // Initial setup
    renderMarket();
    renderInventory();
    updateBalance();
    selectCoinBet(100);
    selectTarget(CATALOG[10]);
  </script>
</body>
</html>"""

end_script_idx = html.find("</script>")
new_html = html[:first_spincase_idx] + clean_spincase_and_end

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Cleaned up duplicated scripts completely!")
