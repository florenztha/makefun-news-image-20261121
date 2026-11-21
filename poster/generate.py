#!/usr/bin/env python3
"""Build poster.html for Saturday 21 November 2026: the world in one page.

V5 layout, rebuilt on the formula the current leaders use: the date itself
is the masthead, every art panel carries a big red banner label with the
story's own hard number, cards run one or two lines of body, and the rest
of the day continues as a numbered brief list beside a small map. Every
story was reported on Saturday 21 November 2026 in at least one time zone;
unconfirmed claims are labelled as claims. Region counts are computed from
the story data, so the region bar always matches the stories printed.
"""
import pathlib

HERE = pathlib.Path(__file__).parent

# ---------------------------------------------------------------- stories
# Cards: n (map pin), place, cat, head, body, region code.
LEADS = [
    dict(n=1, place="ANTALYA, TURKEY", cat="CLIMATE", region="ME",
         head="Climate summit runs into Saturday with no deal",
         body="Nearly 200 nations missed Friday's close as a draft silent "
              "on fossil fuels split the hall. A third text is promised; "
              "campaigners call the draft toothless.",
         src="DEADLINE MISSED · TALKS GO ON"),
    dict(n=2, place="RIYADH, SAUDI ARABIA", cat="WAR", region="ME",
         head="Three Houthi missiles shot down over Riyadh",
         body="Coalition air defences destroyed three ballistic missiles "
              "over Riyadh after 2am and a drone headed south; two more "
              "missiles were downed over Jazan on Friday evening. No "
              "casualties reported.",
         src="COALITION COUNT · VIA REUTERS"),
    dict(n=3, place="JUNIN, PERU", cat="EARTHQUAKE", region="SA",
         head="Magnitude 6.7 earthquake shakes central Peru",
         body="The quake struck 9 km from Carhuamayo, 108 km deep, at "
              "00:09 UTC and was felt in Lima. Indeci counts eight injured "
              "and 128 homes affected; the Navy ruled out a tsunami.",
         src="USGS · IGP · INDECI"),
]
FEATURES = [
    dict(n=4, place="KYIV, UKRAINE", cat="WAR", region="EU",
         head="Ukraine hits the Kerch Bridge a third time in four days",
         body="The strike came hours after the night barrage on Kyiv."),
    dict(n=5, place="STRAIT OF HORMUZ", cat="WAR", region="ME",
         head="Iran says it shot down a US drone over Hormuz",
         body="Tehran claims its 58th MQ-9; Washington has not confirmed it."),
    dict(n=6, place="NEW YORK, US", cat="MARKETS", region="NA",
         head="AI rout tips Wall Street into correction",
         body="Stocks fell 3.7%, the week Anthropic debuted at $2 trillion."),
    dict(n=7, place="THE HAGUE", cat="WORLD COURT", region="EU",
         head="World court: Myanmar committed genocide",
         body="The court found the state responsible for genocide against "
              "the Rohingya; Myanmar rejects the ruling."),
    dict(n=8, place="SHENZHEN", cat="DIPLOMACY", region="AS",
         head="A peace declaration that skips Ukraine",
         body="Trump, Xi and Putin's text says nothing about Ukraine; "
              "Trump then told Europe to defund Kyiv."),
    dict(n=9, place="GAZA", cat="WAR", region="ME",
         head="Israeli strikes kill Palestinians despite the peace deal",
         body="A drone strike on Salah al-Din Street killed one man."),
    dict(n=10, place="YONGBYON", cat="NUCLEAR", region="AS",
         head="North Korea is expanding its uranium plant",
         body="The UN watchdog says new buildings are rising at Yongbyon."),
    dict(n=11, place="BERLIN", cat="PROTESTS", region="EU",
         head="Gen Z protests spread across 25 European countries",
         body="Youth-led demonstrations rolled across the continent."),
    dict(n=12, place="NUUK", cat="DIPLOMACY", region="NA",
         head="Denmark ratifies the US Greenland security deal 109-0",
         body="The unanimous vote allows two new American bases."),
    dict(n=13, place="LONDON, UK", cat="MEDICINE", region="EU",
         head="Pill makes pancreatic tumours vanish in 1 in 12 patients",
         body="Scans found no detectable cancer in one in 12 on the trial."),
]
# Briefs continue the numbering, 14 to 35: (place, region, text)
BRIEFS = [
    ("CARACAS, VENEZUELA", "SA", "The US signed a new military deal, ten months after removing Maduro."),
    ("DHAKA, BANGLADESH", "AS", "Violence flared ahead of ex-PM Sheikh Hasina's planned return."),
    ("MADRID, SPAIN", "EU", "Spain heads to an election on 29 November, conservatives gaining."),
    ("PORT-AU-PRINCE, HAITI", "NA", "Salvadoran troops in Haiti lost soldiers to explosives."),
    ("LOS ANGELES, US", "NA", "A man was convicted of starting the deadly Palisades fire."),
    ("TALLINN, ESTONIA", "EU", "Estonia will close its border crossings with Russia."),
    ("ULAANBAATAR, MONGOLIA", "AS", "Mongolia's president resigned; elections follow within four months."),
    ("SANAA, YEMEN", "ME", "The UN counts about 257,000 displaced across Yemen since August."),
    ("WASHINGTON, US", "NA", "The FBI's criminal database was reportedly hacked amid US outages."),
    ("CALIFORNIA, US", "NA", "14 charged over a train cargo theft ring accused of stealing $22.5M."),
    ("RIYADH, SAUDI ARABIA", "ME", "Saudi Arabia downed a Houthi missile a day after the Riyadh tower hit."),
    ("DAMASCUS, SYRIA", "ME", "Syria captured a former general accused of a 2014 massacre."),
    ("BOGOTA, COLOMBIA", "SA", "A nationwide work stoppage shut roads amid protests."),
    ("UNITED NATIONS", "WO", "The UN cut its food aid target despite a looming starvation threat."),
    ("GENEVA, SWITZERLAND", "EU", "UN talks on lethal autonomous weapons fell short of binding rules."),
    ("COPENHAGEN, DENMARK", "EU", "Denmark says Russia plotted to kill a US-Ukrainian artist."),
    ("GEORGIA, US", "NA", "A man was arrested for sending $26,000 to Islamic State linked people."),
    ("BRASILIA, BRAZIL", "SA", "Students turned scorched fish bones into a clean water filter."),
    ("FRANKFURT, GERMANY", "EU", "Lufthansa plans 1,000 job cuts at Frankfurt and Munich airports."),
    ("JEDDAH, SAUDI ARABIA", "ME", "Houthis threaten Red Sea ports; airlines warned Saudi airspace is unsafe."),
    ("LIMA, PERU", "SA", "Peru's Navy ruled out any tsunami on the coast after the Junin quake."),
    ("CARHUAMAYO, PERU", "SA", "The mayor of the town nearest the epicentre reported no victims there."),
]
NUMS = [
    ("DAY 13", "of a COP31 summit due to close on day 12"),
    ("3", "ballistic missiles destroyed over Riyadh"),
    ("6.7", "magnitude of the quake in Peru's Andes"),
    ("$55,130", "Bitcoin's Saturday low, worst since 2024"),
    ("109-0", "Denmark's vote for the Greenland deal"),
    ("1 IN 12", "patients whose tumours vanished"),
]
REGIONS = [("EU", "Europe", "#33506e"), ("ME", "Middle East", "#b3312a"),
           ("AS", "Asia", "#8c6d1f"), ("NA", "N America", "#2e7d5b"),
           ("SA", "S America", "#7a4a8c"), ("WO", "World", "#555f6a")]

