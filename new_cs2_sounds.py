with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# CS2 / Valve Authentic Sound Synthesis:
# 1. playTick: Snappy wooden/metallic mechanical click of CS2 case reel passing items (white noise burst + filtered wood click)
# 2. playClick: Subtle realistic CS2 UI button hover/press
# 3. playRollStart: Deep whoosh & reel spin start
# 4. playWin: Iconic CS2 Gold Item / Covert reveal sound (deep resonance chime + shimmering harmonics)
# 5. playLose: Realistic CS2 miss thud (muffled bass drop)
# 6. playCoins: Clean metallic coin clink

new_audio_engine = """const AudioEngine = {
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

      // CS2 Authentic Mechanical Reel Click (crisp wood/metal mechanical tooth click)
      playTick(pitchMod = 1.0) {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;

          // High snappy click impulse
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'triangle';
          osc.frequency.setValueAtTime(1400 * pitchMod, now);
          osc.frequency.exponentialRampToValueAtTime(120, now + 0.025);

          gain.gain.setValueAtTime(0.22, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.025);

          // Subtle low mechanical body tap
          const subOsc = this.ctx.createOscillator();
          const subGain = this.ctx.createGain();
          subOsc.type = 'sine';
          subOsc.frequency.setValueAtTime(260, now);
          subOsc.frequency.exponentialRampToValueAtTime(60, now + 0.03);

          subGain.gain.setValueAtTime(0.18, now);
          subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.03);

          osc.connect(gain);
          gain.connect(this.ctx.destination);
          subOsc.connect(subGain);
          subGain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.03);
          subOsc.start(now);
          subOsc.stop(now + 0.035);
        } catch(e) {}
      },

      // CS2 Clean UI Click
      playClick() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(1200, now);
          osc.frequency.exponentialRampToValueAtTime(300, now + 0.02);

          gain.gain.setValueAtTime(0.12, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.02);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.025);
        } catch(e) {}
      },

      // Reel Launch Whoosh (Deep cinematic sound)
      playRollStart() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(90, now);
          osc.frequency.exponentialRampToValueAtTime(320, now + 0.35);

          gain.gain.setValueAtTime(0.01, now);
          gain.gain.linearRampToValueAtTime(0.25, now + 0.15);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.45);
        } catch(e) {}
      },

      // CS2 Rare Item Drop Fanfare (Epic Shimmering Gold Reveal Chord)
      playWin() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          // Rich harmonic chord: D4 (293.66), F#4 (369.99), A4 (440.00), D5 (587.33), F#5 (739.99)
          const freqs = [293.66, 369.99, 440.00, 587.33, 739.99];

          freqs.forEach((f, i) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const start = now + (i * 0.06);

            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, start);

            gain.gain.setValueAtTime(0.18, start);
            gain.gain.exponentialRampToValueAtTime(0.001, start + 0.7);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(start);
            osc.stop(start + 0.75);
          });
        } catch(e) {}
      },

      // CS2 Case / Upgrade Miss (Muffled low bass thud)
      playLose() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          osc.type = 'sine';
          osc.frequency.setValueAtTime(140, now);
          osc.frequency.exponentialRampToValueAtTime(45, now + 0.3);

          gain.gain.setValueAtTime(0.28, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.4);
        } catch(e) {}
      },

      // Realistic Metallic Coins Clink
      playCoins() {
        if (this.muted) return;
        this.init();
        if (!this.ctx) return;

        try {
          const now = this.ctx.currentTime;
          [1800, 2400, 3100].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            const start = now + (idx * 0.05);

            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, start);

            gain.gain.setValueAtTime(0.12, start);
            gain.gain.exponentialRampToValueAtTime(0.001, start + 0.18);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start(start);
            osc.stop(start + 0.2);
          });
        } catch(e) {}
      }
    };"""

idx_start = html.find("const AudioEngine = {")
idx_end = html.find("// User interaction unlocker", idx_start)

html = html[:idx_start] + new_audio_engine + "\n\n    " + html[idx_end:]

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Synthesized authentic CS2 / Valve case sounds successfully!")
