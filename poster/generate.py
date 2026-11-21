#!/usr/bin/env python3
"""Build poster.html for Saturday 21 November 2026: the world in one page.

Every story below was reported on Saturday 21 November 2026 in at least one
time zone. Leads and features are drawn as original flat vector scenes whose
art carries the day's own numbers; briefs keep full context (place, what
happened, and the outcome or figure that makes it news), never a bare wire
headline. Region counts are computed from the story data, so the region bar
always matches the stories printed.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- stories
# n: map pin number, place, head, body, region code
LEADS = [
    dict(n=1, place="KYIV, UKRAINE", region="EU",
         head="Russia fires 510 weapons at Ukraine; missiles land in Poland",
         body="More than 400 drones and 110 missiles hit Ukraine overnight. At "
              "least 8 people were killed in Kyiv, bridges and stations "
              "damaged, and about 20 more wounded in Kryvyi Rih. Two missiles "
              "and a drone came down in Poland; Tusk called it a deliberate "
              "provocation."),
    dict(n=2, place="SHENZHEN, CHINA", region="AS",
         head="Trump, Xi and Putin sign a peace declaration that skips Ukraine",
         body="The US, Chinese and Russian leaders met three ways for the "
              "first time and issued a joint peace declaration, with Xi at "
              "centre stage. The text said nothing about Ukraine, and "
              "afterwards Trump told European leaders to defund Kyiv."),
    dict(n=3, place="THE HAGUE, NETHERLANDS", region="EU",
         head="World court: Myanmar committed genocide against the Rohingya",
         body="The Court of Justice found Myanmar responsible for genocide "
              "against the Rohingya, the first time an international court "
              "has found a state guilty of genocide. Myanmar called it unfair."),
]
FEATURES = [
    dict(n=4, place="NEW YORK, UNITED STATES", region="NA",
         head="AI rout tips Wall Street into correction",
         body="US stocks fell 3.7% as an AI and chip sell-off pushed the S&P "
              "500 and Dow into correction, the same week Anthropic opened "
              "trading worth about $2 trillion."),
    dict(n=5, place="ANTALYA, TURKEY", region="ME",
         head="COP31 runs into overtime over fossil fuels",
         body="Nearly 200 nations at the UN climate summit failed to agree by "
              "the deadline, deadlocked over fossil fuel language that "
              "environmentalists say the draft ignores."),
    dict(n=6, place="BRUSSELS, BELGIUM", region="EU",
         head="Britain and the EU sign their biggest post-Brexit reset",
         body="PM Burnham and EU leaders signed three agreements in Brussels "
              "on food exports, carbon markets and youth mobility, a decade "
              "after the Brexit vote."),
    dict(n=7, place="LONDON, UNITED KINGDOM", region="EU",
         head="Pill makes pancreatic tumours vanish in 1 in 12 patients",
         body="In a trial of the pill daraxonrasib, scans found no detectable "
              "cancer in one in 12 patients, a landmark result against one "
              "of the deadliest cancers."),
]
MINIS = [
    dict(n=8, place="BERLIN, GERMANY", region="EU",
         head="Gen Z protests spread across 25 European countries",
         body="Youth-led demonstrations rolled across the continent, the widest wave yet."),
    dict(n=9, place="STRAIT OF HORMUZ", region="ME",
         head="Iran says it downed a US MQ-9 drone over the strait",
         body="Tehran claimed its 58th MQ-9, while Lewis Pugh swam the strait for its wildlife."),
    dict(n=10, place="GAZA", region="ME",
         head="Israeli strikes kill Palestinians despite the peace deal",
         body="A drone strike on Salah al-Din Street killed one man; West Bank violence went on."),
    dict(n=11, place="YONGBYON, NORTH KOREA", region="AS",
         head="North Korea is expanding its uranium plant",
         body="The UN watchdog says Yongbyon is growing, as Trump calls China's build-up intense."),
    dict(n=12, place="NUUK, GREENLAND", region="NA",
         head="Denmark ratifies the US Greenland security deal 109-0",
         body="The unanimous vote allows two new American bases on the island."),
    dict(n=13, place="KERCH, CRIMEA", region="EU",
         head="Ukraine hits the Crimea bridge a third time in four days",
         body="Kyiv struck the Kerch Bridge again as Berlin hosted talks on the war."),
]
BRIEFS = [
    ("CARACAS, VENEZUELA", "The US signed a new military deal, ten months after US forces removed Maduro."),
    ("DHAKA, BANGLADESH", "Violence flared ahead of ex-PM Sheikh Hasina's planned return."),
    ("MADRID, SPAIN", "Spain heads to an election on 29 November, conservatives gaining."),
    ("PORT-AU-PRINCE, HAITI", "Salvadoran troops in Haiti lost soldiers to explosives."),
    ("LOS ANGELES, US", "A man was convicted of starting the deadly Palisades fire."),
    ("TALLINN, ESTONIA", "Estonia will close its border crossings with Russia."),
    ("ULAANBAATAR, MONGOLIA", "Mongolia's president resigned; elections follow within four months."),
    ("SANAA, YEMEN", "The UN counts about 357,000 displaced across Yemen since August."),
    ("WASHINGTON, US", "The FBI's criminal database was reportedly hacked amid US outages."),
    ("CALIFORNIA, US", "14 charged over a train cargo theft ring accused of stealing $22.5M."),
    ("RIYADH, SAUDI ARABIA", "Saudi Arabia intercepted a Houthi missile a day after a Riyadh tower hit."),
    ("DAMASCUS, SYRIA", "Syria captured a former general accused of a 2014 massacre."),
    ("BOGOTA, COLOMBIA", "A nationwide work stoppage shut roads amid protests."),
    ("UNITED NATIONS", "The UN cut its food aid target despite a looming starvation threat."),
    ("GENEVA, SWITZERLAND", "UN talks on lethal autonomous weapons fell short of binding rules."),
    ("COPENHAGEN, DENMARK", "Denmark says Russia plotted to kill a US-Ukrainian artist."),
    ("GEORGIA, US", "A man was arrested for sending $26,000 to Islamic State linked people."),
    ("BRASILIA, BRAZIL", "Students turned scorched fish bones into a clean water filter."),
    ("FRANKFURT, GERMANY", "Lufthansa plans 1,000 job cuts at Frankfurt and Munich airports."),
]
REGIONS = [("NA", "N AMERICA"), ("SA", "S AMERICA"), ("EU", "EUROPE"),
           ("AF", "AFRICA"), ("ME", "MID EAST"), ("AS", "ASIA"),
           ("OC", "OCEANIA"), ("WS", "WORLD")]
# region of each brief, in order, for the computed region bar
BRIEF_REGIONS = ["SA", "AS", "EU", "NA", "NA", "EU", "AS", "ME", "NA", "NA",
                 "ME", "ME", "SA", "WS", "EU", "EU", "NA", "SA", "EU"]

NUMBERS = [
    ("510", "drones and missiles fired at Ukraine in one night"),
    ("8+", "killed in Kyiv; 2 missiles down in Poland"),
    ("-3.7%", "US stocks fall as the AI rout bites"),
    ("$2 TRILLION", "Anthropic's value as it opens trading"),
    ("1 IN 12", "patients whose tumours vanished on the pill"),
    ("109-0", "Denmark's vote for the Greenland deal"),
]

# ------------------------------------------------------------------- arts
def art_kyiv():
    return """<svg viewBox="0 0 300 84" preserveAspectRatio="none">
