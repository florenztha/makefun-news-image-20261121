#!/usr/bin/env python3
"""Build poster.html for Saturday 21 November 2026: the world in one page.

V6 layout, rebuilt on the consensus formula of this edition's top ten:
the date itself is the masthead, a six-number strip and a region bar
computed from the stories printed, three leads and ten features drawn as
banner-labelled vector scenes, every card carrying its source and a
checked-status tag (CONFIRMED, OFFICIAL, REPORTED, CLAIM) with the legend
in the footer, the rest of the day as a numbered brief list beside a
small map, and a DATE CHECK box that names the Thursday and Friday news
left out. Every story was reported on Saturday 21 November 2026 in at
least one time zone.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- stories
# Cards: n (map pin), place, cat, head, body, region, src, tag.
LEADS = [
    dict(n=1, place="ANTALYA, TURKEY", cat="CLIMATE", region="AS",
         head="Climate summit runs into Saturday with no deal",
         body="Nearly 200 nations missed Friday's close as a draft silent "
              "on fossil fuels split the hall. A third text is promised; "
              "campaigners call the draft toothless.",
         src="(AP, AFP)", tag="CONFIRMED"),
    dict(n=2, place="RIYADH, SAUDI ARABIA", cat="WAR", region="ME",
         head="Three Houthi missiles shot down over Riyadh",
         body="Coalition air defences destroyed three ballistic missiles "
              "over Riyadh after 2am and a drone headed south; two more "
              "missiles were downed over Jazan on Friday evening. No "
              "casualties reported.",
         src="(Reuters, AFP)", tag="OFFICIAL"),
    dict(n=3, place="JUNIN, PERU", cat="EARTHQUAKE", region="AM",
         head="Magnitude 6.7 earthquake shakes central Peru",
         body="The quake struck 9 km from Carhuamayo, 108 km deep, at "
              "00:09 UTC and was felt in Lima. Indeci counts eight injured "
              "and 128 homes affected; the Navy ruled out a tsunami.",
         src="(USGS, IGP)", tag="OFFICIAL"),
]
FEATURES = [
    dict(n=4, place="KYIV, UKRAINE", cat="WAR", region="EU",
         head="Zelensky: the Crimea bridge 'will not stay'",
         body="He warns of more double-tap strikes ahead.",
         src="(NBC)", tag="REPORTED"),
    dict(n=5, place="STRAIT OF HORMUZ", cat="WAR", region="ME",
         head="Iran says it shot down a US drone over Hormuz",
         body="Tehran claims its 58th MQ-9; Washington has not confirmed it.",
         src="(IRIB)", tag="CLAIM"),
    dict(n=6, place="TEHRAN, IRAN", cat="DIPLOMACY", region="AS",
         head="Iran: uranium stock stays in the country",
         body="The minister still seeks a 'fair solution' to the standoff.",
         src="(Times of Israel)", tag="OFFICIAL"),
    dict(n=7, place="WASHINGTON, US", cat="TECH", region="AM",
         head="Trump vows tax on data centres abroad",
         body="'Tremendous' penalty promised; no details yet.",
         src="(ABC)", tag="REPORTED"),
    dict(n=8, place="BEIJING, CHINA", cat="DIPLOMACY", region="AS",
         head="China tells Japan to 'correct' its Taiwan words",
         body="Tokyo says its stance is unchanged.",
         src="(Ministry, AFP)", tag="OFFICIAL"),
    dict(n=9, place="DAVAO, PHILIPPINES", cat="AVIATION", region="AS",
         head="Jet lands safely after an engine fire alert",
         body="The Air Niugini 767 diverted after midnight; all safe.",
         src="(Airline, AP)", tag="OFFICIAL"),
    dict(n=10, place="CANBERRA, AUSTRALIA", cat="DIPLOMACY", region="OC",
         head="Australia and China agree to AI talks",
         body="Albanese wraps up an 11-day trip.",
         src="(ABC)", tag="OFFICIAL"),
    dict(n=11, place="WORLD", cat="MARKETS", region="GL",
         head="Bitcoin slips below $59,000",
         body="Down 3.9% in a day; ether changes hands at $1,625.",
         src="(CoinGecko)", tag="CONFIRMED"),
    dict(n=12, place="LAS VEGAS, US", cat="F1", region="AM",
         head="Russell fastest in Las Vegas practice",
         body="1:34.041 in a damp, messy final session.",
         src="(Formula 1)", tag="OFFICIAL"),
    dict(n=13, place="WELLINGTON, NZ", cat="CRICKET", region="OC",
         head="Rahul century puts India on top",
         body="India 344 for 2 at tea, replying to 368.",
         src="(AFP)", tag="OFFICIAL"),
]
# Briefs continue the numbering, 14 to 35: (place, region, text)
BRIEFS = [
    ("KRYVYI RIH, UKRAINE", "EU", "The double-tap strike's toll rises to 2 dead and 42 injured. (Kyiv Independent)"),
    ("COPENHAGEN, DENMARK", "EU", "A Russian attache is expelled over an alleged plot. (Al Jazeera)"),
    ("ANTALYA, TURKEY", "AS", "The EU warns COP31 risks becoming a 'fossil summit'. (AFP)"),
    ("ANTALYA, TURKEY", "AS", "Panama threatens to block the climate text. (Al Jazeera)"),
    ("WARSAW, POLAND", "EU", "NATO's Rutte visits after the missile incursion. (Reuters)"),
    ("SANAA, YEMEN", "ME", "Houthis threaten Jeddah and the Red Sea ports. (Al Jazeera)"),
    ("WASHINGTON, US", "AM", "Vance says the Iran strikes were Trump's call. (Reuters)"),
    ("WASHINGTON, US", "AM", "A lawmaker threatens SpaceX's funding. (CNN)"),
    ("TEXAS, US", "AM", "An execution of a man of 70 takes 63 minutes. (ABC)"),
    ("LOS ANGELES, US", "AM", "A jury convicts the man who started the Palisades fire. (ABC)"),
    ("MISSOURI, US", "AM", "A judge approves the $7.25bn Roundup settlement. (AFP)"),
    ("VANCOUVER, CANADA", "AM", "Canada rests its defence in a youth climate trial. (AFP)"),
    ("PYONGYANG, NORTH KOREA", "AS", "Kim tours factories; no Trump meeting follows. (AFP)"),
    ("SEJONG, SOUTH KOREA", "AS", "A freight train derails; no one is hurt. (Korea Herald)"),
    ("TAIPEI, TAIWAN", "AS", "A budget and a cash payout are passed. (Taipei Times)"),
    ("NEW DELHI, INDIA", "AS", "A Pakistani minister joins the SCO forum in India. (Dawn)"),
    ("GENEVA, SWITZERLAND", "EU", "'Killer robot' talks end with a 2028 aim. (Reuters)"),
    ("EASTERN INDIA", "AS", "Rain alerts as the remnants of Akvan move inland. (ETV)"),
    ("NAYPYIDAW, MYANMAR", "AS", "Myanmar calls the ICJ ruling unfair; rights groups urge sanctions. (AP)"),
    ("PORT LOUIS, MAURITIUS", "AF", "An African rating agency opens talks with 15 states. (Al Jazeera)"),
    ("MELBOURNE, AUSTRALIA", "OC", "Cummins keeps the Australian captaincy. (ABC)"),
    ("LAS VEGAS, US", "AM", "Verstappen is sent to the stewards after contact. (Autosport)"),
]
NUMS = [
    ("13", "days COP31 has run, a day past its close"),
    ("3", "ballistic missiles shot down over Riyadh"),
    ("6.7", "magnitude of the quake in Peru's Andes"),
    ("146", "people safe after the Davao landing"),
    ("$58,983", "Bitcoin early Saturday, down 3.9% in a day"),
    ("124*", "Rahul's score at tea in Wellington"),
]
REGIONS = [("EU", "Europe", "#33506e"), ("AS", "Asia", "#a03d2a"),
           ("ME", "Middle East", "#8c6d1f"), ("AF", "Africa", "#2e7d5b"),
           ("AM", "Americas", "#5b84a3"), ("OC", "Oceania", "#7a4a8c"),
           ("GL", "Global", "#555f6a")]
TAG_COLORS = {"CONFIRMED": "#1f7a8c", "OFFICIAL": "#2e7d5b",
              "REPORTED": "#c77400", "CLAIM": "#b3312a"}

# ------------------------------------------------------------------- arts
# Every panel: a flat scene, a big red banner label with the story's own
# words, and a small black chip with the count or status that anchors it.
def banner(label, bg, shapes, chip, h=96, fs=17):
    return (f'<svg viewBox="0 0 300 {h}" preserveAspectRatio="none">'
            f'<rect width="300" height="{h}" fill="{bg}"/>{shapes}'
            f'<rect x="0" y="0" width="{16 + len(label) * fs * 0.72:.0f}" height="26" fill="#b3312a"/>'
            f'<text x="8" y="19" font-family="Arial, sans-serif" font-size="{fs}" font-weight="800" fill="#ffffff">{label}</text>'
            f'<rect x="0" y="{h - 15}" width="{12 + len(chip) * 6.0:.0f}" height="15" fill="#14202b"/>'
            f'<text x="5" y="{h - 4}" font-family="Arial, sans-serif" font-size="8.5" font-weight="700" fill="#ffffff">{chip}</text></svg>')

def art_cop31(h):
    return banner("COP31: OVERTIME", "#dcebe2",
        '<circle cx="70" cy="58" r="21" fill="#7fb069"/><path d="M52 50 q18 -12 36 0 q-6 16 -18 20 q-12 -4 -18 -20" fill="#5b8c5a"/>'
        '<rect x="128" y="36" width="10" height="34" rx="5" fill="#e8e3d5" stroke="#8c2f26" stroke-width="2"/><circle cx="133" cy="74" r="8" fill="#b3312a"/>'
        '<circle cx="196" cy="56" r="19" fill="none" stroke="#33506e" stroke-width="3"/><path d="M196 44 v12 l9 6" stroke="#33506e" stroke-width="3" fill="none"/>'
        '<text x="238" y="62" font-family="Arial, sans-serif" font-size="15" font-weight="800" fill="#8c4a12">DAY 13</text>',
        "NO DEAL · DAY 13", h)

def art_saudi(h):
    bursts = '<path d="M196 34 l3 8 8 -3 -5 7 7 5 -9 1 -1 8 -4 -7 -8 3 4 -8 -7 -5 9 -1z" fill="#ffcf5c"/><path d="M248 52 l2 6 6 -2 -4 5 5 4 -7 1 -1 6 -3 -5 -6 2 3 -6 -5 -4 7 -1z" fill="#ffcf5c"/>'
    return banner("SAUDI: MISSILES", "#101d2c",
        '<path d="M0 78 L40 78 L46 62 L54 78 L120 78 L128 58 L136 78 L300 78 L300 96 L0 96 Z" fill="#060d16"/>'
        '<path d="M30 84 Q110 30 196 36 M120 84 Q190 40 250 54" stroke="#ffcf5c" stroke-width="2" stroke-dasharray="5 4" fill="none"/>'
        + bursts, "3 DOWN OVER RIYADH", h)

def art_peru(h):
    return banner("PERU: QUAKE 6.7", "#efe3c2",
        '<path d="M0 62 L50 62 L62 48 L76 62 L130 62 L142 44 L156 62 L300 62" stroke="#8c2f26" stroke-width="3" fill="none"/>'
        '<path d="M8 84 q14 -10 28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0 t28 0" stroke="#b3312a" stroke-width="2.6" fill="none"/>'
        '<path d="M226 62 l10 -16 10 16 z" fill="#a33"/><rect x="252" y="48" width="20" height="14" fill="#fdfaf1" stroke="#7a6a4a" stroke-width="1.6"/><path d="M250 48 l12 -8 12 8" stroke="#7a6a4a" stroke-width="2" fill="none"/>',
        "00:09 UTC · 108 KM DEEP", h)

def art_bridge(h):
    return banner("KYIV: WARNING", "#16283d",
        '<path d="M10 52 Q150 26 290 52" stroke="#7fa6c9" stroke-width="3" fill="none"/>'
        '<path d="M60 44 L60 60 M150 38 L150 60 M240 44 L240 60" stroke="#7fa6c9" stroke-width="2.6"/>'
        '<circle cx="212" cy="42" r="5" fill="#ff8a3c"/>',
        "MORE STRIKES WARNED", h, 13)

def art_hormuz(h):
    return banner("HORMUZ: DRONE", "#bcd6e4",
        '<path d="M0 54 h300 v42 H0z" fill="#5b84a3"/><path d="M96 54 l14 -12 h52 l10 12 z" fill="#33506e"/><rect x="118" y="32" width="30" height="10" fill="#b3312a"/>'
        '<path d="M238 30 l16 6 -16 6 -4 -6z" fill="#14202b"/><circle cx="242" cy="48" r="2.6" fill="#b3312a"/>',
        "IRAN'S CLAIM · UNCONFIRMED", h, 13)

def art_uranium(h):
    return banner("IRAN: URANIUM", "#f3e5cf",
        '<ellipse cx="90" cy="48" rx="42" ry="14" fill="none" stroke="#8c6d1f" stroke-width="2.6"/>'
        '<ellipse cx="90" cy="48" rx="42" ry="14" fill="none" stroke="#8c6d1f" stroke-width="2.6" transform="rotate(60 90 48)"/>'
        '<ellipse cx="90" cy="48" rx="42" ry="14" fill="none" stroke="#8c6d1f" stroke-width="2.6" transform="rotate(120 90 48)"/>'
        '<circle cx="90" cy="48" r="8" fill="#b3312a"/>'
        '<text x="160" y="54" font-family="Arial, sans-serif" font-size="13" font-weight="800" fill="#7a5a10">STOCK STAYS HOME</text>',
        "MINISTER: 'FAIR SOLUTION'", h, 13)

def art_trump(h):
    return banner("TRUMP: AI TAX", "#e8edf2",
        '<text x="52" y="64" font-family="Arial, sans-serif" font-size="44" font-weight="800" fill="#33506e">%</text>'
        '<path d="M150 34 h110 M150 46 h110 M150 58 h74" stroke="#b3312a" stroke-width="5"/>',
        "'TREMENDOUS' PENALTY", h, 13)

def art_chinajapan(h):
    return banner("CHINA-JAPAN", "#f6ecd9",
        '<rect x="36" y="32" width="58" height="34" fill="#de2910"/><circle cx="52" cy="44" r="5" fill="#ffde00"/><circle cx="62" cy="40" r="2" fill="#ffde00"/><circle cx="65" cy="47" r="2" fill="#ffde00"/>'
        '<rect x="130" y="32" width="58" height="34" fill="#ffffff" stroke="#999" stroke-width="1.4"/><circle cx="159" cy="49" r="9" fill="#bc002d"/>'
        '<path d="M212 49 h52 M252 40 l12 9 -12 9" stroke="#33506e" stroke-width="3.4" fill="none"/>',
        "TOKYO: STANCE UNCHANGED", h, 13)

def art_davao(h):
    return banner("DAVAO: 146 SAFE", "#dcebf2",
        '<path d="M20 52 L120 44 L210 30 Q236 28 244 36 L246 42 L150 52 L196 62 L188 68 L110 58 L60 62 Z" fill="#33506e"/>'
        '<circle cx="70" cy="50" r="2.4" fill="#fdfaf1"/><circle cx="86" cy="49" r="2.4" fill="#fdfaf1"/><circle cx="102" cy="48" r="2.4" fill="#fdfaf1"/><circle cx="118" cy="47" r="2.4" fill="#fdfaf1"/>'
        '<path d="M20 74 h260" stroke="#2e7d5b" stroke-width="2.6"/>',
        "ALL 146 ABOARD SAFE", h, 13)

def art_canberra(h):
    return banner("CANBERRA: AI", "#e9f4ee",
        '<path d="M34 32 h92 v24 h-56 l-14 12 v-12 h-22z" fill="#2e7d5b"/>'
        '<path d="M168 36 h92 v24 h-22 v12 l-14 -12 h-56z" fill="#b3312a"/>'
        '<circle cx="58" cy="44" r="3" fill="#fff"/><circle cx="74" cy="44" r="3" fill="#fff"/><circle cx="90" cy="44" r="3" fill="#fff"/>',
        "ALBANESE ENDS 11-DAY TRIP", h, 13)

def art_bitcoin(h):
    return banner("BITCOIN: $58,983", "#22161a",
        '<circle cx="58" cy="48" r="17" fill="#f7931a"/><text x="58" y="56" text-anchor="middle" font-family="Arial, sans-serif" font-size="21" font-weight="800" fill="#fff">B</text>'
        '<path d="M100 36 L140 44 L176 40 L214 56 L262 62" stroke="#e5484d" stroke-width="3" fill="none"/>'
        '<text x="196" y="34" font-family="Arial, sans-serif" font-size="13" font-weight="800" fill="#e5484d">-3.9%</text>',
        "DOWN 3.9% IN A DAY", h, 13)

def art_f1(h):
    return banner("RUSSELL: P1", "#e8edf2",
        '<path d="M28 56 L66 50 L96 38 L150 36 L176 48 L232 50 L244 56 L232 62 L40 62 Z" fill="#14202b"/>'
        '<circle cx="76" cy="62" r="8" fill="#333" stroke="#999" stroke-width="2"/><circle cx="204" cy="62" r="8" fill="#333" stroke="#999" stroke-width="2"/>'
        '<path d="M252 30 h34 v20 h-34z" fill="#fff" stroke="#14202b" stroke-width="1.6"/><path d="M252 40 h34 M261 30 v20 M270 30 v20 M278 30 v20" stroke="#14202b" stroke-width="1.4"/>',
        "1:34.041 · DAMP SESSION", h, 13)

def art_rahul(h):
    return banner("RAHUL: 124*", "#eef3e4",
        '<g transform="rotate(24 66 46)"><rect x="58" y="28" width="15" height="38" rx="4" fill="#c9a15a" stroke="#7a5a10" stroke-width="1.6"/></g>'
        '<circle cx="120" cy="56" r="8" fill="#b3312a"/>'
        '<text x="160" y="58" font-family="Arial, sans-serif" font-size="19" font-weight="800" fill="#1d5c40">124 NOT OUT</text>',
        "INDIA 344 FOR 2 AT TEA", h, 13)

LEAD_ARTS = {1: art_cop31, 2: art_saudi, 3: art_peru}
FEAT_ARTS = {4: art_bridge, 5: art_hormuz, 6: art_uranium, 7: art_trump,
             8: art_chinajapan, 9: art_davao, 10: art_canberra, 11: art_bitcoin,
             12: art_f1, 13: art_rahul}

# -------------------------------------------------------------------- css
CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1024px; height:1024px; overflow:hidden; background:#f7f1e3;
  font-family: Georgia, 'Times New Roman', serif; color:#14202b; padding:10px 18px 6px; }
.kicker { display:flex; justify-content:space-between; font-family: Arial, sans-serif;
  font-size:10.5px; font-weight:700; letter-spacing:2.2px; color:#ffffff;
  background:#b3312a; padding:5px 8px; }
h1 { text-align:center; font-size:46px; letter-spacing:0.5px; line-height:1.02; margin-top:4px; }
.subline { text-align:center; font-style:italic; font-size:14.5px; margin-top:3px; color:#33506e; }
.nums { display:flex; gap:0; margin-top:8px; border-top:1px solid #b9a888; border-bottom:1px solid #b9a888; }
.num { flex:1; padding:4px 8px 5px; border-left:3.5px solid #b3312a; }
.num + .num { border-left:3.5px solid #b3312a; margin-left:10px; }
.num b { font-size:21px; display:block; line-height:1.05; }
.num span { font-size:8.8px; font-family: Arial, sans-serif; line-height:1.15; display:block; }
.regionbar { display:flex; margin-top:6px; font-family: Arial, sans-serif; }
.regionbar div { color:#fff; font-size:7.6px; letter-spacing:0; font-weight:700; text-align:center; padding:3px 0; overflow:hidden; white-space:nowrap; }
.row { display:flex; gap:8px; margin-top:7px; }
.card { border:1px solid #b9a888; background:#fdfaf1; padding:6px 8px; }
.lead { flex:1; }
.lead svg, .feat svg { width:100%; display:block; }
.lead svg { height:88px; }
.place { font-family: Arial, sans-serif; font-size:9px; font-weight:700;
  letter-spacing:1px; color:#8c2f26; margin-top:5px; }
.place b { color:#14202b; background:#b3312a; color:#fff; border-radius:50%;
  display:inline-block; width:15px; height:15px; text-align:center; line-height:15px;
  font-size:9.5px; margin-right:4px; }
.lead h3 { font-size:16.5px; line-height:1.14; margin-top:2px; }
.feat h3 { font-size:11.4px; line-height:1.16; margin-top:2px; }
.lead p { font-size:9.4px; line-height:1.26; margin-top:3px; }
.feat p { font-size:8.6px; line-height:1.18; margin-top:2px; }
.srcrow { display:flex; justify-content:space-between; align-items:center; margin-top:3px; }
.src { font-family: Arial, sans-serif; font-size:8px; color:#555f6a; letter-spacing:0.4px; }
.tag { font-family: Arial, sans-serif; font-size:7.6px; font-weight:800; color:#fff;
  padding:1.5px 5px; letter-spacing:0.8px; }
.feat { flex:1; }
.mapbox { width:400px; flex:none; }
.mapbox .place { margin-top:0; color:#33506e; }
.mapsvg { width:100%; height:128px; display:block; margin-top:3px; }
.legend { font-family: Arial, sans-serif; font-size:8.4px; line-height:1.3; margin-top:4px; }
.briefs { flex:1; }
.briefs .place { margin-top:0; color:#33506e; }
.briefcols { display:flex; gap:14px; margin-top:3px; }
.briefcol { flex:1; }
.brief { font-size:8.5px; line-height:1.18; margin-bottom:3px; }
.brief b { color:#8c2f26; }
.brief .bn { font-weight:800; color:#b3312a; margin-right:3px; }
.footer { display:flex; gap:8px; margin-top:7px; }
.datecheck { flex:1.7; border:1.6px dashed #8c2f26; padding:4px 8px; font-size:8.8px; line-height:1.24; background:#fdf3e3; }
.credit { flex:1; font-size:8.8px; line-height:1.3; text-align:right; color:#555f6a; }
"""

