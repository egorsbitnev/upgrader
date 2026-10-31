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
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="theme-color" content="#0a0d14">
  <title>UPGRADER CS2</title>
  <style>
    :root {{
      --bg-dark: #090c14;
      --bg-surface: #0e1320;
      --bg-panel: #131b2c;
      --bg-card: #182337;
      --bg-card-hover: #1e2c45;
      --neon-cyan: #00f2fe;
      --neon-blue: #4facfe;
      --neon-green: #00e701;
      --neon-green-glow: rgba(0, 231, 1, 0.45);
      --neon-gold: #ffb703;
      --neon-red: #ff2a5f;
      --neon-red-glow: rgba(255, 42, 95, 0.45);
      --text-main: #ffffff;
      --text-dim: #7f8fa4;
      --border: #202c44;
      --safe-top: env(safe-area-inset-top, 0px);
      --safe-bottom: env(safe-area-inset-bottom, 0px);
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
      background: var(--bg-dark);
      color: var(--text-main);
    }}
    body {{
      display: flex;
      flex-direction: column;
      padding-top: var(--safe-top);
      padding-bottom: var(--safe-bottom);
    }}

    /* MOBILE HEADER */
    header {{
      background: #0d121f;
      border-bottom: 1px solid var(--border);
      padding: 8px 12px;
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
      gap: 6px;
    }}
    .brand-icon {{
      width: 26px;
      height: 26px;
      background: linear-gradient(135deg, var(--neon-cyan), var(--neon-blue));
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #080d1a;
      font-weight: 900;
      font-size: 12px;
    }}
    .brand-name {{
      font-size: 15px;
      font-weight: 900;
      letter-spacing: 1px;
      color: #fff;
    }}
    .brand-suffix {{
      font-size: 9px;
      font-weight: 800;
      background: rgba(0, 242, 254, 0.15);
      color: var(--neon-cyan);
      padding: 1px 4px;
      border-radius: 3px;
    }}

    .user-profile {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .balance-pill {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #141c2c;
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 16px;
    }}
    .balance-val {{
      font-weight: 900;
      font-size: 13px;
      color: var(--neon-gold);
    }}
    .btn-deposit {{
      background: linear-gradient(135deg, #00e676, #00c853);
      border: none;
      color: #090e17;
      font-weight: 900;
      font-size: 14px;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    /* MAIN CONTENT VIEWPORT */
    .main-viewport {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    /* UPGRADER VIEW FOR MOBILE */
    #view-upgrader {{
      display: flex;
      flex-direction: column;
      height: 100%;
      overflow: hidden;
    }}

    /* COMPACT ARENA FOR MOBILE PHONES */
    .arena-top {{
      background: radial-gradient(ellipse at 50% 20%, #162035 0%, #0a0e18 100%);
      padding: 8px 10px 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      border-bottom: 1px solid var(--border);
      flex-shrink: 0;
    }}

    .arena-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: 380px;
      gap: 8px;
    }}

    /* MOBILE SLOTS (Left Bet / Right Target) */
    .mobile-slot {{
      flex: 1;
      height: 105px;
      background: var(--bg-panel);
      border: 1.5px dashed var(--border);
      border-radius: 12px;
      padding: 6px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      position: relative;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .mobile-slot.active {{
      border-style: solid;
      border-color: #3b5078;
      background: #162136;
    }}
    .mobile-slot.target.active {{
      border-color: var(--neon-cyan);
      box-shadow: 0 0 14px rgba(0, 242, 254, 0.25);
    }}
    .slot-badge {{
      position: absolute;
      top: 4px;
      font-size: 8.5px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--text-dim);
    }}
    .slot-img-wrap {{
      width: 65px;
      height: 44px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-top: 8px;
    }}
    .slot-img-wrap img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 3px 6px rgba(0,0,0,0.7));
    }}
    .slot-name {{
      font-size: 10.5px;
      font-weight: 700;
      color: #fff;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
      max-width: 105px;
      margin-top: 2px;
    }}
    .slot-price {{
      font-size: 10.5px;
      font-weight: 900;
      color: var(--neon-gold);
    }}

    /* CENTER COMPACT DIAL FOR MOBILE SCREEN */
    .dial-wrap {{
      position: relative;
      width: 130px;
      height: 130px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }}
    .dial-svg {{
      width: 130px;
      height: 130px;
      transform: rotate(-90deg);
    }}
    .dial-bg {{
      fill: transparent;
      stroke: #162136;
      stroke-width: 11;
    }}
    .dial-arc {{
      fill: transparent;
      stroke: var(--neon-green);
      stroke-width: 11;
      stroke-linecap: round;
      stroke-dasharray: 345;
      stroke-dashoffset: 345;
      transition: stroke-dashoffset 0.35s ease;
      filter: drop-shadow(0 0 8px var(--neon-green-glow));
    }}

    .dial-needle {{
      position: absolute;
      top: 50%;
      left: 50%;
      width: 3px;
      height: 62px;
      margin-left: -1.5px;
      margin-top: -62px;
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
      border-left: 6px solid transparent;
      border-right: 6px solid transparent;
      border-top: 13px solid #ffffff;
      filter: drop-shadow(0 0 6px #ffffff);
    }}
    .dial-hub {{
      position: absolute;
      width: 14px;
      height: 14px;
      background: #ffffff;
      border-radius: 50%;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 8px rgba(0, 242, 254, 0.8);
      z-index: 11;
    }}

    .dial-center {{
      position: absolute;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      pointer-events: none;
    }}
    .dial-val {{
      font-size: 21px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1;
      text-shadow: 0 0 10px var(--neon-green-glow);
    }}
    .dial-lbl {{
      font-size: 8px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--text-dim);
      margin-top: 2px;
    }}
    .dial-x {{
      font-size: 11px;
      font-weight: 800;
      color: var(--neon-cyan);
    }}

    /* MOBILE PRESET CHIPS & ACTION BUTTON */
    .arena-actions {{
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      max-width: 380px;
      gap: 6px;
      margin-top: 6px;
    }}
    .presets-carousel {{
      display: flex;
      gap: 5px;
      width: 100%;
      overflow-x: auto;
      scrollbar-width: none;
      padding: 1px 0;
    }}
    .presets-carousel::-webkit-scrollbar {{ display: none; }}
    .preset-pill {{
      flex: 1;
      min-width: 50px;
      background: #141c2c;
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 4px 0;
      font-size: 11px;
      font-weight: 800;
      color: var(--text-dim);
      text-align: center;
      cursor: pointer;
    }}
    .preset-pill:active {{
      background: var(--neon-cyan);
      color: #000;
    }}

    .btn-upgrade-mobile {{
      width: 100%;
      padding: 11px 0;
      background: linear-gradient(135deg, #00e701, #00a801);
      color: #080d15;
      font-size: 14px;
      font-weight: 900;
      letter-spacing: 0.5px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(0, 231, 1, 0.4);
    }}
    .btn-upgrade-mobile:active {{
      transform: scale(0.98);
    }}
    .btn-upgrade-mobile:disabled {{
      background: #1c2639;
      color: #4f617d;
      box-shadow: none;
    }}

    /* MOBILE BOTTOM SKINS COLLECTION */
    .mobile-catalog {{
      flex: 1;
      display: flex;
      flex-direction: column;
      background: var(--bg-surface);
      overflow: hidden;
    }}
    .mobile-tabs-row {{
      display: flex;
      border-bottom: 1px solid var(--border);
      background: #0d121e;
      flex-shrink: 0;
    }}
    .mobile-tab-btn {{
      flex: 1;
      padding: 9px 0;
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--text-dim);
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
    }}
    .mobile-tab-btn.active {{
      color: var(--neon-cyan);
      border-bottom-color: var(--neon-cyan);
      background: rgba(0, 242, 254, 0.05);
    }}

    .mobile-filter-bar {{
      display: flex;
      gap: 5px;
      padding: 5px 8px;
      background: #101625;
      border-bottom: 1px solid var(--border);
      overflow-x: auto;
      scrollbar-width: none;
      flex-shrink: 0;
    }}
    .mobile-filter-bar::-webkit-scrollbar {{ display: none; }}
    .m-filter-chip {{
      padding: 3px 8px;
      font-size: 10px;
      font-weight: 700;
      background: #172134;
      color: var(--text-dim);
      border-radius: 10px;
      border: 1px solid var(--border);
      white-space: nowrap;
      cursor: pointer;
    }}
    .m-filter-chip.active {{
      background: var(--neon-cyan);
      color: #090e18;
      border-color: var(--neon-cyan);
    }}

    .mobile-grid {{
      flex: 1;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      padding: 6px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      align-content: start;
    }}
    @media (min-width: 480px) {{
      .mobile-grid {{
        grid-template-columns: repeat(4, 1fr);
      }}
    }}
    @media (min-width: 768px) {{
      .mobile-grid {{
        grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
      }}
    }}

    .skin-item-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 6px 4px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
      position: relative;
    }}
    .skin-item-card:active {{
      transform: scale(0.95);
    }}
    .skin-item-card.selected {{
      border-color: var(--neon-cyan);
      box-shadow: 0 0 10px rgba(0, 242, 254, 0.35);
      background: #1e2c47;
    }}
    .skin-item-card.rare-contraband {{ border-bottom: 2.5px solid #e4ae39; }}
    .skin-item-card.rare-gold {{ border-bottom: 2.5px solid #ffd700; }}
    .skin-item-card.rare-covert {{ border-bottom: 2.5px solid #eb4b4b; }}
    .skin-item-card.rare-classified {{ border-bottom: 2.5px solid #d32ce6; }}
    .skin-item-card.rare-restricted {{ border-bottom: 2.5px solid #8847ff; }}
    .skin-item-card.rare-milspec {{ border-bottom: 2.5px solid #4b69ff; }}

    .skin-item-card-img {{
      width: 100%;
      height: 48px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 3px;
    }}
    .skin-item-card-img img {{
      max-width: 90%;
      max-height: 90%;
      object-fit: contain;
      filter: drop-shadow(0 2px 4px rgba(0,0,0,0.6));
    }}
    .skin-item-card-name {{
      font-size: 10px;
      font-weight: 700;
      color: #fff;
      line-height: 1.15;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-item-card-type {{
      font-size: 9px;
      color: var(--text-dim);
      margin: 1px 0;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .skin-item-card-price {{
      font-size: 10px;
      font-weight: 900;
      color: var(--neon-gold);
    }}

    /* ================= MOBILE CASES VIEW ================= */
    #view-cases {{
      display: none;
      flex-direction: column;
      height: 100%;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      background: var(--bg-dark);
      padding: 10px 8px;
    }}
    .cases-mobile-grid {{
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 8px;
    }}
    @media (min-width: 500px) {{
      .cases-mobile-grid {{
        grid-template-columns: repeat(3, 1fr);
      }}
    }}
    .case-card-m {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      cursor: pointer;
    }}
    .case-card-m:active {{
      transform: scale(0.96);
    }}
    .case-card-m-img {{
      width: 90px;
      height: 70px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 6px;
    }}
    .case-card-m-img img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
    }}
    .case-card-m-name {{
      font-weight: 800;
      font-size: 11.5px;
      color: #fff;
      margin-bottom: 6px;
      line-height: 1.2;
    }}
    .case-card-m-btn {{
      background: linear-gradient(135deg, #ffb703, #fb8500);
      color: #0b0f19;
      font-weight: 900;
      font-size: 11px;
      padding: 5px 0;
      border-radius: 6px;
      border: none;
      cursor: pointer;
      width: 100%;
      margin-top: auto;
    }}

    /* MOBILE BOTTOM TAB BAR */
    .mobile-bottom-nav {{
      height: 52px;
      background: #0b0e18;
      border-top: 1px solid var(--border);
      display: flex;
      flex-shrink: 0;
      z-index: 90;
    }}
    .m-nav-item {{
      flex: 1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: var(--text-dim);
      font-size: 10px;
      font-weight: 800;
      cursor: pointer;
      gap: 2px;
      transition: color 0.15s;
    }}
    .m-nav-item span {{
      font-size: 17px;
    }}
    .m-nav-item.active {{
      color: var(--neon-cyan);
    }}

    /* CASE OPENING MODAL FOR MOBILE */
    .case-modal {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(6, 9, 15, 0.95);
      backdrop-filter: blur(8px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 12px;
    }}
    .case-modal-box {{
      width: 100%;
      max-width: 360px;
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
    }}
    .case-modal-title {{
      font-size: 16px;
      font-weight: 900;
      color: #fff;
      margin-bottom: 12px;
    }}
    .tape-container {{
      width: 100%;
      height: 96px;
      background: #090c14;
      border: 2px solid var(--border);
      border-radius: 10px;
      position: relative;
      overflow: hidden;
      margin-bottom: 14px;
    }}
    .tape-pointer {{
      position: absolute;
      top: 0; bottom: 0; left: 50%;
      transform: translateX(-50%);
      width: 3px;
      background: #ffb703;
      box-shadow: 0 0 8px #ffb703;
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
      background: #141c2c;
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 4px;
      flex-shrink: 0;
    }}
    .tape-item.rare-gold {{ border-bottom: 2.5px solid #ffd700; }}
    .tape-item.rare-covert {{ border-bottom: 2.5px solid #eb4b4b; }}
    .tape-item.rare-classified {{ border-bottom: 2.5px solid #d32ce6; }}
    .tape-item.rare-restricted {{ border-bottom: 2.5px solid #8847ff; }}
    .tape-item.rare-milspec {{ border-bottom: 2.5px solid #4b69ff; }}
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
    .case-actions-group {{
      display: flex;
      gap: 8px;
      width: 100%;
    }}
    .case-open-btn-m {{
      flex: 1;
      padding: 10px 0;
      border-radius: 10px;
      border: none;
      font-weight: 900;
      font-size: 12px;
      cursor: pointer;
    }}
    .case-open-1x {{
      background: linear-gradient(135deg, #00e701, #00b301);
      color: #0b0f19;
    }}
    .case-open-10x {{
      background: linear-gradient(135deg, #ffb703, #fb8500);
      color: #0b0f19;
    }}
    .case-close-x {{
      position: absolute;
      top: 10px;
      right: 12px;
      color: var(--text-dim);
      font-size: 18px;
      cursor: pointer;
      background: none;
      border: none;
    }}

    /* FULLSCREEN RESULT OVERLAYS FOR MOBILE */
    .animation-overlay {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(6, 9, 16, 0.94);
      backdrop-filter: blur(8px);
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1200;
      padding: 16px;
    }}

    /* WIN POPUP */
    .win-card-box {{
      background: linear-gradient(180deg, #17243c 0%, #101828 100%);
      border: 2px solid var(--neon-green);
      box-shadow: 0 0 35px rgba(0, 231, 1, 0.4);
      border-radius: 18px;
      padding: 20px 16px;
      width: 100%;
      max-width: 310px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      animation: popWin 0.5s cubic-bezier(0.18, 0.89, 0.32, 1.28);
    }}
    @keyframes popWin {{
      0% {{ transform: scale(0.6); opacity: 0; }}
      100% {{ transform: scale(1); opacity: 1; }}
    }}
    .win-badge-title {{
      font-size: 20px;
      font-weight: 900;
      color: var(--neon-green);
      letter-spacing: 0.5px;
    }}
    .win-skin-img-box {{
      width: 140px;
      height: 90px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 10px 0;
    }}
    .win-skin-img-box img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      filter: drop-shadow(0 6px 14px rgba(0, 231, 1, 0.6));
    }}
    .win-item-name {{
      font-size: 15px;
      font-weight: 800;
      color: #ffffff;
    }}
    .win-item-price {{
      font-size: 15px;
      font-weight: 900;
      color: var(--neon-gold);
      margin-top: 3px;
    }}
    .btn-action-dialog {{
      margin-top: 16px;
      width: 100%;
      padding: 12px;
      background: linear-gradient(135deg, #00e701, #00b301);
      border: none;
      border-radius: 10px;
      color: #080d16;
      font-size: 14px;
      font-weight: 900;
      cursor: pointer;
    }}

    /* LOSE POPUP */
    .lose-card-box {{
      background: linear-gradient(180deg, #24141c 0%, #130a0f 100%);
      border: 2px solid var(--neon-red);
      box-shadow: 0 0 35px rgba(255, 42, 95, 0.4);
      border-radius: 18px;
      padding: 20px 16px;
      width: 100%;
      max-width: 300px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      animation: shakeLose 0.6s ease;
    }}
    @keyframes shakeLose {{
      20%, 80% {{ transform: translate3d(-4px, 0, 0); }}
      40%, 60% {{ transform: translate3d(4px, 0, 0); }}
    }}
    .lose-badge-title {{
      font-size: 19px;
      font-weight: 900;
      color: var(--neon-red);
    }}
    .btn-retry-lose {{
      margin-top: 14px;
      width: 100%;
      padding: 11px;
      background: #331d27;
      border: 1px solid #66273c;
      border-radius: 10px;
      color: #fff;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
    }}

    /* 10X CASE MULTI RESULT */
    .multi-res-dialog {{
      background: var(--bg-panel);
      border: 2px solid var(--neon-gold);
      border-radius: 16px;
      padding: 14px;
      width: 100%;
      max-width: 360px;
      max-height: 85vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .multi-res-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 6px;
      width: 100%;
      overflow-y: auto;
      max-height: 55vh;
      padding: 4px 0;
    }}
    .multi-res-card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 5px 3px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }}
    .multi-res-card.rare-gold {{ border-bottom: 2px solid #ffd700; }}
    .multi-res-card.rare-covert {{ border-bottom: 2.5px solid #eb4b4b; }}
    .multi-res-card.rare-classified {{ border-bottom: 2.5px solid #d32ce6; }}
    .multi-res-card.rare-restricted {{ border-bottom: 2.5px solid #8847ff; }}
    .multi-res-card.rare-milspec {{ border-bottom: 2.5px solid #4b69ff; }}
    .multi-res-card img {{
      width: 44px;
      height: 34px;
      object-fit: contain;
    }}
    .multi-res-card-name {{
      font-size: 9px;
      font-weight: 700;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      width: 100%;
    }}
    .multi-res-card-price {{
      font-size: 9px;
      font-weight: 900;
      color: var(--neon-gold);
    }}

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

  <!-- MOBILE HEADER -->
  <header>
    <div class="brand-wrap">
      <div class="brand-icon">UP</div>
      <div class="brand-name">UPGRADER</div>
      <div class="brand-suffix">CS2</div>
    </div>
    <div class="user-profile">
      <div class="balance-pill">
        <span style="font-size: 13px;">🪙</span>
        <span class="balance-val" id="userBalanceDisplay">1,000</span>
      </div>
      <button class="btn-deposit" title="Пополнить бесплатно (+1,000)" onclick="grantFreeCoins()">+</button>
    </div>
  </header>

  <!-- VIEWPORT -->
  <div class="main-viewport">

    <!-- ================= VIEW 1: UPGRADER ================= -->
    <div id="view-upgrader">
      
      <!-- COMPACT ARENA -->
      <div class="arena-top">
        <div class="arena-row">
          
          <!-- Left: User Bet Slot -->
          <div class="mobile-slot active" id="sourceSlot" onclick="switchMobileTab('inventory')">
            <span class="slot-badge">Ставка</span>
            <div class="slot-img-wrap" id="sourceImgBox">
              <span style="font-size: 26px;">🪙</span>
            </div>
            <div class="slot-name" id="sourceTitle">100 Монет</div>
            <div class="slot-price" id="sourcePrice">🪙 100</div>
          </div>

          <!-- Center: Dial Wheel -->
          <div class="dial-wrap">
            <svg class="dial-svg">
              <circle class="dial-bg" cx="65" cy="65" r="55"></circle>
              <circle class="dial-arc" id="winArc" cx="65" cy="65" r="55"></circle>
            </svg>

            <div class="dial-needle" id="needle"></div>
            <div class="dial-hub"></div>

            <div class="dial-center">
              <span class="dial-val" id="chanceDisplay">0%</span>
              <span class="dial-lbl">Шанс</span>
              <span class="dial-x" id="multDisplay">x0.00</span>
            </div>
          </div>

          <!-- Right: Target Slot -->
          <div class="mobile-slot target" id="targetSlot" onclick="switchMobileTab('market')">
            <span class="slot-badge">Цель</span>
            <div class="slot-img-wrap" id="targetImgBox">
              <span style="font-size: 24px;">🎯</span>
            </div>
            <div class="slot-name" id="targetTitle">Выберите</div>
            <div class="slot-price" id="targetPrice">-</div>
          </div>

        </div>

        <!-- Presets & Action Button -->
        <div class="arena-actions">
          <div class="presets-carousel">
            <div class="preset-pill" onclick="applyMultiplierTarget(1.5)">1.5x</div>
            <div class="preset-pill" onclick="applyMultiplierTarget(2)">2x</div>
            <div class="preset-pill" onclick="applyMultiplierTarget(5)">5x</div>
            <div class="preset-pill" onclick="applyMultiplierTarget(10)">10x</div>
            <div class="preset-pill" onclick="applyMultiplierTarget(25)">25x</div>
            <div class="preset-pill" onclick="applyMultiplierTarget(50)">50x</div>
          </div>

          <button class="btn-upgrade-mobile" id="upgradeBtn" disabled onclick="startUpgrade()">
            СДЕЛАТЬ АПГРЕЙД
          </button>
        </div>
      </div>

      <!-- MOBILE CATALOG SECTION -->
      <div class="mobile-catalog">
        <div class="mobile-tabs-row">
          <button class="mobile-tab-btn active" id="tabMarketBtn" onclick="switchMobileTab('market')">Магазин (<span id="marketCount">0</span>)</button>
          <button class="mobile-tab-btn" id="tabInventoryBtn" onclick="switchMobileTab('inventory')">Инвентарь (<span id="invCount">0</span>)</button>
        </div>

        <div class="mobile-filter-bar" id="marketFilterBar">
          <div class="m-filter-chip active" onclick="filterMarket('all', this)">Все</div>
          <div class="m-filter-chip" onclick="filterMarket('knife', this)">Ножи / Перчатки</div>
          <div class="m-filter-chip" onclick="filterMarket('rifle', this)">Винтовки</div>
          <div class="m-filter-chip" onclick="filterMarket('pistol', this)">Пистолеты</div>
          <div class="m-filter-chip" onclick="filterMarket('cheap', this)">До 1,000</div>
          <div class="m-filter-chip" onclick="filterMarket('expensive', this)">10,000+</div>
        </div>

        <div class="mobile-grid" id="marketGrid"></div>
        <div class="mobile-grid" id="inventoryGrid" style="display: none;"></div>
      </div>

    </div>

    <!-- ================= VIEW 2: CASES ================= -->
    <div id="view-cases">
      <div class="cases-mobile-grid" id="casesGrid"></div>
    </div>

  </div>

  <!-- MOBILE BOTTOM BAR NAVIGATION -->
  <div class="mobile-bottom-nav">
    <div class="m-nav-item active" id="navItemUpgrader" onclick="switchMainView('upgrader')">
      <span>⚡</span>
      <div>Апгрейдер</div>
    </div>
    <div class="m-nav-item" id="navItemCases" onclick="switchMainView('cases')">
      <span>📦</span>
      <div>Кейсы CS2</div>
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
        <button class="case-open-btn-m case-open-1x" id="caseOpen1xBtn" onclick="spinCase(1)">
          1x 🪙 250
        </button>
        <button class="case-open-btn-m case-open-10x" id="caseOpen10xBtn" onclick="spinCase(10)">
          ⚡ 10x 🪙 2,500
        </button>
      </div>
    </div>
  </div>

  <!-- WIN ANIMATION MODAL -->
  <div class="animation-overlay" id="winOverlay">
    <canvas id="confettiCanvas"></canvas>
    <div class="win-card-box">
      <div class="win-badge-title">🎉 ПОБЕДА!</div>
      <div class="win-skin-img-box">
        <img id="winSkinImg" src="" alt="Skin">
      </div>
      <div class="win-item-name" id="winSkinName">AK-47 | Вулкан</div>
      <div class="win-item-price" id="winSkinPrice">🪙 +2,800</div>
      <button class="btn-action-dialog" onclick="closeWinOverlay()">ЗАБРАТЬ</button>
    </div>
  </div>

  <!-- LOSE ANIMATION MODAL -->
  <div class="animation-overlay" id="loseOverlay">
    <div class="lose-card-box">
      <div style="font-size: 42px; margin-bottom: 6px;">💥</div>
      <div class="lose-badge-title">НЕУДАЧА</div>
      <div style="font-size: 12px; color: #b97f8c; margin-top: 4px;">Скин сгорел в апгрейде</div>
      <button class="btn-retry-lose" onclick="closeLoseOverlay()">ЕЩЕ РАЗ</button>
    </div>
  </div>

  <!-- 10X CASE MULTI RESULT MODAL -->
  <div class="animation-overlay" id="multiResultOverlay">
    <div class="multi-res-dialog">
      <div style="display: flex; justify-content: space-between; width: 100%; margin-bottom: 8px;">
        <span style="font-weight: 900; font-size: 14px;">🎁 ДРОП ИЗ 10 КЕЙСОВ</span>
        <span style="font-weight: 900; font-size: 13px; color: var(--neon-gold);" id="multiResTotal">+🪙 0</span>
      </div>
      <div class="multi-res-grid" id="multiResGrid"></div>
      <button class="btn-action-dialog" style="margin-top: 10px;" onclick="closeMultiResult()">ЗАБРАТЬ ВСЕ</button>
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

    const CIRCLE_CIRCUMFERENCE = 2 * Math.PI * 55; // ~345.5px

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

    function switchMobileTab(tab) {{
      document.getElementById('tabMarketBtn').classList.toggle('active', tab === 'market');
      document.getElementById('tabInventoryBtn').classList.toggle('active', tab === 'inventory');
      document.getElementById('marketGrid').style.display = tab === 'market' ? 'grid' : 'none';
      document.getElementById('marketFilterBar').style.display = tab === 'market' ? 'flex' : 'none';
      document.getElementById('inventoryGrid').style.display = tab === 'inventory' ? 'grid' : 'none';
    }}

    function filterMarket(filter, el) {{
      state.currentFilter = filter;
      document.querySelectorAll('.m-filter-chip').forEach(c => c.classList.remove('active'));
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

      document.querySelectorAll('#marketGrid .skin-item-card').forEach(c => c.classList.remove('selected'));
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

      document.querySelectorAll('#inventoryGrid .skin-item-card').forEach(c => c.classList.remove('selected'));
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

      document.querySelectorAll('#inventoryGrid .skin-item-card').forEach(c => c.classList.remove('selected'));
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
        card.className = `skin-item-card rare-${{skin.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectTarget(skin);
        card.innerHTML = `
          <div class="skin-item-card-img">
            <img src="${{skin.image}}" alt="${{skin.name}}" loading="lazy">
          </div>
          <div class="skin-item-card-name">${{skin.name}}</div>
          <div class="skin-item-card-type">${{skin.type}}</div>
          <div class="skin-item-card-price">🪙 ${{skin.price.toLocaleString('ru-RU')}}</div>
        `;
        grid.appendChild(card);
      }});
    }}

    function renderInventory() {{
      const grid = document.getElementById('inventoryGrid');
      grid.innerHTML = '';

      const coinCard = document.createElement('div');
      coinCard.className = `skin-item-card`;
      coinCard.style.borderColor = 'var(--neon-gold)';
      coinCard.onclick = () => {{
        const val = prompt("Введите сумму ставки монет:", state.coinBet || "100");
        const num = parseInt(val, 10);
        if (num && num > 0) selectCoinBet(num);
      }};
      coinCard.innerHTML = `
        <div class="skin-item-card-img">
          <span style="font-size: 26px;">🪙</span>
        </div>
        <div class="skin-item-card-name">Монеты</div>
        <div class="skin-item-card-type">Ставка</div>
        <div class="skin-item-card-price">Изменить</div>
      `;
      grid.appendChild(coinCard);

      state.inventory.forEach(item => {{
        const isSelected = state.selectedSource && state.selectedSource.uid === item.uid;
        const card = document.createElement('div');
        card.id = `inv-card-${{item.uid}}`;
        card.className = `skin-item-card rare-${{item.rarity}} ${{isSelected ? 'selected' : ''}}`;
        card.onclick = () => selectSourceItem(item);
        card.innerHTML = `
          <div class="skin-item-card-img">
            <img src="${{item.image}}" alt="${{item.name}}" loading="lazy">
          </div>
          <div class="skin-item-card-name">${{item.name}}</div>
          <div class="skin-item-card-type">${{item.type}}</div>
          <div class="skin-item-card-price">🪙 ${{item.price.toLocaleString('ru-RU')}}</div>
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

    let confettiAnimation = null;
    function triggerConfetti() {{
      const canvas = document.getElementById('confettiCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#00e701', '#00f2fe', '#ffb703', '#ffffff', '#4facfe'];

      for (let i = 0; i < 60; i++) {{
        particles.push({{
          x: canvas.width / 2,
          y: canvas.height / 2,
          vx: (Math.random() - 0.5) * 14,
          vy: (Math.random() - 0.8) * 16,
          size: Math.random() * 6 + 3,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 8
        }});
      }}

      function render() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {{
          p.x += p.vx;
          p.y += p.vy;
          p.vy += 0.35;
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
        card.className = 'case-card-m';
        card.onclick = () => openCaseModal(c);
        card.innerHTML = `
          <div class="case-card-m-img">
            <img src="${{c.image}}" alt="${{c.name}}" loading="lazy">
          </div>
          <div class="case-card-m-name">${{c.name}}</div>
          <button class="case-card-m-btn">🪙 ${{c.price.toLocaleString('ru-RU')}}</button>
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
        track.style.transform = 'translateX(-1800px)';

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
          totalEl.textContent = `+🪙 ${{totalValue.toLocaleString('ru-RU')}}`;

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

        const itemWidth = 90;
        const containerWidth = document.querySelector('.tape-container').offsetWidth;
        const jitter = (Math.random() * 40) - 20;
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

print("Updated index.html with 100% mobile-optimized layout!")