<rect width="300" height="84" fill="#16283d"/>
<path d="M0 68 L60 68 L70 54 L80 68 L150 68 L160 50 L170 68 L300 68 L300 84 L0 84 Z" fill="#0b1622"/>
<path d="M20 68 Q150 40 280 68" stroke="#7fa6c9" stroke-width="3" fill="none"/>
<path d="M52 58 L52 72 M150 50 L150 72 M248 58 L248 72" stroke="#7fa6c9" stroke-width="3"/>
<path d="M96 6 L138 40 M238 8 L196 42" stroke="#ffcf5c" stroke-width="2.5"/>
<circle cx="142" cy="43" r="5" fill="#ff8a3c"/><circle cx="192" cy="45" r="6" fill="#ff8a3c"/>
<text x="10" y="24" font-size="20" font-weight="800" fill="#ffffff">KYIV</text>
<text x="10" y="40" font-size="10" font-weight="700" fill="#ffcf5c">400+ DRONES · 110 MISSILES · BRIDGES HIT</text>
<rect x="188" y="6" width="104" height="16" fill="#b3312a"/><text x="193" y="17.5" font-size="9" font-weight="800" fill="#fff">2 DOWN IN POLAND</text>
</svg>"""

def art_shenzhen():
    flags = ""
    for i, (c1, c2, label) in enumerate([("#3c3b6e", "#b22234", "USA"),
                                         ("#de2910", "#de2910", "CHINA"),
                                         ("#2a4d9b", "#d52b1e", "RUSSIA")]):
        x = 18 + i * 96
        flags += f'<rect x="{x}" y="8" width="76" height="34" fill="{c1}"/>'
        if label == "RUSSIA":
            flags += f'<rect x="{x}" y="19" width="76" height="12" fill="#ffffff"/><rect x="{x}" y="31" width="76" height="11" fill="{c2}"/>'
        if label == "CHINA":
            flags += f'<circle cx="{x+16}" cy="19" r="6" fill="#ffde00"/>'
        if label == "USA":
            flags += f'<path d="M{x} 14 h76 M{x} 21 h76 M{x} 28 h76 M{x} 35 h76" stroke="#fff" stroke-width="3"/>'
        flags += f'<text x="{x+38}" y="55" font-size="10" font-weight="800" fill="#14202b" text-anchor="middle">{label}</text>'
    return f"""<svg viewBox="0 0 300 84" preserveAspectRatio="none">
