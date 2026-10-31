import base64

with open(r"C:\Users\Егор\.gemini\antigravity\brain\c5fc99ae-ad63-493d-9781-837ab4d9120f\.user_uploaded\uploaded_media_1793484464568.m4a", "rb") as f:
    audio_bytes = f.read()

b64_audio = base64.b64encode(audio_bytes).decode('ascii')
print(f"Base64 length: {len(b64_audio)}")

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Exact sound slices from user audio recording (uploaded_media_1793484464568.m4a):
# - Tick sound: isolated single crisp click around 02.40s - 02.50s
# - Roll sound loop: the real upgrader ticking & spinning sound
# - Win sound: celebration cheering and victory fanfare at 10.0s - 12.5s (and 33.2s - 35.5s)
# - Lose sound: short fail drop

user_audio_player_code = f"""
    // ================= 100% AUTHENTIC RECORDED AUDIO ENGINE =================
    // Uses the exact audio recording provided by user sliced via Web Audio API
    const AUTHENTIC_AUDIO_B64 = "data:audio/mp4;base64,{b64_audio}";

    const AudioEngine = {{
      ctx: null,
      audioBuffer: null,
      muted: false,
      isLoading: false,

      init() {{
        if (!this.ctx) {{
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) {{
            this.ctx = new AudioContext();
            this.loadBuffer();
          }}
        }}
        if (this.ctx && this.ctx.state === 'suspended') {{
          this.ctx.resume();
        }}
      }},

      loadBuffer() {{
        if (this.audioBuffer || this.isLoading) return;
        this.isLoading = true;

        fetch(AUTHENTIC_AUDIO_B64)
          .then(res => res.arrayBuffer())
          .then(ab => this.ctx.decodeAudioData(ab))
          .then(decoded => {{
            this.audioBuffer = decoded;
            this.isLoading = false;
          }})
          .catch(err => {{
            this.isLoading = false;
          }});
      }},

      toggleMute() {{
        this.muted = !this.muted;
        const btn = document.getElementById('soundToggleBtn');
        if (btn) btn.textContent = this.muted ? '🔇' : '🔊';
        return this.muted;
      }},

      // Play exact slice from user recording:
      playSlice(startSec, durationSec, volume = 1.0, playbackRate = 1.0) {{
        if (this.muted) return;
        this.init();
        if (!this.ctx || !this.audioBuffer) return;

        try {{
          const source = this.ctx.createBufferSource();
          source.buffer = this.audioBuffer;
          source.playbackRate.value = playbackRate;

          const gain = this.ctx.createGain();
          gain.gain.setValueAtTime(volume, this.ctx.currentTime);
          // smooth fade-out at end to prevent clipping
          gain.gain.setValueAtTime(volume, this.ctx.currentTime + durationSec - 0.04);
          gain.gain.linearRampToValueAtTime(0.001, this.ctx.currentTime + durationSec);

          source.connect(gain);
          gain.connect(this.ctx.destination);

          source.start(0, startSec, durationSec);
        }} catch(e) {{}}
      }},

      // Real upgrader wheel tick from recording (isolated slice around 02.40s)
      playTick(pitchMod = 1.0) {{
        this.playSlice(2.41, 0.05, 0.9, pitchMod);
      }},

      // Real button click
      playClick() {{
        this.playSlice(2.41, 0.04, 0.45, 1.2);
      }},

      // Real continuous roll sequence
      playRollStart() {{
        // Play the real spinning sequence from 03.0s to 07.2s
        this.playSlice(3.0, 4.2, 0.85, 1.0);
      }},

      // Real Win Celebration sound from recording (around 10.0s to 13.0s)
      playWin() {{
        this.playSlice(10.0, 3.2, 1.0, 1.0);
      }},

      // Real Lose / Drop miss sound
      playLose() {{
        this.playSlice(22.8, 0.8, 0.9, 0.9);
      }},

      // Coin / Buy sound
      playCoins() {{
        this.playSlice(2.41, 0.08, 0.7, 1.4);
      }}
    }};
"""

# Replace existing AudioEngine block with user_audio_player_code
start_str = "const AudioEngine = {"
end_str = "// User interaction unlocker"
idx_start = html.find(start_str)
idx_end = html.find(end_str, idx_start)

new_html = html[:idx_start] + user_audio_player_code + "\n\n    " + html[idx_end:]

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Injected user's exact authentic audio recording into index.html!")
