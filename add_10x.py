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
  <title>UPGRADER CS2 - Апгрейдер и Кейсы</title>
  <style>
    :root {{
      --bg: #0b0f19;
      --bg-panel: #121927;
      --bg-card: #182235;
      --bg-card-hover: #1f2b42;
      --accent-green: #00e701;
      --accent-neon: #00f2fe;
      --accent-gold: #ffb703;
      --accent-red: #ff3366;
      --accent-purple: #9d4edd;
      --text: #ffffff;
      --text-muted: #8493ad;
      --border: #223049;
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
      background-color: var(--bg);
      color: var(--text);
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}

    /* Header */
    header {{
      background: #0f1523;
      border-bottom: 1px solid var(--border);
      padding: 10px 16px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 10;
      flex-shrink: 0;
    }}
    .logo-box {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .logo-badge {{
      background: linear-gradient(135deg, #00f2fe, #4facfe);
      color: #0b0f19;
      font-weight: 900;
      font-size: 13px;
      padding: 4px 8px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }}
    .logo-text {{
      font-size: 17px;
      font-weight: 900;
      letter-spacing: 1.5px;
      background: linear-gradient(90deg, #fff, #b4d5fe);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}
    .balance-box {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #172133;
      border: 1px solid var(--border);
      padding: 5px 12px;
      border-radius: 20px;
    }}
    .balance-val {{
      font-weight: 800;
      font-size: 15px;
      color: var(--accent-gold);
    }}
    .add-coins-btn {{
      background: linear-gradient(135deg, #00c853, #00e676);
      border: none;
      color: #0d111a;
      font-weight: 900;
      font-size: 14px;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: transform 0.1s;
    }}
    .add-coins-btn:active {{ transform: scale(0.9); }}

    /* Navigation Mode Bar */
    .top-nav-bar {{
      display: flex;
      background: #0c121d;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }}
    .nav-tab {{
      flex: 1;
      padding: 10px;
      text-align: center;
      font-weight: 800;
      font-size: 13px;
      color: var(--text-muted);
      cursor: pointer;
      border-bottom: 2px solid transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .nav-tab.active {{
      color: #fff;
      border-bottom-color: var(--accent-neon);
      background: rgba(0, 242, 254, 0.06);
    }}

    /* Main Container */
    .app-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* UPGRADE VIEW */
    #view-upgrader {{
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow: hidden;
    }}

    .upgrade-arena {{
      background: radial-gradient(circle at center, #162137 0%, #0d121e 100%);
      padding: 10px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      border-bottom: 1px solid var(--border);
      position: relative;
      flex-shrink: 0;
    }}

    .duel-slots {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      max-width: 440px;
      margin-bottom: 6px;
    }}
    .slot-item {{
      background: var(--bg-card);
      border: 1.5px dashed var(--border);
      border-radius: 12px;
      width: 140px;
      height: 96px;
      padding: 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      cursor: pointer;
      position: relative;
      transition: all 0.2s;
    }}
    .slot-item.active {{
      border-style: solid;
      border-color: #3b5078;
      background: #19243a;
    }}
    .slot-item.target-slot.active {{
      border-color: var(--accent-neon);
      box-shadow: 0 0 14px rgba(0, 242, 254, 0.25);
    }}
    .slot-label {{
      position: absolute;
      top: 4px;
      font-size: 9px;
      text-transform: uppercase;
      font-weight: 700;
      color: var(--text-muted);
    }}
    .slot-img-wrap {{
      width: 58px;
      height: 44px;
      margin-top: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .slot-img-wrap img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 4px 6px rgba(0, 0, 0, 0.6));
    }}
    .slot-coin-icon {{ font-size: 32px; }}
    .slot-title {{
      font-size: 11px;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 125px;
      margin-top: 2px;
    }}
    .slot-price {{
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-gold);
    }}

    .circle-container {{
      position: relative;
      width: 160px;
      height: 160px;
      margin: 2px 0 8px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .progress-ring {{
      transform: rotate(-90deg);
      width: 160px;
      height: 160px;
    }}
    .progress-ring__circle-bg {{
      stroke: #1c263c;
      stroke-width: 12;
      fill: transparent;
    }}
    .progress-ring__circle {{
      stroke: var(--accent-green);
      stroke-width: 12;
      stroke-linecap: round;
      fill: transparent;
      stroke-dasharray: 414;
      stroke-dashoffset: 414;
      transition: stroke-dashoffset 0.4s ease;
      filter: drop-shadow(0 0 8px rgba(0, 231, 1, 0.6));
    }}

    .needle {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 4px;
      height: 76px;
      margin-left: -2px;
      margin-top: -76px;
      transform-origin: bottom center;
      transform: rotate(0deg);
      transition: transform 4s cubic-bezier(0.12, 0.8, 0.22, 1);
      z-index: 5;
      pointer-events: none;
    }}
    .needle::before {{
      content: '';
      position: absolute;
      top: -3px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 7px solid transparent;
      border-right: 7px solid transparent;
      border-top: 14px solid #ffffff;
      filter: drop-shadow(0 0 6px #fff);
    }}
    .needle-center {{
      position: absolute;
      width: 16px;
      height: 16px;
      background: #ffffff;
      border-radius: 50%;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 10px rgba(0, 242, 254, 0.8);
      z-index: 6;
    }}

    .circle-inner-info {{
      position: absolute;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      pointer-events: none;
    }}
    .chance-value {{
      font-size: 25px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -0.5px;
      line-height: 1;
      text-shadow: 0 0 12px rgba(0, 231, 1, 0.5);
    }}
    .chance-label {{
      font-size: 10px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      margin-top: 2px;
    }}
    .multiplier-val {{
      font-size: 12px;
      font-weight: 800;
      color: var(--accent-neon);
      margin-top: 1px;
    }}

    .upgrade-action-btn {{
      background: linear-gradient(135deg, #00e701, #00b301);
      color: #0b0f19;
      font-size: 14px;
      font-weight: 900;
      letter-spacing: 1px;
      padding: 10px 24px;
      border-radius: 12px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 18px rgba(0, 231, 1, 0.35);
      transition: all 0.2s;
      width: 100%;
      max-width: 320px;
    }}
    .upgrade-action-btn:active {{ transform: scale(0.97); }}
    .upgrade-action-btn:disabled {{
      background: #25334d;
      color: #556885;
      box-shadow: none;
      cursor: not-allowed;
    }}

    /* SELECTION SECTION (BOTTOM HALF) */
    .selection-section {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg-panel);
      overflow: hidden;
    }}
    .section-tabs {{
      display: flex;
      border-bottom: 1px solid var(--border);
      background: #0f1523;
      flex-shrink: 0;
    }}
    .sec-tab-btn {{
      flex: 1;
      padding: 10px;
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--text-muted);
      font-weight: 800;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .sec-tab-btn.active {{
      color: var(--accent-neon);
      border-bottom-color: var(--accent-neon);
      background: rgba(0, 242, 254, 0.05);
    }}

    .filter-bar {{
      display: flex;
      gap: 6px;
      padding: 6px 12px;
      background: #111827;
      border-bottom: 1px solid var(--border);
      overflow-x: auto;
      scrollbar-width: none;
      flex-shrink: 0;
    }}
    .filter-bar::-webkit-scrollbar {{ display: none; }}
    .filter-chip {{
      padding: 3px 9px;
      font-size: 11px;
      font-weight: 700;
      background: #1a2335;
      color: var(--text-muted);
      border-radius: 12px;
      border: 1px solid var(--border);
      white-space: nowrap;
      cursor: pointer;
    }}
    .filter-chip.active {{
      background: var(--accent-neon);
      color: #0b0f19;
      border-color: var(--accent-neon);
    }}

    .skins-grid {{
      flex: 1;
      overflow-y: auto;
      padding: 8px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(105px, 1fr));
      gap: 8px;
      align-content: start;
    }}
    .skin-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 7px 5px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      transition: border-color 0.15s, transform 0.1s;
      position: relative;
      overflow: hidden;
    }}
    .skin-card:active {{ transform: scale(0.96); }}
    .skin-card.selected {{
      border-color: var(--accent-neon);
      box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
      background: #1e2c45;
    }}
    
    .skin-card.rare-contraband {{ border-bottom: 3px solid #e4ae39; }}
    .skin-card.rare-gold {{ border-bottom: 3px solid #ffd700; }}
    .skin-card.rare-covert {{ border-bottom: 3px solid #eb4b4b; }}
    .skin-card.rare-classified {{ border-bottom: 3px solid #d32ce6; }}
    .skin-card.rare-restricted {{ border-bottom: 3px solid #8847ff; }}
    .skin-card.rare-milspec {{ border-bottom: 3px solid #4b69ff; }}

    .skin-card-img-wrap {{
      width: 100%;
      height: 56px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 4px;
    }}
    .skin-card-img-wrap img {{
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 4px 6px rgba(0,0,0,0.5));
    }}
    .skin-name {{
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      line-height: 1.2;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-type {{
      font-size: 10px;
      color: var(--text-muted);
      margin: 1px 0 2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-price {{
      font-size: 11px;
      font-weight: 800;
      color: var(--accent-gold);
    }}

    /* ================= CASES VIEW ================= */
    #view-cases {{
      display: none;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      background: var(--bg);
      padding: 14px;
    }}
    .cases-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .cases-header h2 {{
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

    /* Tape Reel */
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
      top: 0;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 3px;
      background: #ffb703;
      box-shadow: 0 0 10px #ffb703;
      z-index: 10;
    }}
    .tape-pointer::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 8px solid #ffb703;
    }}
    .tape-pointer::after {{
      content: '';
      position: absolute;
      bottom: 0;
      left: 50%;
      transform: translateX(-50%);
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-bottom: 8px solid #ffb703;
    }}
    .tape-track {{
      display: flex;
      height: 100%;
      position: absolute;
      left: 0;
      top: 0;
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
      transition: transform 0.1s;
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
      transition: transform 0.1s;
    }}
    .case-open-action-btn:active, .case-open-10x-btn:active {{
      transform: scale(0.97);
    }}
    .case-open-action-btn:disabled, .case-open-10x-btn:disabled {{
      background: #25334d;
      color: #556885;
      box-shadow: none;
      cursor: not-allowed;
    }}
    .case-close-x {{
      position: absolute;
      top: 14px;
      right: 16px;
      color: var(--text-muted);
      font-size: 20px;
      cursor: pointer;
      background: none;
      border: none;
    }}

    /* Result Modals (Single) */
    .result-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(8, 12, 20, 0.88);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1100;
      animation: fadeIn 0.25s;
    }}
    @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}

    .result-dialog {{
      background: var(--bg-panel);
      border: 2px solid var(--border);
      border-radius: 18px;
      padding: 24px;
      width: 86%;
      max-width: 320px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
    }}
    .result-dialog.win {{ border-color: var(--accent-green); box-shadow: 0 0 30px rgba(0, 231, 1, 0.3); }}
    .result-dialog.lose {{ border-color: var(--accent-red); box-shadow: 0 0 30px rgba(255, 51, 102, 0.3); }}

    .res-title {{
      font-size: 20px;
      font-weight: 900;
      margin-bottom: 8px;
    }}
    .res-title.win {{ color: var(--accent-green); text-shadow: 0 0 12px rgba(0, 231, 1, 0.5); }}
    .res-title.lose {{ color: var(--accent-red); text-shadow: 0 0 12px rgba(255, 51, 102, 0.5); }}

    .res-skin-img-wrap {{
      width: 140px;
      height: 90px;
      margin: 10px 0;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .res-skin-img-wrap img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 6px 12px rgba(0,0,0,0.8));
    }}
    .res-skin-name {{ font-weight: 800; font-size: 15px; margin-top: 4px; }}
    .res-skin-price {{ font-weight: 800; font-size: 14px; color: var(--accent-gold); margin-top: 4px; }}
    .res-close-btn {{
      width: 100%;
      margin-top: 18px;
      padding: 12px;
      border-radius: 10px;
      background: #243049;
      border: none;
      color: white;
      font-weight: 800;
      font-size: 14px;
      cursor: pointer;
    }}
    .res-close-btn:active {{ background: #2e3e5f; }}

    /* 10X Case Result Modal */
    .multi-result-dialog {{
      background: var(--bg-panel);
      border: 2px solid var(--accent-gold);
      border-radius: 18px;
      padding: 18px;
      width: 92%;
      max-width: 520px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      box-shadow: 0 0 40px rgba(255, 183, 3, 0.35);
      animation: zoomIn 0.25s;
    }}
    @keyframes zoomIn {{ from {{ transform: scale(0.9); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}

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
      color: var(--accent-gold);
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
      position: relative;
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
      color: var(--accent-gold);
      margin-top: 2px;
    }}
  </style>
</head>
<body>

  <header>
    <div class="logo-box">
      <div class="logo-badge">CS2</div>
      <div class="logo-text">UPGRADER</div>
    </div>
    <div class="balance-box">
      <span>🪙</span>
      <span class="balance-val" id="userBalanceDisplay">1,000</span>
      <button class="add-coins-btn" title="Бесплатные монеты (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>
  </header>

  <div class="top-nav-bar">
    <div class="nav-tab active" id="navTabUpgrader" onclick="switchMainView('upgrader')">
      <span>⚡</span> Апгрейдер
    </div>
    <div class="nav-tab" id="navTabCases" onclick="switchMainView('cases')">
      <span>📦</span> Кейсы CS2
    </div>
  </div>

  <div class="app-content">

    <!-- ================= VIEW 1: UPGRADER ================= -->
    <div id="view-upgrader">
      <div class="upgrade-arena">
        <div class="duel-slots">
          <!-- Source Slot -->
          <div class="slot-item active" id="sourceSlot" onclick="switchTab('inventory')">
            <span class="slot-label">Ваша ставка</span>
            <div class="slot-img-wrap" id="sourceImgWrap">
              <span class="slot-coin-icon">🪙</span>
            </div>
            <div class="slot-title" id="sourceTitle">100 Монет</div>
            <div class="slot-price" id="sourcePrice">🪙 100</div>
          </div>

          <div style="font-size: 20px; font-weight: 900; color: var(--text-muted);">➜</div>

          <!-- Target Slot -->
          <div class="slot-item target-slot" id="targetSlot" onclick="switchTab('market')">
            <span class="slot-label">Целевой Скин</span>
            <div class="slot-img-wrap" id="targetImgWrap">
              <span style="font-size: 26px;">🎯</span>
            </div>
            <div class="slot-title" id="targetTitle">Выберите скин</div>
            <div class="slot-price" id="targetPrice">-</div>
          </div>
        </div>

        <!-- Dial Roulette Gauge -->
        <div class="circle-container">
          <svg class="progress-ring">
            <circle class="progress-ring__circle-bg" cx="80" cy="80" r="66"></circle>
            <circle class="progress-ring__circle" id="winArc" cx="80" cy="80" r="66"></circle>
          </svg>

          <div class="needle" id="needle"></div>
          <div class="needle-center"></div>

          <div class="circle-inner-info">
            <span class="chance-value" id="chanceDisplay">0%</span>
            <span class="chance-label">Шанс успеха</span>
            <span class="multiplier-val" id="multDisplay">x0.00</span>
          </div>
        </div>

        <button class="upgrade-action-btn" id="upgradeBtn" disabled onclick="startUpgrade()">
          СДЕЛАТЬ АПГРЕЙД
        </button>
      </div>

      <!-- TABS & LISTS -->
      <div class="selection-section">
        <div class="section-tabs">
          <button class="sec-tab-btn active" id="tabMarketBtn" onclick="switchTab('market')">Магазин скинов (<span id="marketCount">0</span>)</button>
          <button class="sec-tab-btn" id="tabInventoryBtn" onclick="switchTab('inventory')">Инвентарь (<span id="invCount">0</span>)</button>
        </div>

        <div class="filter-bar" id="marketFilterBar">
          <div class="filter-chip active" onclick="filterMarket('all', this)">Все</div>
          <div class="filter-chip" onclick="filterMarket('knife', this)">Ножи и перчатки</div>
          <div class="filter-chip" onclick="filterMarket('rifle', this)">Винтовки</div>
          <div class="filter-chip" onclick="filterMarket('pistol', this)">Пистолеты</div>
          <div class="filter-chip" onclick="filterMarket('cheap', this)">До 1,000</div>
          <div class="filter-chip" onclick="filterMarket('expensive', this)">10,000+</div>
        </div>

        <div class="skins-grid" id="marketGrid"></div>
        <div class="skins-grid" id="inventoryGrid" style="display: none;"></div>
      </div>
    </div>

    <!-- ================= VIEW 2: CASES ================= -->
    <div id="view-cases">
      <div class="cases-header">
        <h2>Оригинальные кейсы CS2</h2>
        <span style="font-size: 13px; color: var(--accent-gold); font-weight: 800;">🪙 Испытай удачу</span>
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

  <!-- Result Dialog Overlay (Single) -->
  <div class="result-overlay" id="resultOverlay">
    <div class="result-dialog" id="resultDialog">
      <div class="res-title" id="resTitle">🎉 УСПЕХ!</div>
      <div class="res-skin-img-wrap" id="resImgWrap">
        <img id="resImg" src="" alt="Skin">
      </div>
      <div class="res-skin-name" id="resName">AK-47 | Вулкан</div>
      <div class="res-skin-price" id="resPrice">🪙 2,800</div>
      <button class="res-close-btn" onclick="closeResult()">ЗАБРАТЬ В ИНВЕНТАРЬ</button>
    </div>
  </div>

  <!-- Result Dialog Overlay (10x Bulk Opening) -->
  <div class="result-overlay" id="multiResultOverlay">
    <div class="multi-result-dialog">
      <div class="multi-res-header">
        <div class="multi-res-title">🎁 ДРОП ИЗ 10 КЕЙСОВ</div>
        <div class="multi-res-total" id="multiResTotal">+🪙 0</div>
      </div>

      <div class="multi-res-grid" id="multiResGrid"></div>

      <button class="res-close-btn" onclick="closeMultiResult()">ЗАБРАТЬ ВСЕ В ИНВЕНТАРЬ</button>
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

    const CIRCLE_CIRCUMFERENCE = 2 * Math.PI * 66; // ~414px

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
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      if (el) el.classList.add('active');
      renderMarket();
    }}

    function selectTarget(skin) {{
      if (state.isRolling) return;
      state.selectedTarget = skin;
      document.getElementById('targetSlot').classList.add('active');
      document.getElementById('targetImgWrap').innerHTML = `<img src="${{skin.image}}" alt="${{skin.name}}">`;
      document.getElementById('targetTitle').textContent = `${{skin.type}} | ${{skin.name}}`;
      document.getElementById('targetPrice').textContent = `🪙 ${{skin.price.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#marketGrid .skin-card').forEach(c => c.classList.remove('selected'));
      const activeCard = document.getElementById(`target-card-${{skin.id}}`);
      if (activeCard) activeCard.classList.add('selected');

      recalcChance();
    }}

    function selectSourceItem(item) {{
      if (state.isRolling) return;
      state.selectedSource = item;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgWrap').innerHTML = `<img src="${{item.image}}" alt="${{item.name}}">`;
      document.getElementById('sourceTitle').textContent = `${{item.type}} | ${{item.name}}`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{item.price.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .skin-card').forEach(c => c.classList.remove('selected'));
      const activeCard = document.getElementById(`inv-card-${{item.uid}}`);
      if (activeCard) activeCard.classList.add('selected');

      recalcChance();
    }}

    function selectCoinBet(amount) {{
      if (state.isRolling) return;
      state.selectedSource = null;
      state.coinBet = amount;
      document.getElementById('sourceSlot').classList.add('active');
      document.getElementById('sourceImgWrap').innerHTML = `<span class="slot-coin-icon">🪙</span>`;
      document.getElementById('sourceTitle').textContent = `${{amount.toLocaleString('ru-RU')}} Монет`;
      document.getElementById('sourcePrice').textContent = `🪙 ${{amount.toLocaleString('ru-RU')}}`;

      document.querySelectorAll('#inventoryGrid .skin-card').forEach(c => c.classList.remove('selected'));
      recalcChance();
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

      let chance = (sourceVal / targetVal) * 95;
      if (chance > 92) chance = 92;
      if (chance < 0.2) chance = 0.2;

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
        card.className = `skin-card rare-${{skin.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="skin-card-img-wrap">
            <img src="${{skin.image}}" alt="${{skin.name}}" loading="lazy">
          </div>
          <div class="skin-name">${{skin.name}}</div>
          <div class="skin-type">${{skin.type}}</div>
          <div class="skin-price">🪙 ${{skin.price.toLocaleString('ru-RU')}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderInventory() {{
      const grid = document.getElementById('inventoryGrid');
      grid.innerHTML = '';

      const coinCard = document.createElement('div');
      coinCard.className = `skin-card`;
      coinCard.style.borderColor = 'var(--accent-gold)';
      coinCard.onclick = () => {{
        const val = prompt("Введите сумму ставки монет:", state.coinBet || "100");
        const num = parseInt(val, 10);
        if (num && num > 0) selectCoinBet(num);
      }};
      coinCard.innerHTML = `
        <div class="skin-card-img-wrap">
          <span style="font-size: 34px;">🪙</span>
        </div>
        <div class="skin-name">Поставить монеты</div>
        <div class="skin-type">Баланс: ${{state.balance.toLocaleString('ru-RU')}}</div>
        <div class="skin-price">🪙 Изменить сумму</div>
      `;
      grid.appendChild(coinCard);

      state.inventory.forEach(item => {{
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${{item.uid}}`;
        card.className = `skin-card rare-${{item.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="skin-card-img-wrap">
            <img src="${{item.image}}" alt="${{item.name}}" loading="lazy">
          </div>
          <div class="skin-name">${{item.name}}</div>
          <div class="skin-type">${{item.type}}</div>
          <div class="skin-price">🪙 ${{item.price.toLocaleString('ru-RU')}}</div>
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

      let chance = (sourceVal / targetVal) * 95;
      if (sourceVal >= targetVal) chance = 100;
      if (chance > 92) chance = 92;
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
        showResult(isWin);
      }}, 4100);
    }}

    function showResult(isWin) {{
      const overlay = document.getElementById('resultOverlay');
      const dialog = document.getElementById('resultDialog');
      const title = document.getElementById('resTitle');
      const img = document.getElementById('resImg');
      const name = document.getElementById('resName');
      const price = document.getElementById('resPrice');

      if (isWin) {{
        const wonItem = {{ uid: Date.now(), ...state.selectedTarget }};
        state.inventory.unshift(wonItem);
        dialog.className = 'result-dialog win';
        title.className = 'res-title win';
        title.textContent = '🎉 АПГРЕЙД УДАЛСЯ!';
        img.src = wonItem.image;
        name.textContent = `${{wonItem.type}} | ${{wonItem.name}}`;
        price.textContent = `🪙 +${{wonItem.price.toLocaleString('ru-RU')}}`;
      }} else {{
        dialog.className = 'result-dialog lose';
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

    /* ================= CASE SYSTEM LOGIC ================= */
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
      if (rand < 0.3) chosenRarity = 'gold';
      else if (rand < 1.0) chosenRarity = 'covert';
      else if (rand < 5.0) chosenRarity = 'classified';
      else if (rand < 20.0) chosenRarity = 'restricted';

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
        // Fast multi-open: quick 1.5s spin preview then reveal all 10
        const track = document.getElementById('tapeTrack');
        track.style.transition = 'transform 1.4s cubic-bezier(0.1, 0.9, 0.2, 1)';
        track.style.transform = 'translateX(-2200px)';

        setTimeout(() => {{
          state.isOpeningCase = false;
          document.getElementById('caseModal').style.display = 'none';

          // Roll 10 distinct items
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

          // Display multi-result modal
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
        // 1x Single spin animation
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

          const overlay = document.getElementById('resultOverlay');
          const dialog = document.getElementById('resultDialog');
          const title = document.getElementById('resTitle');
          const img = document.getElementById('resImg');
          const name = document.getElementById('resName');
          const price = document.getElementById('resPrice');

          dialog.className = 'result-dialog win';
          title.className = 'res-title win';
          title.textContent = '🎁 ВЫПАЛ СКИН!';
          img.src = finalWonItem.image;
          name.textContent = `${{finalWonItem.type}} | ${{finalWonItem.name}}`;
          price.textContent = `🪙 +${{finalWonItem.price.toLocaleString('ru-RU')}}`;

          overlay.style.display = 'flex';
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

print("Added 10x case opening button!")