<rect width="300" height="84" fill="#f3e5cf"/>{flags}
<text x="150" y="74" font-size="10.5" font-weight="800" fill="#8c2f26" text-anchor="middle">3 LEADERS · 1 DECLARATION · SILENT ON UKRAINE</text>
</svg>"""

def art_icj():
    cols = "".join(f'<rect x="{28+i*34}" y="30" width="13" height="34" fill="#5b7186"/>' for i in range(7))
    return f"""<svg viewBox="0 0 300 84" preserveAspectRatio="none">
<rect width="300" height="84" fill="#e8edf2"/>
<path d="M14 30 L150 6 L286 30 Z" fill="#33506e"/>
<rect x="14" y="64" width="272" height="6" fill="#33506e"/>{cols}
<g transform="rotate(-9 218 52)"><rect x="156" y="36" width="124" height="30" fill="none" stroke="#b3312a" stroke-width="3.2"/>
<text x="218" y="57" font-size="16.5" font-weight="800" fill="#b3312a" text-anchor="middle">GENOCIDE</text></g>
<text x="12" y="80" font-size="9.5" font-weight="700" fill="#33506e">THE HAGUE · WORLD COURT RULING</text>
</svg>"""

def art_markets():
    return """<svg viewBox="0 0 300 74" preserveAspectRatio="none">
<rect width="300" height="74" fill="#22161a"/>
<path d="M118 14 L160 22 L196 20 L228 36 L258 44 L292 56" stroke="#e5484d" stroke-width="3" fill="none"/>
<path d="M292 56 l-24 0 18 -10 z" fill="#e5484d"/>
<text x="10" y="32" font-size="25" font-weight="800" fill="#ff6b6b">-3.7%</text>
<text x="10" y="48" font-size="9" font-weight="700" fill="#f3c1c1">S&amp;P 500 AND DOW INTO CORRECTION</text>
<rect x="0" y="56" width="300" height="18" fill="#173d2a"/><text x="10" y="69" font-size="9.5" font-weight="800" fill="#7be3a8">SAME WEEK: ANTHROPIC DEBUTS AT $2 TRILLION</text>
</svg>"""

def art_cop31():
    return """<svg viewBox="0 0 300 74" preserveAspectRatio="none">
