import os

def build_refined_logos():
    # 1. Favicon SVG (Squircle with glowing amber emblem)
    favicon_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <!-- Background Dark Gradient -->
    <radialGradient id="bgGlow" cx="50%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#1A1E25" />
      <stop offset="70%" stop-color="#0F1216" />
      <stop offset="100%" stop-color="#08090B" />
    </radialGradient>

    <!-- Glowing Amber Border -->
    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFC87C" stop-opacity="0.85" />
      <stop offset="50%" stop-color="#FFB454" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#FF7A00" stop-opacity="0.75" />
    </linearGradient>

    <!-- Amber Ribbon Gradient -->
    <linearGradient id="amberRibbon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0" />
      <stop offset="35%" stop-color="#FFB454" />
      <stop offset="80%" stop-color="#FF7A00" />
      <stop offset="100%" stop-color="#E65100" />
    </linearGradient>

    <linearGradient id="bridgeGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFE0B2" />
      <stop offset="100%" stop-color="#FFB454" />
    </linearGradient>

    <filter id="markShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.7"/>
    </filter>
  </defs>

  <!-- Squircle Base -->
  <rect x="24" y="24" width="464" height="464" rx="116" fill="url(#bgGlow)" stroke="url(#borderGrad)" stroke-width="8" />

  <!-- Ambient Backlight -->
  <circle cx="256" cy="256" r="140" fill="#FFB454" opacity="0.09" filter="blur(30px)" />

  <!-- Monogram Mark -->
  <g filter="url(#markShadow)">
    <path d="M 336 186
             L 336 160
             C 336 128, 308 100, 274 100
             L 230 100
             C 192 100, 160 132, 160 170
             C 160 208, 190 238, 228 250
             L 284 268
             C 322 280, 352 310, 352 350
             C 352 388, 320 420, 282 420
             L 238 420
             C 204 420, 176 392, 176 360
             L 176 334"
          fill="none"
          stroke="url(#amberRibbon)"
          stroke-width="48"
          stroke-linecap="round"
          stroke-linejoin="round" />

    <path d="M 218 247 L 294 271"
          stroke="url(#bridgeGrad)"
          stroke-width="18"
          stroke-linecap="round" />

    <circle cx="336" cy="186" r="12" fill="#FFF3E0" />
    <circle cx="176" cy="334" r="12" fill="#E65100" />
  </g>
</svg>'''

    # 2. Standalone Vector Icon Mark (No Squircle Box)
    logo_mark_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <defs>
    <linearGradient id="amberRibbonMark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0" />
      <stop offset="35%" stop-color="#FFB454" />
      <stop offset="80%" stop-color="#FF7A00" />
      <stop offset="100%" stop-color="#E65100" />
    </linearGradient>

    <linearGradient id="bridgeGradMark" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFE0B2" />
      <stop offset="100%" stop-color="#FFB454" />
    </linearGradient>

    <filter id="markGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#FFB454" flood-opacity="0.3"/>
    </filter>
  </defs>

  <g filter="url(#markGlow)">
    <path d="M 336 186
             L 336 160
             C 336 128, 308 100, 274 100
             L 230 100
             C 192 100, 160 132, 160 170
             C 160 208, 190 238, 228 250
             L 284 268
             C 322 280, 352 310, 352 350
             C 352 388, 320 420, 282 420
             L 238 420
             C 204 420, 176 392, 176 360
             L 176 334"
          fill="none"
          stroke="url(#amberRibbonMark)"
          stroke-width="48"
          stroke-linecap="round"
          stroke-linejoin="round" />

    <path d="M 218 247 L 294 271"
          stroke="url(#bridgeGradMark)"
          stroke-width="18"
          stroke-linecap="round" />

    <circle cx="336" cy="186" r="12" fill="#FFF3E0" />
    <circle cx="176" cy="334" r="12" fill="#E65100" />
  </g>
</svg>'''

    # 3. Full Logo SVG (Icon Box + Typography)
    full_logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGlowH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1A1E24" />
      <stop offset="100%" stop-color="#08090B" />
    </linearGradient>
    <linearGradient id="borderGradH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFC87C" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#FF7A00" stop-opacity="0.3" />
    </linearGradient>
    <linearGradient id="topRibbonH" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3E0" />
      <stop offset="40%" stop-color="#FFB454" />
      <stop offset="100%" stop-color="#FF7A00" />
    </linearGradient>
  </defs>

  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="100" height="100" rx="24" fill="url(#bgGlowH)" stroke="url(#borderGradH)" stroke-width="3" />
    
    <g transform="translate(14, 14) scale(0.14)">
      <path d="M 336 186
               L 336 160
               C 336 128, 308 100, 274 100
               L 230 100
               C 192 100, 160 132, 160 170
               C 160 208, 190 238, 228 250
               L 284 268
               C 322 280, 352 310, 352 350
               C 352 388, 320 420, 282 420
               L 238 420
               C 204 420, 176 392, 176 360
               L 176 334"
            fill="none"
            stroke="url(#topRibbonH)"
            stroke-width="48"
            stroke-linecap="round"
            stroke-linejoin="round" />
      <path d="M 218 247 L 294 271" stroke="#FFF3E0" stroke-width="18" stroke-linecap="round" />
      <circle cx="336" cy="186" r="12" fill="#FFF3E0" />
      <circle cx="176" cy="334" r="12" fill="#E65100" />
    </g>

    <text x="124" y="58" font-family="'Oswald', sans-serif" font-size="44" font-weight="700" letter-spacing="3" fill="#FFB454">SSARI <tspan fill="#F3F4F6">INC</tspan></text>
    <text x="126" y="84" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="500" letter-spacing="4" fill="#7A828C">SOFTWARE &amp; PRODUCTS</text>
  </g>
</svg>'''

    with open('favicon.svg', 'w') as f:
        f.write(favicon_svg)
    with open('logo-mark.svg', 'w') as f:
        f.write(logo_mark_svg)
    with open('logo.svg', 'w') as f:
        f.write(full_logo_svg)

if __name__ == '__main__':
    build_refined_logos()
