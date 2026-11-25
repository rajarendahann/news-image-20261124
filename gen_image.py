import os
from PIL import Image, ImageDraw, ImageFont

def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = []
    for word in words:
        test_line = " ".join(current_line + [word])
        if draw.textlength(test_line, font=font) <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(" ".join(current_line))
            current_line = [word]
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_image(output_path="entry.png"):
    width, height = 1024, 1024
    img = Image.new("RGB", (width, height), color="#FDFBF7")
    draw = ImageDraw.Draw(img)

    # Fonts (DejaVu)
    sans_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    sans_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    serif_bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    serif_path = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

    font_masthead = ImageFont.truetype(serif_bold_path, 52)
    font_subhead = ImageFont.truetype(sans_bold_path, 12)
    font_section = ImageFont.truetype(sans_bold_path, 12)
    font_big_title = ImageFont.truetype(sans_bold_path, 18)
    font_big_body = ImageFont.truetype(sans_path, 13)
    font_med_title = ImageFont.truetype(sans_bold_path, 13)
    font_med_body = ImageFont.truetype(sans_path, 12)
    font_small = ImageFont.truetype(sans_path, 12)
    font_tiny = ImageFont.truetype(sans_path, 11)

    margin = 20
    y = 16

    # 1. Top bar
    draw.text((margin, y), "THE WORLD IN ONE DAY  •  TUESDAY, 24 NOVEMBER 2026  •  EDITION NO. 328", fill="#444444", font=font_subhead)
    y += 20
    draw.line([(margin, y), (width - margin, y)], fill="#222222", width=2)
    y += 10

    # 2. Huge Masthead Title
    title_text = "THE DAILY CHRONICLE"
    draw.text((margin, y), title_text, fill="#111111", font=font_masthead)
    y += 58

    # Lede line naming three biggest stories
    lede = "NVIDIA BOARD REINSTATES HUANG AS CEO  •  IRGC SAYS TANKERS HIT MINES IN HORMUZ  •  MASSIVE AIRSTRIKE ACROSS UKRAINE"
    draw.text((margin, y), lede, fill="#555555", font=font_small)
    y += 18
    draw.line([(margin, y), (width - margin, y)], fill="#888888", width=1)
    y += 8

    # 3. Region counter row (7 regions)
    stats = [
        ("ASIA", "3"),
        ("MIDDLE EAST", "4"),
        ("EUROPE", "4"),
        ("AFRICA", "3"),
        ("AMERICAS", "4"),
        ("OCEANIA", "1"),
        ("GLOBAL", "3")
    ]
    box_w = (width - 2 * margin - 6 * 8) / 7
    bx = margin
    for reg, count in stats:
        draw.rectangle([bx, y, bx + box_w, y + 26], outline="#CCCCCC", fill="#F4F1EA")
        text_str = f"{reg} ({count})"
        tw = draw.textlength(text_str, font=font_tiny)
        draw.text((bx + (box_w - tw) / 2, y + 6), text_str, fill="#333333", font=font_tiny)
        bx += box_w + 8
    y += 34

    # 4. Three Big Story Cards (height 150)
    big_stories = [
        ("GLOBAL", "#2C3E50", "Nvidia Reinstates Jensen Huang as CEO", "President Trump personally intervened to bring back Huang following security consultations.", "Share price surges as chipmaker resolves leadership crisis and reassures global markets."),
        ("MIDDLE EAST", "#8E44AD", "Tankers Hit Naval Mines in Strait of Hormuz", "IRGC Navy says four oil tankers struck mines and caught fire despite US military air escort.", "Tehran warns vessels against unauthorized routes; oil prices jump as traffic falls 40%."),
        ("EUROPE", "#2980B9", "Rosstat Leak Reveals Huge Russian Casualties", "Data extracted from statistics agency indicates at least 490,000 soldiers killed in Ukraine.", "The figure comes from death certificates; Kremlin has not commented on the massive data breach.")
    ]
    
    card_w = (width - 2 * margin - 2 * 12) / 3
    card_h = 135
    cx = margin
    for tag, color, headline, line1, line2 in big_stories:
        draw.rectangle([cx, y, cx + card_w, y + card_h], outline="#B0A899", fill="#FFFFFF", width=1)
        draw.rectangle([cx, y, cx + card_w, y + 20], fill=color)
        draw.text((cx + 8, y + 3), tag, fill="#FFFFFF", font=font_section)
        
        hy = y + 24
        for h_line in wrap_text(headline, font_big_title, card_w - 16, draw):
            draw.text((cx + 8, hy), h_line, fill="#111111", font=font_big_title)
            hy += 18
        
        hy += 1
        body_text = f"{line1} {line2}"
        for b_line in wrap_text(body_text, font_big_body, card_w - 16, draw):
            draw.text((cx + 8, hy), b_line, fill="#333333", font=font_big_body)
            hy += 14
            
        cx += card_w + 12
    y += card_h + 8

    # 5. 3x4 Grid of Medium Cards (height 65)
    med_stories = [
        ("AMERICAS", "#C0392B", "Colombia Car Bomb Injustice", "At least 24 injured in Villavicencio blast targeting government buildings and local businesses."),
        ("ASIA", "#D35400", "Huawei Trade Secret Verdict", "Tech giant found guilty of stealing trade secrets in US court but acquitted of racketeering."),
        ("EUROPE", "#2980B9", "PM Burnham Rules Out EU Return", "UK leader says rejoining EU is 'unthinkable' without a new referendum; calls critics stuck in past."),
        ("AFRICA", "#27AE60", "Russians Killed in Mali Conflict", "Leaked data reveals over 300 Russians killed supporting Mali's junta against regional insurgents."),
        ("AMERICAS", "#C0392B", "Canada Rejects US Defense Memo", "Ottawa says it 'does not report to the US' after Pentagon memo criticized military spending."),
        ("OCEANIA", "#16A085", "Island Dispute at UN Court", "France and Vanuatu face off over sovereignty of Matthew and Hunter islands in the Pacific."),
        ("GLOBAL", "#2C3E50", "2031 Women's World Cup Hosts", "FIFA awards tournament to US, Mexico, Costa Rica and Jamaica; UK to host in 2035."),
        ("ASIA", "#D35400", "Candy Factory Blaze Kills 24", "Fire in Indonesia's Banten province leaves dozens missing; electrical short circuit suspected."),
        ("EUROPE", "#2980B9", "UK Environment Agencies Axed", "Government proposes abolishing Natural England and Environment Agency in deregulation push."),
        ("GLOBAL", "#2C3E50", "Gavi Plans 1.5M Ebola Doses", "Alliance eyes major vaccine purchase for Congo's Bundibugyo outbreak if trials are effective."),
        ("EUROPE", "#2980B9", "Germany School Bomb Threats", "Hundreds of schools across Germany evacuated following a coordinated wave of bomb threats."),
        ("MIDDLE EAST", "#8E44AD", "Israeli Drone Strike in Gaza", "Strike reportedly kills three at a Gaza police post; regional tensions remain at record highs.")
    ]

    grid_cols = 3
    g_w = (width - 2 * margin - 2 * 12) / 3
    g_h = 58
    
    gx_start = margin
    gy_start = y
    
    for i, (tag, color, title, desc) in enumerate(med_stories):
        r = i // grid_cols
        c = i % grid_cols
        gx = gx_start + c * (g_w + 12)
        gy = gy_start + r * (g_h + 4)
        
        draw.rectangle([gx, gy, gx + g_w, gy + g_h], outline="#D0C8B8", fill="#FFFFFF")
        draw.rectangle([gx, gy, gx + g_w, gy + 15], fill=color)
        draw.text((gx + 6, gy + 1), tag, fill="#FFFFFF", font=font_tiny)
        
        draw.text((gx + 6, gy + 17), title, fill="#111111", font=font_med_title)
        
        d_y = gy + 31
        for d_line in wrap_text(desc, font_med_body, g_w - 12, draw)[:2]:
            draw.text((gx + 6, d_y), d_line, fill="#444444", font=font_med_body)
            d_y += 12
        
    y += 4 * (g_h + 4) + 4
    draw.line([(margin, y), (width - margin, y)], fill="#CCCCCC", width=1)
    y += 6

    # NEW: 3x3 'MORE FROM THE DAY' grid
    draw.text((margin, y), "MORE FROM THE DAY", fill="#111111", font=font_section)
    y += 18

    more_stories = [
        ("AMERICAS", "#C0392B", "Cuba Life Expectancy Falls", "Economic crisis and fuel blockades drive life expectancy down to 74.4 years, WHO reports."),
        ("ASIA", "#D35400", "China Official Sentenced", "Former official sentenced to death for spying and leaking state secrets to foreign agencies."),
        ("GLOBAL", "#2C3E50", "UN Warns of AI Power Risk", "Secretary-General warns artificial intelligence risks becoming more powerful than human control."),
        ("AMERICAS", "#C0392B", "Thanksgiving Travel Surge", "AAA projects 81.5 million travelers as airfares jump; storm threatens East Coast routes."),
        ("ASIA", "#D35400", "South Korea Scrambles Jets", "Fighters sent after Russian military aircraft enter air defense identification zone."),
        ("EUROPE", "#2980B9", "Arctic Security Talks", "Norway and Ukraine discuss stability in northern near-areas as regional tensions simmer."),
        ("GLOBAL", "#2C3E50", "LaLiga Fan Data Cyberattack", "Major breach exposes personal data of registered fans; cybersecurity firm investigating."),
        ("AFRICA", "#27AE60", "Zambia Opposition Indicted", "Opposition leader Mundubile formally indicted on treason charges; supporters cry foul."),
        ("EUROPE", "#2980B9", "Ukraine Aid Warning", "Economist warns Europe that funding defense is cheaper than dealing with a Russian win.")
    ]

    gy_start = y
    for i, (tag, color, title, desc) in enumerate(more_stories):
        r = i // grid_cols
        c = i % grid_cols
        gx = gx_start + c * (g_w + 12)
        gy = gy_start + r * (g_h + 4)
        
        draw.rectangle([gx, gy, gx + g_w, gy + g_h], outline="#D0C8B8", fill="#FFFFFF")
        draw.rectangle([gx, gy, gx + g_w, gy + 15], fill=color)
        draw.text((gx + 6, gy + 1), tag, fill="#FFFFFF", font=font_tiny)
        
        draw.text((gx + 6, gy + 17), title, fill="#111111", font=font_med_title)
        
        d_y = gy + 31
        for d_line in wrap_text(desc, font_med_body, g_w - 12, draw)[:2]:
            draw.text((gx + 6, d_y), d_line, fill="#444444", font=font_med_body)
            d_y += 12

    y += 3 * (g_h + 4) + 6
    draw.line([(margin, y), (width - margin, y)], fill="#888888", width=1)
    y += 8

    # 6. Bottom Section: Map on left, Also on this day on right (Height = 160)
    bottom_h = 160
    half_w = (width - 2 * margin - 12) / 2
    
    # Left: Where it happened
    map_x = margin
    draw.rectangle([map_x, y, map_x + half_w, y + bottom_h], outline="#CCCCCC", fill="#F4F1EA")
    draw.rectangle([map_x, y, map_x + half_w, y + 22], fill="#333333")
    draw.text((map_x + 8, y + 4), "WHERE IT HAPPENED", fill="#FFFFFF", font=font_section)
    
    for gx_line in range(int(map_x + 20), int(map_x + half_w), 40):
        draw.line([(gx_line, y + 26), (gx_line, y + bottom_h - 6)], fill="#E0DCD4", width=1)
    for gy_line in range(int(y + 35), int(y + bottom_h), 30):
        draw.line([(map_x + 10, gy_line), (map_x + half_w - 10, gy_line)], fill="#E0DCD4", width=1)

    dots = [
        ("Washington", 45, 50, -35, 2),
        ("Ottawa", 60, 35, 8, -6),
        ("Villavicencio", 75, 110, 8, 2),
        ("London", 165, 45, -35, -12),
        ("Brussels", 185, 42, 6, -12),
        ("Kyiv", 220, 52, 8, 4),
        ("Moscow", 255, 38, 8, -12),
        ("Hormuz", 280, 100, 8, -10),
        ("Mali", 160, 120, 10, -4),
        ("Jakarta", 360, 135, 10, 4),
        ("Shenzhen", 370, 85, 10, 2),
        ("Seoul", 400, 65, 8, -14),
        ("Vanuatu", 450, 130, -35, 8),
    ]

    for city, cx_off, cy_off, lx_off, ly_off in dots:
        px = map_x + cx_off
        py = y + cy_off
        draw.ellipse([px-3, py-3, px+3, py+3], fill="#C0392B", outline="#000000")
        draw.text((px + lx_off, py + ly_off), city, fill="#222222", font=font_tiny)

    # Right: ALSO ON TUESDAY 24 NOVEMBER 2026
    right_x = map_x + half_w + 12
    draw.rectangle([right_x, y, width - margin, y + bottom_h], outline="#CCCCCC", fill="#FFFFFF")
    draw.rectangle([right_x, y, width - margin, y + 22], fill="#333333")
    draw.text((right_x + 8, y + 4), "ALSO ON TUESDAY 24 NOVEMBER 2026", fill="#FFFFFF", font=font_section)

    also_items = [
        "[EUR] Ukraine and Norway sign northern stability pact",
        "[MDE] US Treasury expands sanctions on Iranian banks",
        "[AFR] Rhino poaching spike in South Africa parks",
        "[AMS] Brazil supreme court maintains ban on platform X",
        "[ASI] Thailand arrests human trafficking ringleader",
        "[GLO] Global shipping rates spike after Hormuz incidents",
        "[EUR] Polish miners protest over coal phase-out plan",
        "[AMS] US court allows lead azide detonation at plant",
        "[ASI] Japan reports record-low birth rate for 2026",
        "[AFR] Sudan's RSF and SAF clash near El Fasher",
        "[GLO] WHO warns of rising respiratory virus cases",
        "[EUR] Italy passes Security Decree on migrant NGOs"
    ]

    item_y = y + 26
    for item in also_items:
        draw.text((right_x + 8, item_y), item, fill="#333333", font=font_tiny)
        item_y += 11

    y += bottom_h + 8
    draw.line([(margin, y), (width - margin, y)], fill="#222222", width=1)
    y += 6

    # 7. Footer
    footer1 = "DATE CHECK: Every story on this page happened, or was first reported, on Tuesday 24 November 2026."
    footer2 = "Sources: Reuters, AP, AFP, BBC, Al Jazeera, Euronews, NPR, Kyiv Independent, El Pais, AllAfrica, ABC. Errors are not intentional."
    footer3 = "Stories are attributed, not stated as facts. Numbers are approximate."
    
    draw.text((margin, y), footer1, fill="#555555", font=font_tiny)
    y += 12
    draw.text((margin, y), footer2, fill="#555555", font=font_tiny)
    y += 12
    draw.text((margin, y), footer3, fill="#555555", font=font_tiny)


    # Save output
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    generate_image()