<rect width="300" height="74" fill="#f6ddae"/>
<circle cx="34" cy="28" r="16" fill="#e8963c"/>
<path d="M238 58 q8 -26 28 -32 q-3 17 6 24 q13 -6 11 -20 q17 11 9 28 z" fill="#6b6f72"/>
<text x="62" y="34" font-size="15.5" font-weight="800" fill="#8c4a12">COP31: INTO OVERTIME</text>
<text x="62" y="52" font-size="9.5" font-weight="700" fill="#6d4c1e">200 NATIONS · NO FOSSIL FUEL DEAL</text>
</svg>"""

def art_brussels():
    stars = "".join(f'<circle cx="{150+26*__import__("math").cos(a):.0f}" cy="{27+26*__import__("math").sin(a):.0f}" r="3" fill="#ffcc00"/>' for a in [i * 0.5236 for i in range(12)])
    return f"""<svg viewBox="0 0 300 74" preserveAspectRatio="none">
<rect width="300" height="74" fill="#22406e"/>{stars}
<circle cx="150" cy="27" r="14" fill="#22406e" stroke="#ffcc00" stroke-width="1.4"/>
<text x="150" y="32" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">UK + EU</text>
<text x="150" y="66" font-size="10.5" font-weight="800" fill="#ffd76a" text-anchor="middle">FOOD · CARBON · YOUTH MOBILITY SIGNED</text>
</svg>"""

def art_pill():
    return """<svg viewBox="0 0 300 74" preserveAspectRatio="none">
