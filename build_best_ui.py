import json

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\catalog.json", "r", encoding="utf-8") as f:
    catalog_json = f.read()

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\cases.json", "r", encoding="utf-8") as f:
    cases_json = f.read()

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>UPGRADER CS2 - Симулятор Апгрейда</title>
  <style>
    :root {{
      --bg-dark: #0a0d14;
      --bg-surface: #0f1422;
      --bg-panel: #141c2e;
      --bg-card: #18233a;
      --bg-card-hover: #202d4a;
      --neon-cyan: #00f2fe;
      --neon-blue: #4facfe;
      --neon-green: #00e701;
      --neon-green-glow: rgba(0, 231, 1, 0.45);
      --neon-gold: #ffb703;
      --neon-red: #ff2a5f;
      --neon-red-glow: rgba(255, 42, 95, 0.45);
      --text-main: #ffffff;
      --text-dim: #7f8fa4;
      --border: #23314d;
      --border-light: #2d3e63;
    }}
    * {{
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
      -webkit-tap-highlight-color: transparent;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
    }}
    body {{
      background: radial-gradient(circle at 50% 10%, #151f33 0%, #090c14 100%);
      color: var(--text-main);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    /* HEADER UPGRADER.BEST STYLE */
    header {{
      background: rgba(13, 18, 30, 0.95);
      border-bottom: 1px solid var(--border);
      padding: 10px 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      flex-shrink: 0;
      backdrop-filter: blur(10px);
    }}
    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
    }}
    .brand-icon {{
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, var(--neon-cyan), var(--neon-blue));
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #080d1a;
      font-weight: 900;
      font-size: 15px;
      box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    }}
    .brand-name {{
      font-size: 18px;
      font-weight: 900;
      letter-spacing: 1.5px;
      background: linear-gradient(90deg, #ffffff, #a5c9ff);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .brand-suffix {{
      font-size: 10px;
      font-weight: 800;
      background: rgba(0, 242, 254, 0.15);
      color: var(--neon-cyan);
      padding: 2px 6px;
      border-radius: 4px;
      border: 1px solid rgba(0, 242, 254, 0.3);
      letter-spacing: 0.5px;
    }}

    .user-profile {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .balance-pill {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #151d30;
      border: 1px solid var(--border);
      padding: 5px 12px;
      border-radius: 20px;
      box-shadow: inset 0 2px 4px rgba(0,0,0,0.4);
    }}
    .balance-val {{
      font-weight: 900;
      font-size: 15px;
      color: var(--neon-gold);
      letter-spacing: 0.5px;
    }}
    .btn-deposit {{
      background: linear-gradient(135deg, #00e676, #00c853);
      border: none;
      color: #090e17;
      font-weight: 900;
      font-size: 15px;
      width: 26px;
      height: 26px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(0, 230, 118, 0.4);
      transition: transform 0.1s, box-shadow 0.2s;
    }}
    .btn-deposit:active {{ transform: scale(0.9); }}

    /* SUB NAV (UPGRADER / CASES) */
    .nav-bar {{
      display: flex;
      background: #0d121f;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }}
    .nav-btn {{
      flex: 1;
      padding: 11px 0;
      text-align: center;
      font-size: 13px;
      font-weight: 800;
      color: var(--text-dim);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      transition: all 0.2s;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
    }}
    .nav-btn.active {{
      color: #ffffff;
      border-bottom-color: var(--neon-cyan);
      background: rgba(0, 242, 254, 0.05);
      text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }}

    /* MAIN WRAPPER */
    .main-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* ========================================================
       UPGRADER ARENA (UPGRADER.BEST ORIGINAL LAYOUT)
       ======================================================== */
    #view-upgrader {{
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow: hidden;
    }}

    .arena-board {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 20px;
      padding: 10px 16px 8px;
      background: radial-gradient(ellipse at 50% 40%, #151e33 0%, #0d121d 100%);
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
      position: relative;
    }}

    /* SIDE SLOTS: Left (Bet) & Right (Target) */
    .arena-slot {{
      width: 140px;
      height: 120px;
      background: var(--bg-panel);
      border: 1.5px dashed var(--border);
      border-radius: 14px;
      padding: 8px 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      position: relative;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}
    .arena-slot:hover {{
      border-color: #3f5580;
      transform: translateY(-2px);
    }}
    .arena-slot.active {{
      border-style: solid;
      border-color: #3b5078;
      background: #172237;
    }}
    .arena-slot.target.active {{
      border-color: var(--neon-cyan);
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.25);
    }}
    .slot-tag {{
      position: absolute;
      top: 5px;
      font-size: 9px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-dim);
    }}
    .slot-img-box {{
      width: 75px;
      height: 52px;
      margin-top: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .slot-img-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
    }}
    .slot-text-name {{
      font-size: 11px;
      font-weight: 800;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 125px;
      margin-top: 3px;
    }}
    .slot-text-price {{
      font-size: 11px;
      font-weight: 900;
      color: var(--neon-gold);
    }}

    /* CENTER ROULETTE DIAL (UPGRADER.BEST SIGNATURE) */
    .dial-wrapper {{
      position: relative;
      width: 180px;
      height: 180px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .dial-svg {{
      width: 180px;
      height: 180px;
      transform: rotate(-90deg);
    }}
    .dial-track {{
      fill: transparent;
      stroke: #182236;
      stroke-width: 13;
    }}
    .dial-glow-arc {{
      fill: transparent;
      stroke: var(--neon-green);
      stroke-width: 13;
      stroke-linecap: round;
      stroke-dasharray: 471;
      stroke-dashoffset: 471;
      transition: stroke-dashoffset 0.35s ease;
      filter: drop-shadow(0 0 10px var(--neon-green-glow));
    }}

    /* ARROW NEEDLE */
    .dial-needle {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 4px;
      height: 86px;
      margin-left: -2px;
      margin-top: -86px;
      transform-origin: bottom center;
      transform: rotate(0deg);
      transition: transform 4s cubic-bezier(0.12, 0.8, 0.22, 1);
      z-index: 10;
      pointer-events: none;
    }}
    .dial-needle::before {{
      content: '';
      position: absolute;
      top: -4px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 8px solid transparent;
      border-right: 8px solid transparent;
      border-top: 16px solid #ffffff;
      filter: drop-shadow(0 0 8px #ffffff);
    }}
    .dial-needle-hub {{
      position: absolute;
      width: 20px;
      height: 20px;
      background: radial-gradient(circle, #ffffff 40%, #00f2fe 100%);
      border-radius: 50%;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 14px rgba(0, 242, 254, 0.8);
      z-index: 11;
    }}

    /* DIAL CENTER TEXT */
    .dial-center-data {{
      position: absolute;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      pointer-events: none;
    }}
    .dial-chance {{
      font-size: 28px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1;
      letter-spacing: -0.5px;
      text-shadow: 0 0 14px var(--neon-green-glow);
    }}
    .dial-chance-label {{
      font-size: 9px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-dim);
      margin-top: 2px;
    }}
    .dial-mult {{
      font-size: 13px;
      font-weight: 800;
      color: var(--neon-cyan);
      margin-top: 1px;
    }}

    /* UPGRADE CONTROLS BAR (MULTIPLIER PRESETS & UPGRADE BUTTON) */
    .arena-controls {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      padding: 6px 14px 10px;
      background: #0d121d;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }}
    .presets-row {{
      display: flex;
      gap: 6px;
      width: 100%;
      max-width: 440px;
      justify-content: center;
    }}
    .preset-chip {{
      flex: 1;
      background: #141c2c;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 5px 0;
      font-size: 11px;
      font-weight: 800;
      color: var(--text-dim);
      text-align: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .preset-chip:hover {{
      border-color: #3b5078;
      color: #fff;
    }}
    .preset-chip:active {{
      transform: scale(0.96);
    }}

    .btn-upgrade-main {{
      width: 100%;
      max-width: 440px;
      padding: 12px 0;
      background: linear-gradient(135deg, #00e701, #00a801);
      color: #080d15;
      font-size: 15px;
      font-weight: 900;
      letter-spacing: 1px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0, 231, 1, 0.4);
      transition: all 0.2s;
    }}
    .btn-upgrade-main:hover:not(:disabled) {{
      box-shadow: 0 4px 25px rgba(0, 231, 1, 0.6);
      transform: translateY(-1px);
    }}
    .btn-upgrade-main:active:not(:disabled) {{
      transform: scale(0.98);
    }}
    .btn-upgrade-main:disabled {{
      background: #1c2639;
      color: #4f617d;
      box-shadow: none;
      cursor: not-allowed;
    }}

    /* BOTTOM TABS & MARKET/INVENTORY GRIDS */
    .bottom-section {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg-surface);
      overflow: hidden;
    }}
    .section-tabs-bar {{
      display: flex;
      border-bottom: 1px solid var(--border);
      background: #0d121e;
      flex-shrink: 0;
    }}
    .sec-tab {{
      flex: 1;
      padding: 10px;
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--text-dim);
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .sec-tab.active {{
      color: var(--neon-cyan);
      border-bottom-color: var(--neon-cyan);
      background: rgba(0, 242, 254, 0.05);
    }}

    .filter-scroll-bar {{
      display: flex;
      gap: 6px;
      padding: 6px 12px;
      background: #101625;
      border-bottom: 1px solid var(--border);
      overflow-x: auto;
      scrollbar-width: none;
      flex-shrink: 0;
    }}
    .filter-scroll-bar::-webkit-scrollbar {{ display: none; }}
    .filter-tag {{
      padding: 3px 10px;
      font-size: 11px;
      font-weight: 700;
      background: #172134;
      color: var(--text-dim);
      border-radius: 12px;
      border: 1px solid var(--border);
      white-space: nowrap;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .filter-tag.active {{
      background: var(--neon-cyan);
      color: #090e18;
      border-color: var(--neon-cyan);
    }}

    .skins-collection {{
      flex: 1;
      overflow-y: auto;
      padding: 8px 10px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(105px, 1fr));
      gap: 8px;
      align-content: start;
    }}
    .skin-tile {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 8px 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: all 0.15s;
    }}
    .skin-tile:hover {{
      border-color: #3f5580;
      transform: translateY(-2px);
    }}
    .skin-tile:active {{
      transform: scale(0.96);
    }}
    .skin-tile.selected {{
      border-color: var(--neon-cyan);
      box-shadow: 0 0 12px rgba(0, 242, 254, 0.3);
      background: #1e2c47;
    }}
    .skin-tile.rare-contraband {{ border-bottom: 3px solid #e4ae39; }}
    .skin-tile.rare-gold {{ border-bottom: 3px solid #ffd700; }}
    .skin-tile.rare-covert {{ border-bottom: 3px solid #eb4b4b; }}
    .skin-tile.rare-classified {{ border-bottom: 3px solid #d32ce6; }}
    .skin-tile.rare-restricted {{ border-bottom: 3px solid #8847ff; }}
    .skin-tile.rare-milspec {{ border-bottom: 3px solid #4b69ff; }}

    .skin-tile-img {{
      width: 100%;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4px;
    }}
    .skin-tile-img img {{
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 3px 6px rgba(0,0,0,0.5));
    }}
    .skin-tile-name {{
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      line-height: 1.2;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-tile-type {{
      font-size: 10px;
      color: var(--text-dim);
      margin: 1px 0 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-tile-price {{
      font-size: 11px;
      font-weight: 900;
      color: var(--neon-gold);
    }}

    /* ========================================================
       CASES VIEW
       ======================================================== */
    #view-cases {{
      display: none;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      background: var(--bg-dark);
      padding: 14px;
    }}
    .cases-banner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .cases-banner h2 {{
      font-size: 18px;
      font-weight: 900;
      color: #fff;
    }}
    .cases-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
      gap: 12px;
    }}
    .case-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 14px 10px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .case-card:hover {{
      transform: translateY(-3px);
      border-color: #3b5078;
    }}
    .case-card:active {{ transform: scale(0.96); }}
    .case-card-img {{
      width: 110px;
      height: 85px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 8px;
    }}
    .case-card-img img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.6));
    }}
    .case-card-name {{
      font-weight: 800;
      font-size: 13px;
      color: #fff;
      margin-bottom: 6px;
    }}
    .case-open-btn {{
      background: linear-gradient(135deg, #ffb703, #fb8500);
      color: #0b0f19;
      font-weight: 900;
      font-size: 12px;
      padding: 6px 14px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      width: 100%;
      margin-top: auto;
    }}

    /* CASE OPENING MODAL & ROULETTE REEL */
    .case-modal {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(8, 11, 18, 0.95);
      backdrop-filter: blur(10px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 16px;
    }}
    .case-modal-box {{
      width: 100%;
      max-width: 480px;
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 18px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      box-shadow: 0 10px 40px rgba(0,0,0,0.8);
    }}
    .case-modal-title {{
      font-size: 18px;
      font-weight: 900;
      color: #fff;
      margin-bottom: 14px;
    }}
    .tape-container {{
      width: 100%;
      height: 120px;
      background: #090c14;
      border: 2px solid var(--border);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
      margin-bottom: 16px;
    }}
    .tape-pointer {{
      position: absolute;
      top: 0; bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 3px;
      background: #ffb703;
      box-shadow: 0 0 10px #ffb703;
      z-index: 10;
    }}
    .tape-pointer::before {{
      content: '';
      position: absolute;
      top: 0; left: 50%;
      transform: translateX(-50%);
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 8px solid #ffb703;
    }}
    .tape-pointer::after {{
      content: '';
      position: absolute;
      bottom: 0; left: 50%;
      transform: translateX(-50%);
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-bottom: 8px solid #ffb703;
    }}
    .tape-track {{
      display: flex;
      height: 100%;
      position: absolute;
      left: 0; top: 0;
      will-change: transform;
    }}
    .tape-item {{
      width: 110px;
      height: 100%;
      background: #141c2c;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 6px;
      flex-shrink: 0;
      box-sizing: border-box;
      position: relative;
    }}
    .tape-item.rare-gold {{ border-bottom: 3px solid #ffd700; }}
    .tape-item.rare-covert {{ border-bottom: 3px solid #eb4b4b; }}
    .tape-item.rare-classified {{ border-bottom: 3px solid #d32ce6; }}
    .tape-item.rare-restricted {{ border-bottom: 3px solid #8847ff; }}
    .tape-item.rare-milspec {{ border-bottom: 3px solid #4b69ff; }}
    .tape-item-img {{
      width: 65px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .tape-item-img img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .tape-item-name {{
      font-size: 10px;
      font-weight: 700;
      color: #fff;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      margin-top: 4px;
    }}

    .case-actions-group {{
      display: flex;
      gap: 10px;
      width: 100%;
      max-width: 380px;
    }}
    .case-open-action-btn {{
      flex: 1;
      background: linear-gradient(135deg, #00e701, #00b301);
      color: #0b0f19;
      font-weight: 900;
      font-size: 13px;
      padding: 12px 14px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(0, 231, 1, 0.35);
    }}
    .case-open-10x-btn {{
      flex: 1;
      background: linear-gradient(135deg, #ffb703, #fb8500);
      color: #0b0f19;
      font-weight: 900;
      font-size: 13px;
      padding: 12px 14px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(255, 183, 3, 0.35);
    }}
    .case-close-x {{
      position: absolute;
      top: 14px;
      right: 16px;
      color: var(--text-dim);
      font-size: 20px;
      cursor: pointer;
      background: none;
      border: none;
    }}

    /* ========================================================
       SPECTACULAR WIN / LOSE FULLSCREEN ANIMATIONS & MODALS
       ======================================================== */
    .animation-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(6, 9, 16, 0.92);
      backdrop-filter: blur(10px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1200;
      overflow: hidden;
    }}

    /* WIN MODAL WITH NEON CONFETTI & EXPLOSION */
    .win-container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      position: relative;
      animation: popWin 0.6s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards;
      max-width: 360px;
      width: 90%;
    }}
    @keyframes popWin {{
      0% {{ transform: scale(0.4); opacity: 0; }}
      70% {{ transform: scale(1.08); }}
      100% {{ transform: scale(1); opacity: 1; }}
    }}

    .win-light-rays {{
      position: absolute;
      width: 380px;
      height: 380px;
      background: conic-gradient(from 0deg, rgba(0, 231, 1, 0.25), transparent 45deg, rgba(0, 242, 254, 0.25) 90deg, transparent 135deg, rgba(0, 231, 1, 0.25) 180deg, transparent 225deg, rgba(0, 242, 254, 0.25) 270deg, transparent 315deg);
      border-radius: 50%;
      animation: rotateRays 12s linear infinite;
      z-index: 1;
      pointer-events: none;
    }}
    @keyframes rotateRays {{
      from {{ transform: rotate(0deg); }}
      to {{ transform: rotate(360deg); }}
    }}

    .win-card-box {{
      background: linear-gradient(180deg, #17243c 0%, #101828 100%);
      border: 2px solid var(--neon-green);
      box-shadow: 0 0 50px rgba(0, 231, 1, 0.4), inset 0 0 20px rgba(0, 231, 1, 0.2);
      border-radius: 20px;
      padding: 26px 20px;
      width: 100%;
      position: relative;
      z-index: 2;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .win-badge-title {{
      font-size: 24px;
      font-weight: 900;
      color: var(--neon-green);
      letter-spacing: 1px;
      text-shadow: 0 0 16px rgba(0, 231, 1, 0.7);
      margin-bottom: 4px;
    }}
    .win-subtitle {{
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-dim);
      margin-bottom: 12px;
    }}
    .win-skin-glow-wrap {{
      width: 170px;
      height: 110px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 8px 0;
      position: relative;
    }}
    .win-skin-glow-wrap img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 10px 20px rgba(0, 231, 1, 0.6));
      animation: floatSkin 3s ease-in-out infinite;
    }}
    @keyframes floatSkin {{
      0%, 100% {{ transform: translateY(0px) scale(1); }}
      50% {{ transform: translateY(-8px) scale(1.05); }}
    }}

    .win-item-name {{
      font-size: 18px;
      font-weight: 900;
      color: #ffffff;
      margin-top: 6px;
    }}
    .win-item-price {{
      font-size: 16px;
      font-weight: 900;
      color: var(--neon-gold);
      margin-top: 4px;
      text-shadow: 0 0 10px rgba(255, 183, 3, 0.5);
    }}
    .btn-collect-win {{
      margin-top: 20px;
      width: 100%;
      padding: 13px;
      background: linear-gradient(135deg, #00e701, #00b301);
      border: none;
      border-radius: 12px;
      color: #080d16;
      font-size: 15px;
      font-weight: 900;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0, 231, 1, 0.4);
      transition: all 0.15s;
    }}
    .btn-collect-win:active {{ transform: scale(0.97); }}

    /* LOSE MODAL WITH SHAKE & ASH/FIRE EFFECT */
    .lose-container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      max-width: 340px;
      width: 90%;
      animation: shakeLose 0.7s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
    }}
    @keyframes shakeLose {{
      10%, 90% {{ transform: translate3d(-3px, 0, 0); }}
      20%, 80% {{ transform: translate3d(5px, 0, 0); }}
      30%, 50%, 70% {{ transform: translate3d(-7px, 0, 0); }}
      40%, 60% {{ transform: translate3d(7px, 0, 0); }}
    }}
    .lose-card-box {{
      background: linear-gradient(180deg, #24141c 0%, #130a0f 100%);
      border: 2px solid var(--neon-red);
      box-shadow: 0 0 45px rgba(255, 42, 95, 0.4), inset 0 0 20px rgba(255, 42, 95, 0.2);
      border-radius: 20px;
      padding: 24px 20px;
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lose-icon {{
      font-size: 55px;
      margin: 8px 0;
      filter: drop-shadow(0 0 16px rgba(255, 42, 95, 0.6));
      animation: smokeFade 1.2s ease-in-out infinite alternate;
    }}
    @keyframes smokeFade {{
      from {{ transform: scale(0.9) rotate(-4deg); opacity: 0.7; }}
      to {{ transform: scale(1.1) rotate(4deg); opacity: 1; }}
    }}
    .lose-badge-title {{
      font-size: 22px;
      font-weight: 900;
      color: var(--neon-red);
      letter-spacing: 1px;
      text-shadow: 0 0 16px rgba(255, 42, 95, 0.7);
      margin-bottom: 4px;
    }}
    .lose-desc {{
      font-size: 13px;
      color: #b97f8c;
      margin: 4px 0 16px;
    }}
    .btn-retry-lose {{
      width: 100%;
      padding: 12px;
      background: #331d27;
      border: 1px solid #66273c;
      border-radius: 12px;
      color: #fff;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .btn-retry-lose:active {{ transform: scale(0.97); }}

    /* MULTI RESULT 10X */
    .multi-res-dialog {{
      background: var(--bg-panel);
      border: 2px solid var(--neon-gold);
      border-radius: 18px;
      padding: 18px;
      width: 92%;
      max-width: 520px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 0 40px rgba(255, 183, 3, 0.35);
      animation: popWin 0.3s ease;
    }}
    .multi-res-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      margin-bottom: 12px;
    }}
    .multi-res-title {{
      font-size: 18px;
      font-weight: 900;
      color: #fff;
    }}
    .multi-res-total {{
      font-size: 14px;
      font-weight: 800;
      color: var(--neon-gold);
    }}
    .multi-res-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(90px, 1fr));
      gap: 8px;
      width: 100%;
      overflow-y: auto;
      max-height: 52vh;
      padding: 4px;
    }}
    .multi-res-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 6px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }}
    .multi-res-card.rare-gold {{ border-bottom: 3px solid #ffd700; box-shadow: 0 0 10px rgba(255, 215, 0, 0.4); }}
    .multi-res-card.rare-covert {{ border-bottom: 3px solid #eb4b4b; }}
    .multi-res-card.rare-classified {{ border-bottom: 3px solid #d32ce6; }}
    .multi-res-card.rare-restricted {{ border-bottom: 3px solid #8847ff; }}
    .multi-res-card.rare-milspec {{ border-bottom: 3px solid #4b69ff; }}
    .multi-res-card img {{
      width: 54px;
      height: 40px;
      object-fit: contain;
      margin-bottom: 4px;
    }}
    .multi-res-card-name {{
      font-size: 10px;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .multi-res-card-price {{
      font-size: 10px;
      font-weight: 800;
      color: var(--neon-gold);
      margin-top: 2px;
    }}
    .btn-collect-all {{
      margin-top: 14px;
      width: 100%;
      padding: 12px;
      background: #25334d;
      border: none;
      border-radius: 10px;
      color: #fff;
      font-weight: 800;
      cursor: pointer;
    }}

    /* PARTICLES CANVAS */
    #confettiCanvas {{
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      pointer-events: none;
      z-index: 5;
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="brand-wrap">
      <div class="brand-icon">UP</div>
      <div class="brand-name">UPGRADER</div>
      <div class="brand-suffix">BEST</div>
    </div>
    <div class="user-profile">
      <div class="balance-pill">
        <span>🪙</span>
        <span class="balance-val" id="userBalanceDisplay">1,000</span>
      </div>
      <button class="btn-deposit" title="Пополнить бесплатно (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>
  </header>

  <!-- NAVIGATION -->
  <div class="nav-bar">
    <div class="nav-btn active" id="navTabUpgrader" onclick="switchMainView('upgrader')">
      <span>⚡</span> Апгрейдер
    </div>
    <div class="nav-btn" id="navTabCases" onclick="switchMainView('cases')">
      <span>📦</span> Кейсы CS2
    </div>
  </div>

  <div class="main-content">

    <!-- ================= VIEW 1: UPGRADER ================= -->
    <div id="view-upgrader">
      
      <!-- ARENA: Left Bet Slot - Dial Wheel - Right Target Slot -->
      <div class="arena-board">
        
        <!-- Left Slot: Source -->
        <div class="arena-slot active" id="sourceSlot" onclick="switchTab('inventory')">
          <span class="slot-tag">Ваша ставка</span>
          <div class="slot-img-box" id="sourceImgBox">
            <span style="font-size: 32px;">🪙</span>
          </div>
          <div class="slot-text-name" id="sourceTitle">100 Монет</div>
          <div class="slot-text-price" id="sourcePrice">🪙 100</div>
        </div>

        <!-- Center: Roulette Dial -->
        <div class="dial-wrapper">
          <svg class="dial-svg">
            <circle class="dial-track" cx="90" cy="90" r="75"></circle>
            <circle class="dial-glow-arc" id="winArc" cx="90" cy="90" r="75"></circle>
          </svg>

          <div class="dial-needle" id="needle"></div>
          <div class="dial-needle-hub"></div>

          <div class="dial-center-data">
            <span class="dial-chance" id="chanceDisplay">0%</span>
            <span class="dial-chance-label">Шанс успеха</span>
            <span class="dial-mult" id="multDisplay">x0.00</span>
          </div>
        </div>

        <!-- Right Slot: Target Skin -->
        <div class="arena-slot target" id="targetSlot" onclick="switchTab('market')">
          <span class="slot-tag">Цель</span>
          <div class="slot-img-box" id="targetImgBox">
            <span style="font-size: 26px;">🎯</span>
          </div>
          <div class="slot-text-name" id="targetTitle">Выберите скин</div>
          <div class="slot-text-price" id="targetPrice">-</div>
        </div>

      </div>

      <!-- Controls Row: Preset Multipliers & Action Button -->
      <div class="arena-controls">
        <div class="presets-row">
          <div class="preset-chip" onclick="applyMultiplierTarget(1.5)">1.5x</div>
          <div class="preset-chip" onclick="applyMultiplierTarget(2)">2x</div>
          <div class="preset-chip" onclick="applyMultiplierTarget(5)">5x</div>
          <div class="preset-chip" onclick="applyMultiplierTarget(10)">10x</div>
          <div class="preset-chip" onclick="applyMultiplierTarget(25)">25x</div>
          <div class="preset-chip" onclick="applyMultiplierTarget(50)">50x</div>
        </div>

        <button class="btn-upgrade-main" id="upgradeBtn" disabled onclick="startUpgrade()">
          СДЕЛАТЬ АПГРЕЙД
        </button>
      </div>

      <!-- Bottom Collection Section -->
      <div class="bottom-section">
        <div class="section-tabs-bar">
          <button class="sec-tab active" id="tabMarketBtn" onclick="switchTab('market')">Магазин скинов (<span id="marketCount">0</span>)</button>
          <button class="sec-tab" id="tabInventoryBtn" onclick="switchTab('inventory')">Инвентарь (<span id="invCount">0</span>)</button>
        </div>

        <div class="filter-scroll-bar" id="marketFilterBar">
          <div class="filter-tag active" onclick="filterMarket('all', this)">Все</div>
          <div class="filter-tag" onclick="filterMarket('knife', this)">Ножи и перчатки</div>
          <div class="filter-tag" onclick="filterMarket('rifle', this)">Винтовки</div>
          <div class="filter-tag" onclick="filterMarket('pistol', this)">Пистолеты</div>
          <div class="filter-tag" onclick="filterMarket('cheap', this)">До 1,000</div>
          <div class="filter-tag" onclick="filterMarket('expensive', this)">10,000+</div>
        </div>

        <div class="skins-collection" id="marketGrid"></div>
        <div class="skins-collection" id="inventoryGrid" style="display: none;"></div>
      </div>

    </div>

    <!-- ================= VIEW 2: CASES ================= -->
    <div id="view-cases">
      <div class="cases-banner">
        <h2>Оригинальные кейсы CS2</h2>
        <span style="font-size: 13px; color: var(--neon-gold); font-weight: 800;">📦 Открытие в 1 клик</span>
      </div>
      <div class="cases-grid" id="casesGrid"></div>
    </div>

  </div>

  <!-- CASE OPENING MODAL -->
  <div class="case-modal" id="caseModal">
    <div class="case-modal-box">
      <button class="case-close-x" onclick="closeCaseModal()">✕</button>
      <div class="case-modal-title" id="caseModalTitle">Кейс «Киловатт»</div>

      <div class="tape-container">
        <div class="tape-pointer"></div>
        <div class="tape-track" id="tapeTrack"></div>
      </div>

      <div class="case-actions-group">
        <button class="case-open-action-btn" id="caseOpen1xBtn" onclick="spinCase(1)">
          1x 🪙 250
        </button>
        <button class="case-open-10x-btn" id="caseOpen10xBtn" onclick="spinCase(10)">
          ⚡ 10x 🪙 2,500
        </button>
      </div>
    </div>
  </div>

  <!-- WIN ANIMATION MODAL -->
  <div class="animation-overlay" id="winOverlay">
    <canvas id="confettiCanvas"></canvas>
    <div class="win-light-rays"></div>
    <div class="win-container">
      <div class="win-card-box">
        <div class="win-badge-title">🎉 АПГРЕЙД УСПЕШЕН!</div>
        <div class="win-subtitle">Поздравляем с выигрышем</div>
        <div class="win-skin-glow-wrap">
          <img id="winSkinImg" src="" alt="Skin">
        </div>
        <div class="win-item-name" id="winSkinName">AK-47 | Вулкан</div>
        <div class="win-item-price" id="winSkinPrice">🪙 +2,800</div>
        <button class="btn-collect-win" onclick="closeWinOverlay()">ЗАБРАТЬ В ИНВЕНТАРЬ</button>
      </div>
    </div>
  </div>

  <!-- LOSE ANIMATION MODAL -->
  <div class="animation-overlay" id="loseOverlay">
    <div class="lose-container">
      <div class="lose-card-box">
        <div class="lose-icon">💥</div>
        <div class="lose-badge-title">АПГРЕЙД ПРОВАЛЕН</div>
        <div class="lose-desc">Стрелка остановилась вне зоны победы. Предмет сгорел.</div>
        <button class="btn-retry-lose" onclick="closeLoseOverlay()">ПОПРОБОВАТЬ СНОВА</button>
      </div>
    </div>
  </div>

  <!-- 10X CASE MULTI RESULT MODAL -->
  <div class="animation-overlay" id="multiResultOverlay">
    <div class="multi-res-dialog">
      <div class="multi-res-header">
        <div class="multi-res-title">🎁 ДРОП ИЗ 10 КЕЙСОВ</div>
        <div class="multi-res-total" id="multiResTotal">+🪙 0</div>
      </div>
      <div class="multi-res-grid" id="multiResGrid"></div>
      <button class="btn-collect-all" onclick="closeMultiResult()">ЗАБРАТЬ ВСЕ В ИНВЕНТАРЬ</button>
    </div>
  </div>

  <script>
    const CATALOG = {catalog_json};
    const CASES = {cases_json};

    let state = {{
      balance: 1000,
      inventory: [
        {{ uid: 1, ...CATALOG[0] }},
        {{ uid: 2, ...CATALOG[2] }}
      ],
      selectedSource: null,
      coinBet: 100,
      selectedTarget: null,
      isRolling: false,
      currentFilter: 'all',
      activeCase: null,
      isOpeningCase: false
    }};

    try {{
      const saved = localStorage.getItem('upgrader_best_state');
      if (saved) {{
        const parsed = JSON.parse(saved);
        state.balance = parsed.balance ?? 1000;
        if (Array.isArray(parsed.inventory) && parsed.inventory.length > 0) {{
          state.inventory = parsed.inventory;
        }}
      }}
    }} catch(e) {{}}

    function saveState() {{
      try {{
        localStorage.setItem('upgrader_best_state', JSON.stringify({{
          balance: state.balance,
          inventory: state.inventory
        }}));
      }} catch(e) {{}}
    }}

    const CIRCLE_CIRCUMFERENCE = 2 * Math.PI * 75; // ~471px

    function updateBalance() {{
      document.getElementById('userBalanceDisplay').textContent = Math.floor(state.balance).toLocaleString('ru-RU');
      document.getElementById('invCount').textContent = state.inventory.length;
      document.getElementById('marketCount').textContent = CATALOG.length;
      saveState();
    }}

    function grantFreeCoins() {{
      state.balance += 1000;
      updateBalance();
      recalcChance();
    }}

    function switchMainView(mode) {{
      document.getElementById('navTabUpgrader').classList.toggle('active', mode === 'upgrader');
      document.getElementById('navTabCases').classList.toggle('active', mode === 'cases');
      document.getElementById('view-upgrader').style.display = mode === 'upgrader' ? 'flex' : 'none';
      document.getElementById('view-cases').style.display = mode === 'cases' ? 'flex' : 'none';
      if (mode === 'cases') renderCases();
    }}

    function switchTab(tab) {{
      document.getElementById('tabMarketBtn').classList.toggle('active', tab === 'market');
      document.getElementById('tabInventoryBtn').classList.toggle('active', tab === 'inventory');
      document.getElementById('marketGrid').style.display = tab === 'market' ? 'grid' : 'none';
      document.getElementById('marketFilterBar').style.display = tab === 'market' ? 'flex' : 'none';
      document.getElementById('inventoryGrid').style.display = tab === 'inventory' ? 'grid' : 'none';
    }}

    function filterMarket(filter, el) {{
      state.currentFilter = filter;
      document.querySelectorAll('.filter-tag').forEach(c => c.classList.remove('active'));
      if (el) el.classList.add('active');
      renderMarket();
    }}

    function selectTarget(skin) {{
      if (state.isRolling) return;
      state.selectedTarget = skin;
      document.getElementById('targetSlot').classList.add('active');
      document.getElementById('targetImgBox').innerHTML = `<img src="${{skin.image}}" alt="${{skin.name}}">`;
      document.getElementById('targetTitle').textContent = `${{skin.type}} | ${{skin.name}}`;
      document.getElementById('targetPrice').textContent = `🪙 ${{skin.price.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#marketGrid .skin-tile').forEach(c => c.classList.remove('selected'));
      const activeCard = document.getElementById(`target-card-${{skin.id}}`);
      if (activeCard) activeCard.classList.add('selected');

      recalcChance();
    }}

    function selectSourceItem(item) {{
      if (state.isRolling) return;
      state.selectedSource = item;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgBox').innerHTML = `<img src="${{item.image}}" alt="${{item.name}}">`;
      document.getElementById('sourceTitle').textContent = `${{item.type}} | ${{item.name}}`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{item.price.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .skin-tile').forEach(c => c.classList.remove('selected'));
      const activeCard = document.getElementById(`inv-card-${{item.uid}}`);
      if (activeCard) activeCard.classList.add('selected');

      recalcChance();
    }}

    function selectCoinBet(amount) {{
      if (state.isRolling) return;
      state.selectedSource = null;
      state.coinBet = amount;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgBox').innerHTML = `<span style="font-size: 32px;">🪙</span>`;
      document.getElementById('sourceTitle').textContent = `${{amount.toLocaleString('ru-RU')}} Монет`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{amount.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .skin-tile').forEach(c => c.classList.remove('selected'));
      recalcChance();
    }}

    function applyMultiplierTarget(mult) {{
      const sourceVal = getSourceValue();
      const targetVal = sourceVal * mult;
      // find skin closest to targetVal
      let closest = CATALOG[0];
      let minDiff = Infinity;
      CATALOG.forEach(s => {{
        const diff = Math.abs(s.price - targetVal);
        if (diff < minDiff) {{
          minDiff = diff;
          closest = s;
        }}
      }});
      selectTarget(closest);
    }}

    function getSourceValue() {{
      return state.selectedSource ? state.selectedSource.price : state.coinBet;
    }}

    function recalcChance() {{
      const chanceText = document.getElementById('chanceDisplay');
      const multText = document.getElementById('multDisplay');
      const winArc = document.getElementById('winArc');
      const btn = document.getElementById('upgradeBtn');

      if (!state.selectedTarget) {{
        chanceText.textContent = "0%";
        multText.textContent = "x0.00";
        winArc.style.strokeDashoffset = CIRCLE_CIRCUMFERENCE;
        btn.disabled = true;
        return;
      }}

      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      if (sourceVal >= targetVal) {{
        chanceText.textContent = "100%";
        multText.textContent = "x1.00";
        winArc.style.strokeDashoffset = 0;
        btn.disabled = (!state.selectedSource && state.balance < state.coinBet);
        return;
      }}

      // Boosted formula x1.6 for generous win-rates
      let chance = (sourceVal / targetVal) * 160;
      if (chance > 96) chance = 96;
      if (chance < 3.0) chance = 3.0;

      const mult = (targetVal / sourceVal).toFixed(2);

      chanceText.textContent = chance.toFixed(1) + "%";
      multText.textContent = "x" + mult;

      const offset = CIRCLE_CIRCUMFERENCE - (CIRCLE_CIRCUMFERENCE * (chance / 100));
      winArc.style.strokeDashoffset = offset;

      if (!state.selectedSource && state.balance < state.coinBet) {{
        btn.disabled = true;
      }} else {{
        btn.disabled = false;
      }}
    }}

    function renderMarket() {{
      const grid = document.getElementById('marketGrid');
      grid.innerHTML = '';
      
      const filtered = CATALOG.filter(skin => {{
        if (state.currentFilter === 'knife') return skin.type.includes('Нож') || skin.type.includes('Керамбит') || skin.type.includes('перчатки');
        if (state.currentFilter === 'rifle') return skin.type.includes('AK-47') || skin.type.includes('M4A') || skin.type.includes('AWP');
        if (state.currentFilter === 'pistol') return skin.type.includes('P250') || skin.type.includes('Glock') || skin.type.includes('USP') || skin.type.includes('Eagle');
        if (state.currentFilter === 'cheap') return skin.price <= 1000;
        if (state.currentFilter === 'expensive') return skin.price >= 10000;
        return true;
      }});

      filtered.forEach(skin => {{
        const isSelected = state.selectedTarget && state.selectedTarget.id === skin.id;
        const card = document.createElement('div');
        card.id = `target-card-${{skin.id}}`;
        card.className = `skin-tile rare-${{skin.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="skin-tile-img">
            <img src="${{skin.image}}" alt="${{skin.name}}" loading="lazy">
          </div>
          <div class="skin-tile-name">${{skin.name}}</div>
          <div class="skin-tile-type">${{skin.type}}</div>
          <div class="skin-tile-price">🪙 ${{skin.price.toLocaleString('ru-RU')}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderInventory() {{
      const grid = document.getElementById('inventoryGrid');
      grid.innerHTML = '';

      const coinCard = document.createElement('div');
      coinCard.className = `skin-tile`;
      coinCard.style.borderColor = 'var(--neon-gold)';
      coinCard.onclick = () => {{
        const val = prompt("Введите сумму ставки монет:", state.coinBet || "100");
        const num = parseInt(val, 10);
        if (num && num > 0) selectCoinBet(num);
      }};
      coinCard.innerHTML = `
        <div class="skin-tile-img">
          <span style="font-size: 34px;">🪙</span>
        </div>
        <div class="skin-tile-name">Ставка монетами</div>
        <div class="skin-tile-type">Баланс: ${{state.balance.toLocaleString('ru-RU')}}</div>
        <div class="skin-tile-price">🪙 Изменить</div>
      `;
      grid.appendChild(coinCard);

      state.inventory.forEach(item => {{
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${{item.uid}}`;
        card.className = `skin-tile rare-${{item.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="skin-tile-img">
            <img src="${{item.image}}" alt="${{item.name}}" loading="lazy">
          </div>
          <div class="skin-tile-name">${{item.name}}</div>
          <div class="skin-tile-type">${{item.type}}</div>
          <div class="skin-tile-price">🪙 ${{item.price.toLocaleString('ru-RU')}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    let currentRotation = 0;

    function startUpgrade() {{
      if (state.isRolling || !state.selectedTarget) return;

      const sourceVal = getSourceValue();
      const targetVal = state.selectedTarget.price;

      if (!state.selectedSource) {{
        if (state.balance < state.coinBet) {{
          alert("Недостаточно виртуальных монет! Нажмите '+' возле баланса.");
          return;
        }}
        state.balance -= state.coinBet;
      }} else {{
        const idx = state.inventory.findIndex(i => i.uid === state.selectedSource.uid);
        if (idx !== -1) state.inventory.splice(idx, 1);
      }}

      state.isRolling = true;
      document.getElementById('upgradeBtn').disabled = true;
      updateBalance();
      renderInventory();

      let chance = (sourceVal / targetVal) * 160;
      if (sourceVal >= targetVal) chance = 100;
      if (chance > 96) chance = 96;
      if (chance < 3.0) chance = 3.0;

      const isWin = (Math.random() * 100) <= chance;
      const winSectorDeg = (chance / 100) * 360;
      let targetDeg;

      if (isWin) {{
        targetDeg = Math.random() * (winSectorDeg - 4) + 2;
      }} else {{
        targetDeg = winSectorDeg + (Math.random() * (360 - winSectorDeg - 4) + 2);
      }}

      const fullSpins = (5 + Math.floor(Math.random() * 3)) * 360;
      currentRotation += fullSpins + (targetDeg - (currentRotation % 360));
      if (currentRotation < fullSpins) currentRotation += fullSpins;

      const needle = document.getElementById('needle');
      needle.style.transform = `rotate(${{currentRotation}}deg)`;

      setTimeout(() => {{
        state.isRolling = false;
        showUpgradeResult(isWin);
      }}, 4100);
    }}

    function showUpgradeResult(isWin) {{
      if (isWin) {{
        const wonItem = {{ uid: Date.now(), ...state.selectedTarget }};
        state.inventory.unshift(wonItem);
        updateBalance();
        renderInventory();

        document.getElementById('winSkinImg').src = wonItem.image;
        document.getElementById('winSkinName').textContent = `${{wonItem.type}} | ${{wonItem.name}}`;
        document.getElementById('winSkinPrice').textContent = `🪙 +${{wonItem.price.toLocaleString('ru-RU')}}`;

        document.getElementById('winOverlay').style.display = 'flex';
        triggerConfetti();
      }} else {{
        updateBalance();
        renderInventory();
        document.getElementById('loseOverlay').style.display = 'flex';
      }}
    }}

    function closeWinOverlay() {{
      document.getElementById('winOverlay').style.display = 'none';
      stopConfetti();
      state.selectedSource = null;
      selectCoinBet(100);
    }}

    function closeLoseOverlay() {{
      document.getElementById('loseOverlay').style.display = 'none';
      state.selectedSource = null;
      selectCoinBet(100);
    }}

    /* ================= CONFETTI PARTICLES ================= */
    let confettiAnimation = null;
    function triggerConfetti() {{
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#00e701', '#00f2fe', '#ffb703', '#ffffff', '#4facfe'];

      for (let i = 0; i < 90; i++) {{
        particles.push({{
          x: canvas.width / 2,
          y: canvas.height / 2,
          vx: (Math.random() - 0.5) * 16,
          vy: (Math.random() - 0.8) * 18,
          size: Math.random() * 7 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 10
        }});
      }}

      function render() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.4; // gravity
          p.rotation += p.rotSpeed;

          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
          ctx.restore();
        }});
        confettiAnimation = requestAnimationFrame(render);
      }}
      render();
    }}

    function stopConfetti() {{
      if (confettiAnimation) cancelAnimationFrame(confettiAnimation);
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    }}

    /* ================= CASES LOGIC ================= */
    function renderCases() {{
      const grid = document.getElementById('casesGrid');
      grid.innerHTML = '';
      CASES.forEach(c => {{
        const card = document.createElement('div');
        card.className = 'case-card';
        card.onclick = () => openCaseModal(c);
        card.innerHTML = `
          <div class="case-card-img">
            <img src="${{c.image}}" alt="${{c.name}}" loading="lazy">
          </div>
          <div class="case-card-name">${{c.name}}</div>
          <button class="case-open-btn">🪙 ${{c.price.toLocaleString('ru-RU')}}</button>
        `;
        grid.appendChild(card);
      }});
    }}

    let generatedItemsTape = [];

    function openCaseModal(caseData) {{
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      
      const price1x = caseData.price;
      const price10x = caseData.price * 10;
      
      const btn1x = document.getElementById('caseOpen1xBtn');
      const btn10x = document.getElementById('caseOpen10xBtn');
      
      btn1x.textContent = `1x 🪙 ${{price1x.toLocaleString('ru-RU')}}`;
      btn10x.textContent = `⚡ 10x 🪙 ${{price10x.toLocaleString('ru-RU')}}`;
      
      btn1x.disabled = (state.balance < price1x);
      btn10x.disabled = (state.balance < price10x);

      populateTape(caseData);
      document.getElementById('caseModal').style.display = 'flex';
    }}

    function closeCaseModal() {{
      if (state.isOpeningCase) return;
      document.getElementById('caseModal').style.display = 'none';
    }}

    function rollRandomItem(pool) {{
      const rand = Math.random() * 100;
      let chosenRarity = 'milspec';
      if (rand < 7.0) chosenRarity = 'gold';
      else if (rand < 25.0) chosenRarity = 'covert';
      else if (rand < 60.0) chosenRarity = 'classified';
      else if (rand < 85.0) chosenRarity = 'restricted';

      const filtered = pool.filter(it => it.rarity === chosenRarity);
      return filtered.length > 0 ? filtered[Math.floor(Math.random() * filtered.length)] : pool[Math.floor(Math.random() * pool.length)];
    }}

    function populateTape(caseData) {{
      const track = document.getElementById('tapeTrack');
      track.style.transition = 'none';
      track.style.transform = 'translateX(0px)';
      track.innerHTML = '';

      generatedItemsTape = [];
      const pool = caseData.items;

      for (let i = 0; i < 50; i++) {{
        const item = rollRandomItem(pool);
        generatedItemsTape.push(item);

        const el = document.createElement('div');
        el.className = `tape-item rare-${{item.rarity}}`;
        el.innerHTML = `
          <div class="tape-item-img">
            <img src="${{item.image}}" alt="${{item.name}}">
          </div>
          <div class="tape-item-name">${{item.name}}</div>
        `;
        track.appendChild(el);
      }}
    }}

    function spinCase(count = 1) {{
      if (state.isOpeningCase || !state.activeCase) return;
      const totalCost = state.activeCase.price * count;

      if (state.balance < totalCost) {{
        alert("Недостаточно монет! Нажмите '+' возле баланса для пополнения.");
        return;
      }}

      state.balance -= totalCost;
      updateBalance();

      state.isOpeningCase = true;
      document.getElementById('caseOpen1xBtn').disabled = true;
      document.getElementById('caseOpen10xBtn').disabled = true;

      if (count === 10) {{
        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 1.4s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = 'translateX(-2200px)';

        setTimeout(() => {{
          state.isOpeningCase = false;
          document.getElementById('caseModal').style.display = 'none';

          const wonItems = [];
          let totalValue = 0;
          for (let i = 0; i < 10; i++) {{
            const it = rollRandomItem(state.activeCase.items);
            const won = {{ uid: Date.now() + i, ...it }};
            wonItems.push(won);
            state.inventory.unshift(won);
            totalValue += won.price;
          }}

          updateBalance();
          renderInventory();

          const multiOverlay = document.getElementById('multiResultOverlay');
          const grid = document.getElementById('multiResGrid');
          const totalEl = document.getElementById('multiResTotal');

          grid.innerHTML = '';
          totalEl.textContent = `Общая ценность: 🪙 ${{totalValue.toLocaleString('ru-RU')}}`;

          wonItems.forEach(item => {{
            const card = document.createElement('div');
            card.className = `multi-res-card rare-${{item.rarity}}`;
            card.innerHTML = `
              <img src="${{item.image}}" alt="${{item.name}}">
              <div class="multi-res-card-name">${{item.name}}</div>
              <div class="multi-res-card-price">🪙 ${{item.price.toLocaleString('ru-RU')}}</div>
            `;
            grid.appendChild(card);
          }});

          multiOverlay.style.display = 'flex';
        }}, 1500);

      }} else {{
        const winIndex = 36;
        const wonSkin = generatedItemsTape[winIndex];

        const itemWidth = 110;
        const containerWidth = document.querySelector('.tape-container').offsetWidth;
        const jitter = (Math.random() * 60) - 30;
        const targetOffset = (winIndex * itemWidth) + (itemWidth / 2) - (containerWidth / 2) + jitter;

        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 4.8s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = `translateX(-${{targetOffset}}px)`;

        setTimeout(() => {{
          state.isOpeningCase = false;
          document.getElementById('caseModal').style.display = 'none';

          const finalWonItem = {{ uid: Date.now(), ...wonSkin }};
          state.inventory.unshift(finalWonItem);
          updateBalance();
          renderInventory();

          document.getElementById('winSkinImg').src = finalWonItem.image;
          document.getElementById('winSkinName').textContent = `${{finalWonItem.type}} | ${{finalWonItem.name}}`;
          document.getElementById('winSkinPrice').textContent = `🪙 +${{finalWonItem.price.toLocaleString('ru-RU')}}`;
          document.getElementById('winOverlay').style.display = 'flex';
          triggerConfetti();
        }}, 5000);
      }}
    }}

    function closeMultiResult() {{
      document.getElementById('multiResultOverlay').style.display = 'none';
    }}

    // Initial setup
    renderMarket();
    renderInventory();
    updateBalance();
    selectCoinBet(100);
    selectTarget(CATALOG[6]);
  </script>
</body>
</html>
"""

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Redesigned UI like upgrader.best and added win/lose animations!")
