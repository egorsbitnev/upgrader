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
  <title>UPGRADER CS2</title>
  <style>
    :root {{
      --bg-main: #0e131d;
      --bg-panel: #141a27;
      --bg-card: #192030;
      --bg-card-hover: #1f273b;
      --bg-card-active: #242e45;
      --accent-green: #00c74d;
      --accent-yellow: #f5a623;
      --accent-blue: #3b82f6;
      --accent-red: #ef4444;
      --text-white: #f3f4f6;
      --text-muted: #838fa5;
      --border: #222c3f;
      --border-light: #2b374e;
    }}
    * {{
      box-sizing: border-box;
      user-select: none;
      -webkit-user-select: none;
      -webkit-tap-highlight-color: transparent;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    }}
    html, body {{
      width: 100%;
      height: 100%;
      overflow: hidden;
      background: var(--bg-main);
      color: var(--text-white);
    }}
    body {{
      display: flex;
      flex-direction: column;
    }}

    /* HEADER UPGRADER STYLE (CLEAN & DARK) */
    header {{
      background: #111723;
      border-bottom: 1px solid var(--border);
      padding: 8px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      flex-shrink: 0;
      height: 48px;
    }}
    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .brand-icon {{
      width: 28px;
      height: 28px;
      background: #2563eb;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-weight: 900;
      font-size: 13px;
    }}
    .brand-name {{
      font-size: 16px;
      font-weight: 800;
      letter-spacing: 0.5px;
      color: #fff;
    }}
    .brand-badge {{
      font-size: 10px;
      font-weight: 700;
      background: #1e293b;
      color: #94a3b8;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid var(--border);
    }}

    .user-profile {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .btn-sound {{
      background: #1a2233;
      border: 1px solid var(--border);
      color: var(--text-muted);
      border-radius: 50%;
      width: 28px;
      height: 28px;
      cursor: pointer;
      font-size: 13px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .balance-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #161e2e;
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 8px;
    }}
    .balance-val {{
      font-weight: 800;
      font-size: 13px;
      color: var(--accent-yellow);
    }}
    .btn-deposit {{
      background: var(--accent-green);
      border: none;
      color: #0b111a;
      font-weight: 900;
      font-size: 15px;
      width: 26px;
      height: 26px;
      border-radius: 6px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: opacity 0.15s;
    }}
    .btn-deposit:active {{ opacity: 0.8; }}

    /* NAV TABS */
    .top-nav {{
      display: flex;
      background: #101624;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }}
    .top-nav-btn {{
      flex: 1;
      padding: 8px 0;
      text-align: center;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }}
    .top-nav-btn.active {{
      color: #fff;
      border-bottom-color: var(--accent-blue);
      background: rgba(59, 130, 246, 0.05);
    }}

    /* MAIN VIEWPORT */
    .viewport {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* ========================================================
       TOP ARENA (UPGRADER WHEEL + SLOTS)
       ======================================================== */
    .upgrader-arena {{
      background: #111724;
      border-bottom: 1px solid var(--border);
      padding: 8px 12px;
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
    }}
    .arena-top-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 480px;
      gap: 10px;
    }}

    /* SLOTS: Left (Bet) / Right (Target) */
    .arena-slot {{
      flex: 1;
      height: 110px;
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: border-color 0.15s, background 0.15s;
    }}
    .arena-slot.active {{
      border-color: #3b82f6;
      background: #1a2438;
    }}
    .arena-slot.target.active {{
      border-color: var(--accent-green);
    }}
    .slot-tag {{
      position: absolute;
      top: 4px;
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
    }}
    .slot-img-box {{
      width: 70px;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 8px;
    }}
    .slot-img-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .slot-name {{
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      max-width: 130px;
      margin-top: 2px;
    }}
    .slot-price {{
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-yellow);
    }}

    /* DIAL WHEEL (NO WHITE DOT, CLEAN SHARP ARROW) */
    .dial-container {{
      position: relative;
      width: 136px;
      height: 136px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .dial-svg {{
      width: 136px;
      height: 136px;
      transform: rotate(-90deg);
    }}
    .dial-track {{
      fill: transparent;
      stroke: #1e273b;
      stroke-width: 10;
    }}
    .dial-arc {{
      fill: transparent;
      stroke: var(--accent-green);
      stroke-width: 10;
      stroke-linecap: round;
      stroke-dasharray: 364;
      stroke-dashoffset: 364;
      transition: stroke-dashoffset 0.25s ease;
    }}

    /* THE NEEDLE / POINTER (ONLY ARROW, NO WHITE CENTER DOT) */
    .dial-needle {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 2px;
      height: 65px;
      margin-left: -1px;
      margin-top: -65px;
      transform-origin: bottom center;
      transform: rotate(0deg);
      transition: transform 4s cubic-bezier(0.12, 0.8, 0.22, 1);
      z-index: 10;
      pointer-events: none;
    }}
    .dial-needle::before {{
      content: '';
      position: absolute;
      top: -3px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 13px solid #ffffff;
    }}

    .dial-center-info {{
      position: absolute;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      pointer-events: none;
    }}
    .dial-chance-num {{
      font-size: 22px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1;
    }}
    .dial-chance-label {{
      font-size: 9px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: 2px;
    }}
    .dial-multiplier {{
      font-size: 11px;
      font-weight: 800;
      color: #60a5fa;
      margin-top: 1px;
    }}

    /* PRESET BUTTONS + UPGRADE BUTTON */
    .arena-bottom-row {{
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      max-width: 480px;
      gap: 6px;
      margin-top: 6px;
    }}
    .preset-chips-row {{
      display: flex;
      gap: 6px;
      width: 100%;
    }}
    .preset-btn {{
      flex: 1;
      background: #172030;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 0;
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-align: center;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .preset-btn:hover {{
      background: #202b40;
      color: #fff;
    }}
    .preset-btn:active {{
      background: #2563eb;
      color: #fff;
    }}

    .btn-upgrade-action {{
      width: 100%;
      padding: 10px 0;
      background: var(--accent-green);
      color: #0b111a;
      font-size: 14px;
      font-weight: 900;
      letter-spacing: 0.5px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .btn-upgrade-action:hover:not(:disabled) {{
      background: #00d955;
    }}
    .btn-upgrade-action:disabled {{
      background: #1e293b;
      color: #475569;
      cursor: not-allowed;
    }}

    /* ========================================================
       SPLIT DUAL BOTTOM SECTION: INVENTORY (LEFT) & MARKET (RIGHT)
       ======================================================== */
    .dual-bottom-panels {{
      flex: 1;
      display: flex;
      overflow: hidden;
      background: var(--bg-main);
    }}

    /* LEFT PANE: INVENTORY */
    .panel-inventory {{
      flex: 1;
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--border);
      background: #0c101a;
      overflow: hidden;
    }}
    /* RIGHT PANE: MARKET */
    .panel-market {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: #0e1422;
      overflow: hidden;
    }}

    .panel-header {{
      background: #141a28;
      border-bottom: 1px solid var(--border);
      padding: 6px 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-shrink: 0;
      height: 32px;
    }}
    .panel-title {{
      font-size: 11px;
      font-weight: 800;
      color: #cbd5e1;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}
    .panel-badge {{
      font-size: 10px;
      font-weight: 700;
      color: var(--text-muted);
    }}

    .filter-mini-bar {{
      display: flex;
      gap: 4px;
      padding: 4px 6px;
      background: #111622;
      border-bottom: 1px solid var(--border);
      overflow-x: auto;
      scrollbar-width: none;
      flex-shrink: 0;
    }}
    .filter-mini-bar::-webkit-scrollbar {{ display: none; }}
    .f-chip {{
      padding: 2px 7px;
      font-size: 9.5px;
      font-weight: 700;
      background: #1a2233;
      color: var(--text-muted);
      border-radius: 4px;
      border: 1px solid var(--border);
      white-space: nowrap;
      cursor: pointer;
    }}
    .f-chip.active {{
      background: #2563eb;
      color: #fff;
      border-color: #2563eb;
    }}

    .dual-grid {{
      flex: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 6px;
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px;
      align-content: start;
    }}
    @media (min-width: 600px) {{
      .dual-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}
    @media (min-width: 900px) {{
      .dual-grid {{
        grid-template-columns: repeat(4, 1fr);
      }}
    }}

    /* SKIN CARDS (CLEAN UPGRADER LOOK) */
    .mini-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 6px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      transition: border-color 0.12s, background 0.12s;
    }}
    .mini-card:hover {{
      background: var(--bg-card-hover);
      border-color: #3b4866;
    }}
    .mini-card.selected {{
      border-color: #3b82f6;
      background: #1b263b;
    }}
    .mini-card.target-selected {{
      border-color: var(--accent-green);
      background: #142820;
    }}
    .mini-card.rare-contraband {{ border-bottom: 2px solid #e4ae39; }}
    .mini-card.rare-gold {{ border-bottom: 2px solid #ffd700; }}
    .mini-card.rare-covert {{ border-bottom: 2px solid #eb4b4b; }}
    .mini-card.rare-classified {{ border-bottom: 2px solid #d32ce6; }}
    .mini-card.rare-restricted {{ border-bottom: 2px solid #8847ff; }}
    .mini-card.rare-milspec {{ border-bottom: 2px solid #4b69ff; }}

    .mini-card-img {{
      width: 100%;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 3px;
    }}
    .mini-card-img img {{
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
    }}
    .mini-card-name {{
      font-size: 10px;
      font-weight: 700;
      color: #fff;
      line-height: 1.15;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .mini-card-type {{
      font-size: 9px;
      color: var(--text-muted);
      margin: 1px 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .mini-card-price {{
      font-size: 10px;
      font-weight: 800;
      color: var(--accent-yellow);
    }}

    /* ================= CASES VIEW ================= */
    #view-cases {{
      display: none;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      background: var(--bg-main);
      padding: 12px;
    }}
    .cases-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
      gap: 10px;
    }}
    .case-card {{
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 10px 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
    }}
    .case-card-img {{
      width: 85px;
      height: 65px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 6px;
    }}
    .case-card-img img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .case-card-name {{
      font-weight: 700;
      font-size: 12px;
      color: #fff;
      margin-bottom: 6px;
    }}
    .case-card-btn {{
      background: #d97706;
      color: #fff;
      font-weight: 800;
      font-size: 11px;
      padding: 5px 0;
      border-radius: 6px;
      border: none;
      cursor: pointer;
      width: 100%;
      margin-top: auto;
    }}

    /* CASE MODAL */
    .case-modal {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(4px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 12px;
    }}
    .case-modal-box {{
      width: 100%;
      max-width: 380px;
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}
    .tape-container {{
      width: 100%;
      height: 96px;
      background: #090c14;
      border: 1px solid var(--border);
      border-radius: 8px;
      position: relative;
      overflow: hidden;
      margin: 12px 0 14px;
    }}
    .tape-pointer {{
      position: absolute;
      top: 0; bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 2px;
      background: var(--accent-yellow);
      z-index: 10;
    }}
    .tape-track {{
      display: flex;
      height: 100%;
      position: absolute;
      left: 0; top: 0;
      will-change: transform;
    }}
    .tape-item {{
      width: 90px;
      height: 100%;
      background: #121824;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 4px;
      flex-shrink: 0;
    }}
    .tape-item.rare-gold {{ border-bottom: 2px solid #ffd700; }}
    .tape-item.rare-covert {{ border-bottom: 2px solid #eb4b4b; }}
    .tape-item.rare-classified {{ border-bottom: 2px solid #d32ce6; }}
    .tape-item.rare-restricted {{ border-bottom: 2px solid #8847ff; }}
    .tape-item.rare-milspec {{ border-bottom: 2px solid #4b69ff; }}
    .tape-item-img {{
      width: 50px;
      height: 38px;
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
      font-size: 8.5px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      text-align: center;
      margin-top: 2px;
    }}
    .case-actions {{
      display: flex;
      gap: 8px;
      width: 100%;
    }}
    .case-btn {{
      flex: 1;
      padding: 9px 0;
      border-radius: 6px;
      border: none;
      font-weight: 800;
      font-size: 12px;
      cursor: pointer;
    }}
    .case-btn-1x {{ background: var(--accent-green); color: #0b111a; }}
    .case-btn-10x {{ background: var(--accent-yellow); color: #0b111a; }}

    /* RESULTS OVERLAYS */
    .result-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(4px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1200;
      padding: 16px;
    }}
    .result-dialog-box {{
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px 16px;
      width: 100%;
      max-width: 310px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }}
    .result-dialog-box.win {{ border-color: var(--accent-green); }}
    .result-dialog-box.lose {{ border-color: var(--accent-red); }}
    .res-title {{
      font-size: 18px;
      font-weight: 900;
      margin-bottom: 6px;
    }}
    .res-title.win {{ color: var(--accent-green); }}
    .res-title.lose {{ color: var(--accent-red); }}
    .res-img-box {{
      width: 130px;
      height: 85px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 8px 0;
    }}
    .res-img-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
    }}
    .res-btn {{
      margin-top: 14px;
      width: 100%;
      padding: 10px;
      border-radius: 6px;
      border: none;
      font-weight: 800;
      font-size: 13px;
      cursor: pointer;
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="brand-wrap">
      <div class="brand-icon">UP</div>
      <div class="brand-name">UPGRADER</div>
      <div class="brand-badge">CS2</div>
    </div>
    <div class="user-profile">
      <button class="btn-sound" id="soundToggleBtn" onclick="AudioEngine.toggleMute()">🔊</button>
      <div class="balance-pill">
        <span>🪙</span>
        <span class="balance-val" id="userBalanceDisplay">1,000</span>
      </div>
      <button class="btn-deposit" title="Пополнить бесплатно (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>
  </header>

  <!-- TOP NAV -->
  <div class="top-nav">
    <div class="top-nav-btn active" id="navItemUpgrader" onclick="switchMainView('upgrader')">
      <span>⚡</span> Апгрейдер
    </div>
    <div class="top-nav-btn" id="navItemCases" onclick="switchMainView('cases')">
      <span>📦</span> Кейсы CS2
    </div>
  </div>

  <div class="viewport">

    <!-- ================= VIEW 1: UPGRADER ================= -->
    <div id="view-upgrader" style="display: flex; flex-direction: column; height: 100%;">
      
      <!-- TOP ARENA (UPGRADER WHEEL + SLOTS) -->
      <div class="upgrader-arena">
        <div class="arena-top-row">
          
          <!-- Left: User Bet Slot -->
          <div class="arena-slot active" id="sourceSlot">
            <span class="slot-tag">Ваша ставка</span>
            <div class="slot-img-box" id="sourceImgBox">
              <span style="font-size: 26px;">🪙</span>
            </div>
            <div class="slot-name" id="sourceTitle">100 Монет</div>
            <div class="slot-price" id="sourcePrice">🪙 100</div>
          </div>

          <!-- Center: Dial Wheel (No white center circle) -->
          <div class="dial-container">
            <svg class="dial-svg">
              <circle class="dial-track" cx="68" cy="68" r="58"></circle>
              <circle class="dial-arc" id="winArc" cx="68" cy="68" r="58"></circle>
            </svg>

            <!-- Arrow only without white center hub -->
            <div class="dial-needle" id="needle"></div>

            <div class="dial-center-info">
              <span class="dial-chance-num" id="chanceDisplay">0%</span>
              <span class="dial-chance-label">Шанс</span>
              <span class="dial-multiplier" id="multDisplay">x0.00</span>
            </div>
          </div>

          <!-- Right: Target Slot -->
          <div class="arena-slot target active" id="targetSlot">
            <span class="slot-tag">Цель</span>
            <div class="slot-img-box" id="targetImgBox">
              <span style="font-size: 24px;">🎯</span>
            </div>
            <div class="slot-name" id="targetTitle">Выберите скин</div>
            <div class="slot-price" id="targetPrice">-</div>
          </div>

        </div>

        <!-- Presets and Upgrade Button -->
        <div class="arena-bottom-row">
          <div class="preset-chips-row">
            <div class="preset-btn" onclick="applyMultiplierTarget(1.5)">1.5x</div>
            <div class="preset-btn" onclick="applyMultiplierTarget(2)">2x</div>
            <div class="preset-btn" onclick="applyMultiplierTarget(5)">5x</div>
            <div class="preset-btn" onclick="applyMultiplierTarget(10)">10x</div>
            <div class="preset-btn" onclick="applyMultiplierTarget(20)">20x</div>
            <div class="preset-btn" onclick="applyMultiplierTarget(50)">50x</div>
          </div>

          <button class="btn-upgrade-action" id="upgradeBtn" disabled onclick="startUpgrade()">
            СДЕЛАТЬ АПГРЕЙД
          </button>
        </div>
      </div>

      <!-- DUAL BOTTOM SECTION: SPLIT IN TWO HALVES (INVENTORY ON LEFT, MARKET ON RIGHT) -->
      <div class="dual-bottom-panels">
        
        <!-- LEFT HALF: USER INVENTORY -->
        <div class="panel-inventory">
          <div class="panel-header">
            <span class="panel-title">🎒 Инвентарь</span>
            <span class="panel-badge"><span id="invCount">0</span> предм.</span>
          </div>
          <div class="dual-grid" id="inventoryGrid"></div>
        </div>

        <!-- RIGHT HALF: SKINS MARKET -->
        <div class="panel-market">
          <div class="panel-header">
            <span class="panel-title">🛒 Магазин целей</span>
            <span class="panel-badge"><span id="marketCount">0</span> шт.</span>
          </div>
          <div class="filter-mini-bar" id="marketFilterBar">
            <div class="f-chip active" onclick="filterMarket('all', this)">Все</div>
            <div class="f-chip" onclick="filterMarket('knife', this)">Ножи/Перчатки</div>
            <div class="f-chip" onclick="filterMarket('rifle', this)">Винтовки</div>
            <div class="f-chip" onclick="filterMarket('pistol', this)">Пистолеты</div>
            <div class="f-chip" onclick="filterMarket('cheap', this)">До 1,000</div>
          </div>
          <div class="dual-grid" id="marketGrid"></div>
        </div>

      </div>

    </div>

    <!-- ================= VIEW 2: CASES ================= -->
    <div id="view-cases">
      <div class="cases-grid" id="casesGrid"></div>
    </div>

  </div>

  <!-- CASE OPENING MODAL -->
  <div class="case-modal" id="caseModal">
    <div class="case-modal-box">
      <div style="display: flex; justify-content: space-between; width: 100%;">
        <span style="font-weight: 800; font-size: 15px;" id="caseModalTitle">Кейс</span>
        <span style="cursor: pointer; color: var(--text-muted); font-size: 18px;" onclick="closeCaseModal()">✕</span>
      </div>

      <div class="tape-container">
        <div class="tape-pointer"></div>
        <div class="tape-track" id="tapeTrack"></div>
      </div>

      <div class="case-actions">
        <button class="case-btn case-btn-1x" id="caseOpen1xBtn" onclick="spinCase(1)">1x</button>
        <button class="case-btn case-btn-10x" id="caseOpen10xBtn" onclick="spinCase(10)">⚡ 10x</button>
      </div>
    </div>
  </div>

  <!-- RESULT OVERLAY -->
  <div class="result-overlay" id="resultOverlay">
    <div class="result-dialog-box" id="resultDialogBox">
      <div class="res-title" id="resTitle">АПГРЕЙД</div>
      <div class="res-img-box">
        <img id="resImg" src="" alt="Skin">
      </div>
      <div style="font-size: 14px; font-weight: 800;" id="resName">AK-47</div>
      <div style="font-size: 13px; font-weight: 800; color: var(--accent-yellow); margin-top: 2px;" id="resPrice">🪙 0</div>
      <button class="res-btn" style="background:#2563eb; color:#fff;" onclick="closeResult()">ЗАКРЫТЬ</button>
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

    const CIRCLE_CIRCUMFERENCE = 2 * Math.PI * 58; // ~364.4px

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
      document.getElementById('navItemUpgrader').classList.toggle('active', mode === 'upgrader');
      document.getElementById('navItemCases').classList.toggle('active', mode === 'cases');
      document.getElementById('view-upgrader').style.display = mode === 'upgrader' ? 'flex' : 'none';
      document.getElementById('view-cases').style.display = mode === 'cases' ? 'flex' : 'none';
      if (mode === 'cases') renderCases();
    }}

    function filterMarket(filter, el) {{
      state.currentFilter = filter;
      document.querySelectorAll('.f-chip').forEach(c => c.classList.remove('active'));
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

      document.querySelectorAll('#marketGrid .mini-card').forEach(c => c.classList.remove('target-selected'));
      const activeCard = document.getElementById(`target-card-${{skin.id}}`);
      if (activeCard) activeCard.classList.add('target-selected');

      recalcChance();
    }}

    function selectSourceItem(item) {{
      if (state.isRolling) return;
      state.selectedSource = item;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgBox').innerHTML = `<img src="${{item.image}}" alt="${{item.name}}">`;
      document.getElementById('sourceTitle').textContent = `${{item.type}} | ${{item.name}}`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{item.price.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .mini-card').forEach(c => c.classList.remove('selected'));
      const activeCard = document.getElementById(`inv-card-${{item.uid}}`);
      if (activeCard) activeCard.classList.add('selected');

      recalcChance();
    }}

    function selectCoinBet(amount) {{
      if (state.isRolling) return;
      state.selectedSource = null;
      state.coinBet = amount;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgBox').innerHTML = `<span style="font-size: 26px;">🪙</span>`;
      document.getElementById('sourceTitle').textContent = `${{amount.toLocaleString('ru-RU')}} Монет`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{amount.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .mini-card').forEach(c => c.classList.remove('selected'));
      recalcChance();
    }}

    function applyMultiplierTarget(mult) {{
      const sourceVal = getSourceValue();
      const targetVal = sourceVal * mult;
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

    // REALISTIC UPGRADER.BEST MATHEMATICS (HONEST 95% HOUSE PAYOUT)
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

      // Standard casino house edge 95%
      let chance = (sourceVal / targetVal) * 95;
      if (chance > 95) chance = 95;
      if (chance < 0.2) chance = 0.2;

      const mult = (targetVal / sourceVal).toFixed(2);

      chanceText.textContent = chance.toFixed(1) + "%";
      multText.textContent = "x" + mult;

      // Arc offset proportional to actual win chance
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
        return true;
      }});

      filtered.forEach(skin => {{
        const isSelected = state.selectedTarget && state.selectedTarget.id === skin.id;
        const card = document.createElement('div');
        card.id = `target-card-${{skin.id}}`;
        card.className = `mini-card rare-${{skin.rarity}} ${{isSelected ? 'target-selected' : ''}}`;
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${{skin.image}}" alt="${{skin.name}}" loading="lazy">
          </div>
          <div class="mini-card-name">${{skin.name}}</div>
          <div class="mini-card-type">${{skin.type}}</div>
          <div class="mini-card-price">🪙 ${{skin.price.toLocaleString('ru-RU')}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderInventory() {{
      const grid = document.getElementById('inventoryGrid');
      grid.innerHTML = '';

      // Coin betting card
      const coinCard = document.createElement('div');
      coinCard.className = `mini-card`;
      coinCard.style.borderColor = 'var(--accent-yellow)';
      coinCard.onclick = () => {{
        const val = prompt("Введите сумму ставки монет:", state.coinBet || "100");
        const num = parseInt(val, 10);
        if (num && num > 0) selectCoinBet(num);
      }};
      coinCard.innerHTML = `
        <div class="mini-card-img">
          <span style="font-size: 24px;">🪙</span>
        </div>
        <div class="mini-card-name">Монеты</div>
        <div class="mini-card-type">Ставка</div>
        <div class="mini-card-price">🪙 Изменить</div>
      `;
      grid.appendChild(coinCard);

      state.inventory.forEach(item => {{
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${{item.uid}}`;
        card.className = `mini-card rare-${{item.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="mini-card-img">
            <img src="${{item.image}}" alt="${{item.name}}" loading="lazy">
          </div>
          <div class="mini-card-name">${{item.name}}</div>
          <div class="mini-card-type">${{item.type}}</div>
          <div class="mini-card-price">🪙 ${{item.price.toLocaleString('ru-RU')}}</div>
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
          alert("Недостаточно монет! Нажмите '+' возле баланса.");
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

      let chance = (sourceVal / targetVal) * 95;
      if (sourceVal >= targetVal) chance = 100;
      if (chance > 95) chance = 95;
      if (chance < 0.2) chance = 0.2;

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
      const overlay = document.getElementById('resultOverlay');
      const box = document.getElementById('resultDialogBox');
      const title = document.getElementById('resTitle');
      const img = document.getElementById('resImg');
      const name = document.getElementById('resName');
      const price = document.getElementById('resPrice');

      if (isWin) {{
        const wonItem = {{ uid: Date.now(), ...state.selectedTarget }};
        state.inventory.unshift(wonItem);
        box.className = 'result-dialog-box win';
        title.className = 'res-title win';
        title.textContent = '🎉 АПГРЕЙД УДАЛСЯ!';
        img.src = wonItem.image;
        name.textContent = `${{wonItem.type}} | ${{wonItem.name}}`;
        price.textContent = `🪙 +${{wonItem.price.toLocaleString('ru-RU')}}`;
      }} else {{
        box.className = 'result-dialog-box lose';
        title.className = 'res-title lose';
        title.textContent = '💔 АПГРЕЙД ПРОВАЛЕН';
        img.src = 'https://community.akamai.steamstatic.com/economy/image/i0CoZ81Ui0m-9KwlBY1L_18myuGuq1wfhWSaZgMttyVfPaERSR0Wqmu7LAocGJKz2lu_XuWbwcuyMESA4Fdl-4nnpU7iQA3-kKnr8ytd6s2lfa9_Kb6VXmPGwuogsbNvSyi3zR4jsTnQztyqdS6QP1IoXpoiEeAC5Be5l9CxKaq8sIvgdE5J';
        name.textContent = 'Предмет сгорел';
        price.textContent = '🪙 0';
      }}

      overlay.style.display = 'flex';
      updateBalance();
      renderInventory();
    }}

    function closeResult() {{
      document.getElementById('resultOverlay').style.display = 'none';
      state.selectedSource = null;
      selectCoinBet(100);
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
          <button class="case-card-btn">🪙 ${{c.price.toLocaleString('ru-RU')}}</button>
        `;
        grid.appendChild(card);
      }});
    }}

    let generatedItemsTape = [];

    function openCaseModal(caseData) {{
      if (state.isOpeningCase) return;
      state.activeCase = caseData;
      document.getElementById('caseModalTitle').textContent = caseData.name;
      document.getElementById('caseOpen1xBtn').textContent = `1x 🪙 ${{caseData.price.toLocaleString('ru-RU')}}`;
      document.getElementById('caseOpen10xBtn').textContent = `⚡ 10x 🪙 ${{(caseData.price * 10).toLocaleString('ru-RU')}}`;
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
      if (rand < 1.0) chosenRarity = 'gold';
      else if (rand < 5.0) chosenRarity = 'covert';
      else if (rand < 20.0) chosenRarity = 'classified';
      else if (rand < 45.0) chosenRarity = 'restricted';

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
        alert("Недостаточно монет! Нажмите '+' возле баланса.");
        return;
      }}

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
      track.style.transform = `translateX(-${{targetOffset}}px)`;

      setTimeout(() => {{
        state.isOpeningCase = false;
        document.getElementById('caseModal').style.display = 'none';

        const finalWonItem = {{ uid: Date.now(), ...wonSkin }};
        state.inventory.unshift(finalWonItem);
        updateBalance();
        renderInventory();

        showUpgradeResult(true);
        document.getElementById('resTitle').textContent = '🎁 ВЫПАЛ СКИН!';
        document.getElementById('resImg').src = finalWonItem.image;
        document.getElementById('resName').textContent = `${{finalWonItem.type}} | ${{finalWonItem.name}}`;
        document.getElementById('resPrice').textContent = `🪙 +${{finalWonItem.price.toLocaleString('ru-RU')}}`;
      }}, 4700);
    }}

    // Initial setup
    renderMarket();
    renderInventory();
    updateBalance();
    selectCoinBet(100);
    selectTarget(CATALOG[10]);
  </script>
</body>
</html>
"""

with open(r"C:\Users\Егор\.gemini\antigravity\scratch\idle-upgrader-game\index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Split bottom inventory/market, removed neon & center dot, fixed chances!")