<rect width="300" height="74" fill="#e9f4ee"/>
<g transform="rotate(-24 52 34)"><rect x="12" y="20" width="80" height="28" rx="14" fill="#2e7d5b"/><rect x="52" y="20" width="40" height="28" rx="14" fill="#f2f2f2" stroke="#2e7d5b" stroke-width="2"/></g>
<text x="108" y="38" font-size="21" font-weight="800" fill="#1d5c40">1 IN 12</text>
<text x="108" y="56" font-size="9.5" font-weight="700" fill="#1d5c40">PATIENTS: NO TUMOUR FOUND ON SCANS</text>
<circle cx="272" cy="24" r="13" fill="none" stroke="#2e7d5b" stroke-width="2.6"/><path d="M264 24 l6 6 l11 -13" stroke="#2e7d5b" stroke-width="3.4" fill="none"/>
</svg>"""

ARTS = {1: art_kyiv, 2: art_shenzhen, 3: art_icj, 4: art_markets,
        5: art_cop31, 6: art_brussels, 7: art_pill}

# -------------------------------------------------------------------- map
GRID = [
    "    ####  ##        ####                    #########  ############   ",
    "  ###########      ######        ##       ######################### ",
    " #############    ########            ############################  ",
    "  ##########       #####      ##   ###############################  ",
    "   ########              ########  ##############################   ",
    "    ######            #  #########################  #############   ",
    "     #####            ###########################    ##########     ",
    "      ####     #       #########################       ########     ",
    "      #####            #######################   ##     ######      ",
    "       ####            #####################    ###    #####        ",
    "       ###              ##################     ####     ####        ",
    "        ##     #         ################      #####     ###        ",
    "        ###   ###         ##############       ######     ##        ",
    "         ##  #####         ############         ####     ####       ",
    "          # ########        ##########          ###      ########   ",
    "           #########         ########           ##       #########  ",
    "            ########          ######            #         ########  ",
    "             ######           #####                        ######   ",
    "             #####            ####                          ####    ",
    "             ####             ###              ##           ###     ",
    "             ###              ##              ####          ##      ",
    "             ###                              #####                 ",
    "             ##                                ###         #        ",
    "             #                                 #           ##       ",
    "             #                                             ##       ",
    "            #                                               #       ",
]
PINS = {1: (30.5, 50.4), 2: (114.2, 22.5), 3: (4.3, 52.1), 4: (-74.0, 40.7),
        5: (30.7, 36.9), 6: (4.35, 50.8), 7: (-0.1, 51.5), 8: (13.4, 52.5),
        9: (56.3, 26.3), 10: (34.3, 31.3), 11: (125.8, 39.8),
        12: (-41.7, 64.2), 13: (36.6, 45.4)}

def world_map():
    from worldmap import render_map
    return render_map()


# ------------------------------------------------------------------ build
CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1024px; height:1024px; overflow:hidden; background:#f7f1e3;
  font-family: Georgia, 'Times New Roman', serif; color:#14202b; padding:14px 18px 6px; }
.kicker { display:flex; justify-content:space-between; font-family: Arial, sans-serif;
  font-size:10.5px; font-weight:700; letter-spacing:2.2px; color:#8c2f26;
  border-bottom:2.5px solid #14202b; padding-bottom:5px; }
h1 { text-align:center; font-size:44px; letter-spacing:1px; line-height:1.0; margin-top:3px; }
.subline { text-align:center; font-family: Arial, sans-serif; font-size:12.5px;
  font-weight:700; letter-spacing:1.6px; margin-top:3px; color:#33506e; }
.strap { background:#b3312a; color:#fff; font-family: Arial, sans-serif; font-weight:800;
  font-size:12.2px; text-align:center; padding:5px 6px; margin-top:6px; letter-spacing:.2px; }
.nums { display:flex; gap:6px; margin-top:5px; }
.num { flex:1; background:#14202b; color:#f7f1e3; text-align:center; padding:5px 3px 4px; }
.num b { display:block; font-size:17px; color:#ffd76a; font-family: Arial, sans-serif; }
.num span { font-size:8.6px; font-family: Arial, sans-serif; line-height:1.15; display:block; }
.row { display:flex; gap:8px; margin-top:6px; }
.card { background:#fffdf6; border:1.6px solid #14202b; padding:6px 7px 5px; }
.card svg { width:100%; display:block; }
.lead { flex:1; }
.lead svg { height:78px; }
.feat { flex:1; }
.feat svg { height:54px; }
.pnum { display:inline-block; background:#b3312a; color:#fff; font-family: Arial, sans-serif;
  font-weight:800; font-size:10.5px; border-radius:50%; width:16px; height:16px;
  text-align:center; line-height:16px; margin-right:4px; vertical-align:1px; }
.place { font-family: Arial, sans-serif; font-size:9px; font-weight:800; letter-spacing:1.1px; color:#8c2f26; margin-top:4px; }
.lead h2 { font-size:15.8px; line-height:1.12; margin-top:2px; }
.feat h3 { font-size:12.4px; line-height:1.13; margin-top:2px; }
.lead p, .feat p { font-size:10px; line-height:1.27; margin-top:3px; }
.lead p { font-size:10.4px; }
.mapbox { width:468px; flex:none; }
.mapbox .place { margin-top:0; }
.mapsvg { width:100%; height:158px; display:block; margin-top:3px; }
.legend { font-family: Arial, sans-serif; font-size:8.4px; margin-top:3px; color:#33506e; }
.minis { flex:1.08; }
.mini { display:flex; gap:5px; padding:2px 0; border-bottom:1px solid #cbbfa4; }
.mini:last-child { border-bottom:none; }
.mini h4 { font-size:11.2px; line-height:1.1; }
.mini p { font-size:9.3px; line-height:1.08; }
.mini .place { margin-top:0; }
.briefhead { font-family: Arial, sans-serif; font-weight:800; font-size:11px; letter-spacing:1.6px;
  border-top:2.5px solid #14202b; border-bottom:1px solid #14202b; padding:3px 0; margin-top:4px;
  display:flex; justify-content:space-between; }
.briefs { display:flex; gap:14px; margin-top:5px; }
.bcol { flex:1; }
.brief { font-size:8.6px; line-height:1.14; margin-bottom:3px; }
.brief b { font-family: Arial, sans-serif; font-size:8.5px; letter-spacing:.3px; }
.footer { display:flex; gap:8px; margin-top:3px; }
.datecheck { flex:1.65; border:1.6px dashed #8c2f26; padding:4px 8px; font-size:8.8px; line-height:1.22; background:#fdf3e3; }
.datecheck b { font-family: Arial, sans-serif; font-size:9.4px; color:#8c2f26; letter-spacing:.6px; }
.credit { flex:1; font-family: Arial, sans-serif; font-size:8.8px; line-height:1.4; color:#33506e; padding-top:2px; }
"""

