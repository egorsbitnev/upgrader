import re

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Web Audio API Sound Synthesizer mimicking CS2 / Upgrader casino sounds
sound_system_js = """
    // ================= REALISTIC AUDIO SYNTHESIZER (WEB AUDIO API) =================
    // No external MP3 files needed - 100% offline, zero lag, works in Android APK & Browser
    const AudioEngine = {
      ctx: null,
      muted: false,

      init() {
        if (!this.ctx) {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) {
            this.ctx = new AudioContext();
          }
        }
        if (this.ctx && this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      },

      toggleMute() {
        this.muted = !this.muted;
        const btn = document.getElementById('soundToggleBtn');
        if (btn) btn.textContent = this.muted ? '🔇' : '🔊';
        return this.muted;
      },

      // Mechanical tick during roulette spinning (like roulette needle passing teeth)
      playTick(pitchMod = 1.0) {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          const now = this.ctx.currentTime;

          osc.type = 'triangle';
          osc.frequency.setValueAtTime(600 * pitchMod, now);
          osc.frequency.exponentialRampToValueAtTime(150, now + 0.04);

          gain.gain.setValueAtTime(0.18, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.04);
        } catch(e) {}
      },

      // Button / Item click
      playClick() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          const now = this.ctx.currentTime;

          osc.type = 'sine';
          osc.frequency.setValueAtTime(800, now);
          osc.frequency.exponentialRampToValueAtTime(400, now + 0.03);

          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.03);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.03);
        } catch(e) {}
      },

      // Upgrade Start Whoosh / Tension buildup
      playRollStart() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(120, now);
          osc.frequency.exponentialRampToValueAtTime(450, now + 0.5);

          gain.gain.setValueAtTime(0.01, now);
          gain.gain.linearRampToValueAtTime(0.15, now + 0.3);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.5);
        } catch(e) {}
      },

      // Victory Fanfare (Casino Jackpot / Level Up Chime)
      playWin() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6 arpeggio

          notes.forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const noteStart = now + idx * 0.1;

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, noteStart);

            gain.gain.setValueAtTime(0.22, noteStart);
            gain.gain.exponentialRampToValueAtTime(0.001, noteStart + 0.4);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(noteStart);
            osc.stop(noteStart + 0.4);
          });
        } catch(e) {}
      },

      // Failure / Loss Buzz Thud
      playLose() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(180, now);
          osc.frequency.linearRampToValueAtTime(60, now + 0.35);

          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.35);
        } catch(e) {}
      },

      // Coin Add Chime
      playCoins() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(987.77, now); // B5
          osc.frequency.setValueAtTime(1318.51, now + 0.08); // E6

          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.3);
        } catch(e) {}
      }
    };

    // User interaction unlocker for browsers/mobile
    document.addEventListener('pointerdown', () => AudioEngine.init(), { once: true });
"""

# 1. Add Sound button to Header in user-profile
old_header_profile = """    <div class="user-profile">
      <div class="balance-pill">
        <span style="font-size: 13px;">🪙</span>
        <span class="balance-val" id="userBalanceDisplay">1,000</span>
      </div>
      <button class="btn-deposit" title="Пополнить бесплатно (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>"""

new_header_profile = """    <div class="user-profile">
      <button id="soundToggleBtn" onclick="AudioEngine.toggleMute()" style="background:#141c2c; border:1px solid var(--border); color:#fff; border-radius:50%; width:26px; height:26px; cursor:pointer; font-size:12px; display:flex; align-items:center; justify-content:center;">🔊</button>
      <div class="balance-pill">
        <span style="font-size: 13px;">🪙</span>
        <span class="balance-val" id="userBalanceDisplay">1,000</span>
      </div>
      <button class="btn-deposit" title="Пополнить бесплатно (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>"""

html = html.replace(old_header_profile, new_header_profile)

# 2. Inject AudioEngine into script
html = html.replace("const CATALOG =", sound_system_js + "\n    const CATALOG =")

# 3. Add sounds to grantFreeCoins
html = html.replace("function grantFreeCoins() {", "function grantFreeCoins() {\n      AudioEngine.playCoins();")

# 4. Add sounds to selectTarget and selectSourceItem and applyMultiplierTarget
html = html.replace("function selectTarget(skin) {", "function selectTarget(skin) {\n      AudioEngine.playClick();")
html = html.replace("function selectSourceItem(item) {", "function selectSourceItem(item) {\n      AudioEngine.playClick();")

# 5. Add sound ticks during startUpgrade needle spin
old_start_upgrade_end = """      const needle = document.getElementById('needle');
      needle.style.transform = `rotate(${currentRotation}deg)`;

      setTimeout(() => {
        state.isRolling = false;
        showUpgradeResult(isWin);
      }, 4100);"""

new_start_upgrade_end = """      const needle = document.getElementById('needle');
      needle.style.transform = `rotate(${currentRotation}deg)`;
      AudioEngine.playRollStart();

      // Play decelerating roulette ticks mimicking authentic Upgrader dial wheel
      let elapsed = 0;
      let tickDelay = 60;
      function scheduleTick() {
        if (elapsed < 3800) {
          AudioEngine.playTick(1.0 + (3800 - elapsed) / 3800);
          elapsed += tickDelay;
          tickDelay = Math.min(320, tickDelay * 1.07); // gradually slow down
          setTimeout(scheduleTick, tickDelay);
        }
      }
      setTimeout(scheduleTick, 100);

      setTimeout(() => {
        state.isRolling = false;
        showUpgradeResult(isWin);
      }, 4100);"""

html = html.replace(old_start_upgrade_end, new_start_upgrade_end)

# 6. Add sound in showUpgradeResult for win / lose
html = html.replace("document.getElementById('winOverlay').style.display = 'flex';", "document.getElementById('winOverlay').style.display = 'flex';\n        AudioEngine.playWin();")
html = html.replace("document.getElementById('loseOverlay').style.display = 'flex';", "document.getElementById('loseOverlay').style.display = 'flex';\n        AudioEngine.playLose();")

# 7. Add case spinning sounds
old_case_single_spin = """        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 4.8s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = `translateX(-${targetOffset}px)`;

        setTimeout(() => {"""

new_case_single_spin = """        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 4.8s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = `translateX(-${targetOffset}px)`;
        AudioEngine.playRollStart();

        let caseElapsed = 0;
        let caseDelay = 70;
        function scheduleCaseTick() {
          if (caseElapsed < 4500) {
            AudioEngine.playTick(1.2);
            caseElapsed += caseDelay;
            caseDelay = Math.min(350, caseDelay * 1.08);
            setTimeout(scheduleCaseTick, caseDelay);
          }
        }
        setTimeout(scheduleCaseTick, 100);

        setTimeout(() => {"""

html = html.replace(old_case_single_spin, new_case_single_spin)

# 8. Add case win sound in single and multi case reveal
html = html.replace("triggerConfetti();", "triggerConfetti();\n          AudioEngine.playWin();")
html = html.replace("multiOverlay.style.display = 'flex';", "multiOverlay.style.display = 'flex';\n          AudioEngine.playWin();")

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Added full sound system to index.html successfully!")
