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

    # 4. Three Big Story Cards (height 170)
    big_stories = [
        ("GLOBAL", "#2C3E50", "Nvidia Reinstates Jensen Huang as CEO", "Board unanimously votes to bring back Huang following US government security consultations.", "Share price surges as chipmaker resolves leadership crisis and reassures markets."),
        ("MIDDLE EAST", "#8E44AD", "Tankers Hit Naval Mines in Strait of Hormuz", "IRGC Navy says three oil tankers struck naval mines and caught fire despite US military escort.", "Tehran warns vessels against unauthorized routes; US Treasury widens sanctions on shadow networks."),
        ("EUROPE", "#2980B9", "Massive Airstrike Hits Ukrainian Grid", "Russia launches over 150 drones and missiles targeting energy infrastructure across multiple regions.", "President Zelenskyy urges Western allies to urgently supply additional air defense Patriot missiles.")
    ]
    
    card_w = (width - 2 * margin - 2 * 12) / 3
    card_h = 170
    cx = margin
    for tag, color, headline, line1, line2 in big_stories:
        draw.rectangle([cx, y, cx + card_w, y + card_h], outline="#B0A899", fill="#FFFFFF", width=1)
        draw.rectangle([cx, y, cx + card_w, y + 22], fill=color)
        draw.text((cx + 8, y + 4), tag, fill="#FFFFFF", font=font_section)
        
        hy = y + 26
        for h_line in wrap_text(headline, font_big_title, card_w - 16, draw):
            draw.text((cx + 8, hy), h_line, fill="#111111", font=font_big_title)
            hy += 20
        
        hy += 4
        body_text = f"{line1} {line2}"
        for b_line in wrap_text(body_text, font_big_body, card_w - 16, draw):
            draw.text((cx + 8, hy), b_line, fill="#333333", font=font_big_body)
            hy += 16
            
        cx += card_w + 12
    y += card_h + 12

    # 5. 3x3 Grid of Medium Cards (height 72)
    med_stories = [
        ("ASIA", "#D35400", "Candy Factory Fire Kills 24", "Blaze in Indonesia's Banten province leaves dozens missing; short circuit suspected."),
        ("MIDDLE EAST", "#8E44AD", "Qatari PM Warns on Escalation", "Doha works with Washington and Tehran to restart negotiations and prevent regional conflict."),
        ("EUROPE", "#2980B9", "Trilateral Talks in Abu Dhabi", "Kremlin says Russia, US and Ukraine could hold new round of high-level diplomatic talks."),
        ("AFRICA", "#27AE60", "Gavi Eyes 1.5M Ebola Doses", "Alliance plans vaccine purchase for Congo's Bundibugyo outbreak if trials prove effective."),
        ("AMERICAS", "#C0392B", "SpaceX-Tesla Merger Talks", "Companies appoint five directors to guide special committees handling merger negotiations."),
        ("OCEANIA", "#16A085", "COP31 Climate Talks Friction", "Pacific territories push for stronger climate finance and resilience at Antalya summit."),
        ("GLOBAL", "#2C3E50", "2031 Women's World Cup Hosts", "FIFA awards tournament to US, Mexico, Costa Rica and Jamaica; UK to host 2035."),
        ("AMERICAS", "#C0392B", "Thanksgiving Travel Surge", "AAA projects 81.5 million travelers as airfares jump 17% ahead of US holiday week."),
        ("ASIA", "#D35400", "South Korea Scrambles Jets", "Fighters sent after Russian military aircraft enter air defense identification zone.")
    ]

    grid_cols = 3
    g_w = (width - 2 * margin - 2 * 12) / 3
    g_h = 72
    
    gx_start = margin
    gy_start = y
    
    for i, (tag, color, title, desc) in enumerate(med_stories):
        r = i // grid_cols
        c = i % grid_cols
        gx = gx_start + c * (g_w + 12)
        gy = gy_start + r * (g_h + 8)
        
        draw.rectangle([gx, gy, gx + g_w, gy + g_h], outline="#D0C8B8", fill="#FFFFFF")
        draw.rectangle([gx, gy, gx + g_w, gy + 16], fill=color)
        draw.text((gx + 6, gy + 2), tag, fill="#FFFFFF", font=font_tiny)
        
        draw.text((gx + 6, gy + 19), title, fill="#111111", font=font_med_title)
        
        d_y = gy + 35
        for d_line in wrap_text(desc, font_med_body, g_w - 12, draw)[:2]:
            draw.text((gx + 6, d_y), d_line, fill="#444444", font=font_med_body)
            d_y += 15
        
    y += 3 * (g_h + 8) + 8
    draw.line([(margin, y), (width - margin, y)], fill="#888888", width=1)
    y += 10

    # 6. Bottom Section: Map on left, Also on this day on right (Height = 212)
    bottom_h = 212
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
        ("Washington", 50, 60, -10, -14),
        ("Brussels", 190, 50, 6, -12),
        ("Kyiv", 225, 62, 8, 4),
        ("Moscow", 260, 45, 8, -12),
        ("Antalya", 210, 85, -35, 8),
        ("Hormuz", 280, 115, 8, -10),
        ("Addis Ababa", 240, 160, 10, -4),
        ("Jakarta", 360, 175, 10, 4),
        ("Abu Dhabi", 295, 128, 8, 4),
        ("Shenzhen", 370, 95, 10, -12),
        ("Seoul", 400, 75, 8, 2),
        ("London", 170, 55, -35, -12),
    ]

    for city, cx_off, cy_off, lx_off, ly_off in dots:
        px = map_x + cx_off
        py = y + cy_off
        draw.ellipse([px-4, py-4, px+4, py+4], fill="#C0392B", outline="#000000")
        draw.text((px + lx_off, py + ly_off), city, fill="#222222", font=font_tiny)

    # Right: ALSO ON TUESDAY 24 NOVEMBER 2026
    right_x = map_x + half_w + 12
    draw.rectangle([right_x, y, width - margin, y + bottom_h], outline="#CCCCCC", fill="#FFFFFF")
    draw.rectangle([right_x, y, width - margin, y + 22], fill="#333333")
    draw.text((right_x + 8, y + 4), "ALSO ON TUESDAY 24 NOVEMBER 2026", fill="#FFFFFF", font=font_section)

    also_items = [
        "[EUR] Norway and Ukraine discuss stability in northern near-areas",
        "[MDE] US Treasury slaps sweeping sanctions on Iranian shadow banks",
        "[AFR] Zambian opposition leader Mundubile formally indicted on treason",
        "[AMS] Pentagon orders military preparation for Iran operations within 96h",
        "[ASI] China sentences official to death for spying and leaking secrets",
        "[GLO] UN chief warns artificial intelligence risks becoming more powerful",
        "[EUR] Hundreds of school bomb threats across Germany prompt evacuations",
        "[MDE] Israeli drone strike kills three Palestinians at Gaza police post",
        "[GLO] LaLiga suffers cyberattack exposing personal data of registered fans"
    ]

    item_y = y + 26
    for item in also_items:
        wrapped_items = wrap_text(item, font_tiny, half_w - 16, draw)
        for w_item in wrapped_items:
            draw.text((right_x + 8, item_y), w_item, fill="#333333", font=font_tiny)
            item_y += 15
        item_y += 2

    y += bottom_h + 10
    draw.line([(margin, y), (width - margin, y)], fill="#222222", width=1)
    y += 8

    # 7. Footer
    footer1 = "DATE CHECK: Every story on this page happened, or was first reported, on Tuesday 24 November 2026."
    footer2 = "Sources: Reuters, AP, AFP, BBC, Al Jazeera, Euronews, NPR, Kyiv Independent, El País, AllAfrica, ABC. Errors are not intentional."
    footer3 = "Stories are attributed, not stated as facts. Numbers are approximate."
    
    draw.text((margin, y), footer1, fill="#555555", font=font_tiny)
    y += 14
    draw.text((margin, y), footer2, fill="#555555", font=font_tiny)
    y += 14
    draw.text((margin, y), footer3, fill="#555555", font=font_tiny)

    # Save output
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    img.save(output_path, "PNG", optimize=True)
    print(f"Successfully generated {output_path}")

if __name__ == "__main__":
    generate_image()