def card(s, cls, tag):
    return (f'<div class="card {cls}">{ARTS[s["n"]]()}'
            f'<div class="place"><span class="pnum">{s["n"]}</span>{s["place"]}</div>'
            f'<{tag}>{s["head"]}</{tag}><p>{s["body"]}</p></div>')

def build_html():
    total = len(LEADS) + len(FEATURES) + len(MINIS) + len(BRIEFS)
    counts = {}
    for s in LEADS + FEATURES + MINIS:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    for r in BRIEF_REGIONS:
        counts[r] = counts.get(r, 0) + 1
    region_bar = " · ".join(f"{name} {counts.get(code, 0)}" for code, name in REGIONS if counts.get(code))
    nums = "".join(f'<div class="num"><b>{v}</b><span>{t}</span></div>' for v, t in NUMBERS)
    leads = "".join(card(s, "lead", "h2") for s in LEADS)
    feats = "".join(card(s, "feat", "h3") for s in FEATURES)
    minis = "".join(
        f'<div class="mini"><div><div class="place"><span class="pnum">{s["n"]}</span>{s["place"]}</div>'
        f'<h4>{s["head"]}</h4><p>{s["body"]}</p></div></div>' for s in MINIS)
    per = (len(BRIEFS) + 2) // 3
    cols = ""
    for i in range(3):
        chunk = BRIEFS[i * per:(i + 1) * per]
        cols += '<div class="bcol">' + "".join(
            f'<div class="brief"><b>{p}:</b> {t}</div>' for p, t in chunk) + "</div>"
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="kicker"><span>THE WORLD IN ONE DAY</span><span>SATURDAY'S NEWS · ONE PAGE · {total} STORIES</span></div>
<h1>THE WORLD IN ONE PAGE</h1>
<div class="subline">SATURDAY 21 NOVEMBER 2026 · {region_bar}</div>
<div class="strap">510 WEAPONS FALL ON UKRAINE, 2 IN POLAND · PEACE TEXT SILENT ON UKRAINE · WORLD COURT: MYANMAR GENOCIDE · AI ROUT VS $2 TRILLION DEBUT</div>
<div class="nums">{nums}</div>
<div class="row">{leads}</div>
<div class="row">{feats}</div>
<div class="row">
  <div class="card mapbox"><div class="place">WHERE IT HAPPENED · NUMBERED AS PRINTED · GOLD RING = THE THREE LEADS</div>{world_map()}
  <div class="legend">1 KYIV · 2 SHENZHEN · 3 THE HAGUE · 4 NEW YORK · 5 ANTALYA · 6 BRUSSELS · 7 LONDON · 8 BERLIN · 9 HORMUZ · 10 GAZA · 11 YONGBYON · 12 GREENLAND · 13 KERCH</div></div>
  <div class="minis">{minis}</div>
</div>
<div class="briefhead"><span>AROUND THE WORLD IN BRIEF</span><span>{len(BRIEFS)} MORE STORIES</span></div>
<div class="briefs">{cols}</div>
<div class="footer">
  <div class="datecheck"><b>DATE CHECK:</b> every story above was reported on Saturday 21 November 2026. The Shenzhen leaders met on Thursday; their declaration, and Trump's defund-Ukraine call after it, are Saturday's news. Anthropic opened trading on Thursday; its $2 trillion value is printed with the sell-off.</div>
  <div class="credit">Drawn and set in one page from Saturday's reporting (AP, Reuters, AFP, BBC, France 24, CBS, El Pais, UN News, IAEA). No photographs: every scene is an original drawing.</div>
</div>
</body></html>"""

def main():
    out = HERE / "poster.html"
    out.write_text(build_html(), encoding="utf-8")
    print("poster.html", out.stat().st_size, "bytes")

if __name__ == "__main__":
    main()