# ------------------------------------------------------------------- arts
# Every panel: a flat scene, a big red banner label with the story's own
# words, and a small black chip with the count or status that anchors it.
def banner(label, bg, shapes, chip, h=96, fs=17):
    return (f'<svg viewBox="0 0 300 {h}" preserveAspectRatio="none">'
            f'<rect width="300" height="{h}" fill="{bg}"/>{shapes}'
            f'<rect x="0" y="0" width="{16 + len(label) * fs * 0.72:.0f}" height="26" fill="#b3312a"/>'
            f'<text x="8" y="19" font-family="Arial, sans-serif" font-size="{fs}" font-weight="800" fill="#ffffff">{label}</text>'
            f'<rect x="0" y="{h - 15}" width="{12 + len(chip) * 6.0:.0f}" height="15" fill="#14202b"/>'
            f'<text x="5" y="{h - 4}" font-size="8.5" font-weight="700" fill="#ffffff">{chip}</text></svg>')

def art_cop31(h):
    return banner("COP31: OVERTIME", "#dcebe2",
        '<circle cx="70" cy="58" r="21" fill="#7fb069"/><path d="M52 50 q18 -12 36 0 q-6 16 -18 20 q-12 -4 -18 -20" fill="#5b8c5a"/>'
        '<rect x="128" y="36" width="10" height="34" rx="5" fill="#e8e3d5" stroke="#8c2f26" stroke-width="2"/><circle cx="133" cy="74" r="8" fill="#b3312a"/>'
        '<circle cx="196" cy="56" r="19" fill="none" stroke="#33506e" stroke-width="3"/><path d="M196 44 v12 l9 6" stroke="#33506e" stroke-width="3" fill="none"/>'
        '<text x="238" y="62" font-size="15" font-weight="800" fill="#8c4a12">DAY 13</text>',
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
    return banner("KYIV: THE BRIDGE", "#16283d",
        '<path d="M10 52 Q150 26 290 52" stroke="#7fa6c9" stroke-width="3" fill="none"/>'
        '<path d="M60 44 L60 60 M150 38 L150 60 M240 44 L240 60" stroke="#7fa6c9" stroke-width="2.6"/>'
        '<circle cx="212" cy="42" r="5" fill="#ff8a3c"/>',
        "3RD HIT IN 4 DAYS", h, 13)

def art_hormuz(h):
    return banner("HORMUZ: DRONE", "#bcd6e4",
        '<path d="M0 54 h300 v42 H0z" fill="#5b84a3"/><path d="M96 54 l14 -12 h52 l10 12 z" fill="#33506e"/><rect x="118" y="32" width="30" height="10" fill="#b3312a"/>'
        '<path d="M238 30 l16 6 -16 6 -4 -6z" fill="#14202b"/><circle cx="242" cy="48" r="2.6" fill="#b3312a"/>',
        "IRAN'S CLAIM · UNCONFIRMED", h, 13)

def art_rout(h):
    return banner("AI ROUT: -3.7%", "#22161a",
        '<path d="M16 66 L70 58 L118 62 L168 74 L220 80 L284 90" stroke="#e5484d" stroke-width="3" fill="none"/>'
        '<text x="164" y="52" font-family="Arial, sans-serif" font-size="11" font-weight="800" fill="#7be3a8">$2 TRILLION DEBUT</text>',
        "S&P AND DOW IN CORRECTION", h, 13)

def art_icj(h):
    cols = "".join(f'<rect x="{52+i*30}" y="40" width="11" height="26" fill="#5b7186"/>' for i in range(6))
    return banner("MYANMAR: GENOCIDE", "#e8edf2",
        f'<path d="M40 40 L140 24 L240 40 Z" fill="#33506e"/><rect x="40" y="66" width="200" height="5" fill="#33506e"/>{cols}',
        "WORLD COURT RULING", h, 13)

def art_peace(h):
    return banner("PEACE TEXT", "#f3e5cf",
        '<rect x="30" y="34" width="52" height="26" fill="#3c3b6e"/><rect x="116" y="34" width="52" height="26" fill="#de2910"/><circle cx="129" cy="43" r="5" fill="#ffde00"/>'
        '<rect x="202" y="34" width="52" height="26" fill="#2a4d9b"/><rect x="202" y="42" width="52" height="9" fill="#ffffff"/><rect x="202" y="51" width="52" height="9" fill="#d52b1e"/>',
        "SILENT ON UKRAINE", h, 13)

def art_gaza(h):
    return banner("GAZA: STRIKES", "#d9d3c3",
        '<rect x="30" y="42" width="26" height="30" fill="#8a8378"/><rect x="66" y="34" width="22" height="38" fill="#6f6a5e"/><rect x="98" y="46" width="30" height="26" fill="#8a8378"/>'
        '<path d="M210 34 q10 14 2 26" stroke="#555" stroke-width="3" fill="none"/><circle cx="212" cy="66" r="4" fill="#b3312a"/>',
        "DESPITE THE PEACE DEAL", h, 13)

def art_yongbyon(h):
    return banner("YONGBYON GROWS", "#dfe5da",
        '<rect x="120" y="30" width="14" height="38" fill="#7a6a4a"/><path d="M112 30 h30 l-4 -10 h-22z" fill="#555f6a"/>'
        '<rect x="30" y="52" width="60" height="16" fill="#a8b39a"/><rect x="196" y="48" width="70" height="20" fill="#a8b39a"/>'
        '<path d="M0 72 h300" stroke="#555f6a" stroke-width="2" stroke-dasharray="6 4"/>',
        "UN WATCHDOG REPORT", h, 13)

def art_genz(h):
    heads = "".join(f'<circle cx="{40+i*26}" cy="58" r="7" fill="#33506e"/>' for i in range(9))
    signs = '<rect x="70" y="30" width="34" height="16" fill="#fdfaf1" stroke="#b3312a" stroke-width="1.6"/><rect x="188" y="28" width="34" height="16" fill="#fdfaf1" stroke="#33506e" stroke-width="1.6"/>'
    return banner("GEN Z: 25 COUNTRIES", "#f0e6d2", heads + signs,
        "EUROPE MARCHES", h, 13)

def art_greenland(h):
    return banner("GREENLAND: 109-0", "#dcebf2",
        '<path d="M0 74 L60 52 L120 68 L190 46 L300 66 L300 96 L0 96 Z" fill="#fdfefe"/>'
        '<rect x="140" y="30" width="4" height="30" fill="#7a6a4a"/><path d="M144 30 h26 l-6 6 6 6 h-26z" fill="#2a4d9b"/>'
        '<rect x="196" y="34" width="4" height="26" fill="#7a6a4a"/><path d="M200 34 h24 l-5 5 5 5 h-24z" fill="#b3312a"/>',
        "US SECURITY DEAL SIGNED", h, 13)

def art_pill(h):
    return banner("CANCER PILL", "#e9f4ee",
        '<g transform="rotate(-24 70 52)"><rect x="30" y="38" width="80" height="28" rx="14" fill="#2e7d5b"/><rect x="70" y="38" width="40" height="28" rx="14" fill="#f2f2f2" stroke="#2e7d5b" stroke-width="2"/></g>'
        '<text x="148" y="50" font-size="17" font-weight="800" fill="#1d5c40">1 IN 12</text>',
        "NO TUMOUR FOUND ON SCANS", h, 13)

LEAD_ARTS = {1: art_cop31, 2: art_saudi, 3: art_peru}
FEAT_ARTS = {4: art_bridge, 5: art_hormuz, 6: art_rout, 7: art_icj, 8: art_peace,
             9: art_gaza, 10: art_yongbyon, 11: art_genz, 12: art_greenland, 13: art_pill}

# -------------------------------------------------------------------- css
CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1024px; height:1024px; overflow:hidden; background:#f7f1e3;
  font-family: Georgia, 'Times New Roman', serif; color:#14202b; padding:10px 18px 6px; }
.kicker { display:flex; justify-content:space-between; font-family: Arial, sans-serif;
  font-size:10.5px; font-weight:700; letter-spacing:2.2px; color:#8c2f26;
  border-bottom:2.5px solid #14202b; padding-bottom:4px; }
h1 { text-align:center; font-size:46px; letter-spacing:0.5px; line-height:1.02; margin-top:4px; }
.subline { text-align:center; font-style:italic; font-size:14.5px; margin-top:3px; color:#33506e; }
.nums { display:flex; gap:0; margin-top:8px; border-top:1px solid #b9a888; border-bottom:1px solid #b9a888; }
.num { flex:1; padding:4px 8px 5px; border-left:3.5px solid #b3312a; }
.num + .num { border-left:3.5px solid #b3312a; margin-left:10px; }
.num b { font-size:21px; display:block; line-height:1.05; }
.num span { font-size:8.8px; font-family: Arial, sans-serif; line-height:1.15; display:block; }
.regionbar { display:flex; margin-top:6px; font-family: Arial, sans-serif; }
.regionbar div { color:#fff; font-size:9px; overflow:hidden; white-space:nowrap; font-weight:700; text-align:center; padding:3px 0; }
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
.src { font-family: Arial, sans-serif; font-size:8px; color:#555f6a; margin-top:3px; letter-spacing:0.6px; }
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

def card_lead(s):
    return (f'<div class="card lead">{LEAD_ARTS[s["n"]](96)}'
            f'<div class="place"><b>{s["n"]}</b>{s["place"]} · {s["cat"]}</div>'
            f'<h3>{s["head"]}</h3><p>{s["body"]}</p>'
            f'<div class="src">{s["src"]}</div></div>')

def card_feat(s):
    return (f'<div class="card feat">{FEAT_ARTS[s["n"]](66)}'
            f'<div class="place"><b>{s["n"]}</b>{s["place"]} · {s["cat"]}</div>'
            f'<h3>{s["head"]}</h3><p>{s["body"]}</p></div>')

def build():
    counts = {}
    for s in LEADS + FEATURES:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    for _, rg, _ in BRIEFS:
        counts[rg] = counts.get(rg, 0) + 1
    total = sum(counts.values())
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
<div class="kicker"><span>THE WORLD IN ONE DAY</span><span>{total} STORIES · {len([1 for c in counts if counts[c]])} REGIONS · EVERY ONE REPORTED SATURDAY 21 NOVEMBER 2026</span></div>
<h1>Saturday 21 November 2026</h1>
<div class="subline">Climate summit runs past its deadline · Three missiles shot down over Riyadh · Strong quake shakes Peru</div>
<div class="nums">{nums}</div>
<div class="regionbar">{regionbar}</div>
<div class="row">{leads}</div>
<div class="row">{feats1}</div>
<div class="row">{feats2}</div>
<div class="row">
  <div class="mapbox"><div class="place">WHERE IT HAPPENED</div>{worldmap.render_map()}
  <div class="legend">Each number is the story with that number on this page. Pins sit where the story happened; crowded labels are lifted clear on leader lines.</div></div>
  <div class="briefs"><div class="place">ALSO ON SATURDAY 21 NOVEMBER 2026 · {len(BRIEFS)} MORE STORIES</div>
  <div class="briefcols"><div class="briefcol">{col1}</div><div class="briefcol">{col2}</div></div></div>
</div>
<div class="footer">
<div class="datecheck"><b>DATE CHECK</b> · Every story above was reported on Saturday 21 November 2026 in at least one time zone. The Peru quake struck at 00:09 UTC on Saturday and the Riyadh missiles after 2am local time. The Shenzhen leaders met on Thursday; only their declaration, issued Saturday, is printed. Unconfirmed claims are labelled as claims.</div>
<div class="credit">Drawn and set in one page from Saturday's reporting (AP, Reuters, AFP, BBC, Al Jazeera, USGS, IGP, Indeci, CoinGecko). No photographs: every scene is an original drawing.</div>
</div>
</body></html>"""
    (HERE / "poster.html").write_text(html, encoding="utf-8")
    print("poster.html written:", len(html), "bytes;", total, "stories; regions:", counts)

if __name__ == "__main__":
    build()