# ------------------------------------------------------------------ build
import worldmap

def tag_html(tag):
    return f'<span class="tag" style="background:{TAG_COLORS[tag]}">{tag}</span>'

def card_lead(s):
    return (f'<div class="card lead">{LEAD_ARTS[s["n"]](96)}'
            f'<div class="place"><b>{s["n"]}</b>{s["place"]} · {s["cat"]}</div>'
            f'<h3>{s["head"]}</h3><p>{s["body"]}</p>'
            f'<div class="srcrow"><span class="src">{s["src"]}</span>{tag_html(s["tag"])}</div></div>')

def card_feat(s):
    return (f'<div class="card feat">{FEAT_ARTS[s["n"]](66)}'
            f'<div class="place"><b>{s["n"]}</b>{s["place"]} · {s["cat"]}</div>'
            f'<h3>{s["head"]}</h3><p>{s["body"]}</p>'
            f'<div class="srcrow"><span class="src">{s["src"]}</span>{tag_html(s["tag"])}</div></div>')

def build():
    counts = {}
    for s in LEADS + FEATURES:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    for _, rg, _ in BRIEFS:
        counts[rg] = counts.get(rg, 0) + 1
    total = sum(counts.values())
    nregions = len([1 for c in counts if counts[c]])
    regionbar = "".join(
        f'<div style="background:{color};flex:{counts[code]}">{name} {counts[code]}</div>'
        for code, name, color in REGIONS if counts.get(code))
    nums = "".join(f'<div class="num"><b>{v}</b><span>{t}</span></div>' for v, t in NUMS)
    leads = "".join(card_lead(s) for s in LEADS)
    feats1 = "".join(card_feat(s) for s in FEATURES[:5])
    feats2 = "".join(card_feat(s) for s in FEATURES[5:])
    half = (len(BRIEFS) + 1) // 2
    def brief_html(i, b):
        return f'<div class="brief"><span class="bn">{14 + i}</span><b>{b[0]}:</b> {b[2]}</div>'
    col1 = "".join(brief_html(i, b) for i, b in enumerate(BRIEFS[:half]))
    col2 = "".join(brief_html(half + i, b) for i, b in enumerate(BRIEFS[half:]))
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body>
<div class="kicker"><span>THE WORLD IN ONE DAY</span><span>{total} STORIES · {nregions} REGIONS · EVERY ONE DATED SATURDAY 21 NOVEMBER 2026</span></div>
<h1>Saturday 21 November 2026</h1>
<div class="subline">Climate summit runs past its deadline · Three missiles shot down over Riyadh · Strong quake shakes Peru</div>
<div class="nums">{nums}</div>
<div class="regionbar">{regionbar}</div>
<div class="row">{leads}</div>
<div class="row">{feats1}</div>
<div class="row">{feats2}</div>
<div class="row">
  <div class="mapbox"><div class="place">WHERE IT HAPPENED</div>{worldmap.render_map()}
  <div class="legend">Each number is the story with that number on this page; story 11 (Bitcoin) is worldwide and has no pin. Pins sit where the story happened.</div></div>
  <div class="briefs"><div class="place">ALSO ON SATURDAY 21 NOVEMBER 2026 · {len(BRIEFS)} MORE STORIES</div>
  <div class="briefcols"><div class="briefcol">{col1}</div><div class="briefcol">{col2}</div></div></div>
</div>
<div class="footer">
<div class="datecheck"><b>DATE CHECK</b> · Left out as Friday 20 November's news: Wall Street's fall into correction, the barrage that hit Kyiv's bridges, the missiles that landed in Poland, the UK-EU reset deal and Cyclone Akvan's landfall. Older still (Thu 19): the Shenzhen summit and the ICJ's Myanmar ruling; Myanmar's Saturday reaction is brief 32, and Kryvyi Rih's rising toll is brief 14. Not confirmed when drawn, so not shown: a final COP31 text.</div>
<div class="credit"><b>HOW WE CHECKED</b> · CONFIRMED = 2+ outlets · OFFICIAL = on the record · REPORTED = one outlet · CLAIM = one side's account. Every story here happened, or was first reported, on Saturday 21 November 2026. Original drawings, not photographs.</div>
</div>
</body></html>"""
    (HERE / "poster.html").write_text(html, encoding="utf-8")
    print("poster.html written:", len(html), "bytes;", total, "stories; regions:", counts)

if __name__ == "__main__":
    build()
