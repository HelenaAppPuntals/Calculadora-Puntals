"""
=============================================================================
APP WEB — CALCULADORA DE PUNTALS  (TFG + VENT IAP-11)
Helena Maymí Ardèvol · Facultat de Nàutica de Barcelona · UPC
=============================================================================
Per executar:
    streamlit run app_puntals.py

Els fitxers Logo_UPC.png i escut.png han d'estar a la mateixa carpeta.
=============================================================================
"""

import math
import streamlit as st

# ── Configuració de la pàgina ──
st.set_page_config(
    page_title="Calculadora de Puntals",
    page_icon="",
    layout="centered"
)

# ── CSS tècnic amb color ──
st.markdown("""
<style>
    * { font-family: 'Georgia', 'Times New Roman', Times, serif !important; }
    .stApp { background: linear-gradient(160deg, #07111f 0%, #0a1c35 60%, #0c1a2e 100%) !important; }
    h1, h2, h3 { color: #e8f2ff !important; letter-spacing: 0.03em; }
    p, label, div, span, .stMarkdown { color: #b8cfe8 !important; }
    .stMetric label { color: #7ec8c8 !important; font-size: 11px !important; letter-spacing: 0.07em; text-transform: uppercase; }
    .stMetric [data-testid="stMetricValue"] { color: #f0d080 !important; font-size: 2.2rem !important; }
    .stMetric [data-testid="metric-container"] {
        background: linear-gradient(135deg, #0d2040 0%, #102848 100%) !important;
        border: 1px solid #2a5a8a !important;
        border-top: 2px solid #7ec8c8 !important;
        border-radius: 4px !important;
        padding: 14px 12px !important;
    }
    .stSelectbox label, .stNumberInput label { color: #7ec8c8 !important; font-size: 12px !important; letter-spacing: 0.05em; text-transform: uppercase; }
    .stSelectbox [data-baseweb="select"] span,
    .stSelectbox [data-baseweb="select"] div { color: #f0d080 !important; font-family: Georgia, serif !important; }
    div[data-baseweb="select"] > div { background-color: #0d2040 !important; border: 1px solid #2a5a8a !important; }
    hr { border-color: #1a3a5a !important; }
    .stButton > button {
        background: linear-gradient(90deg, #0f2a50 0%, #1a3a6a 50%, #0f2a50 100%) !important;
        color: #f0d080 !important;
        border: 1px solid #c8a840 !important;
        border-radius: 3px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        letter-spacing: 0.18em !important;
        text-transform: uppercase !important;
        padding: 14px !important;
    }
    .stButton > button:hover { background: linear-gradient(90deg, #1a3a6a 0%, #2a5a9a 50%, #1a3a6a 100%) !important; border-color: #e0c060 !important; }
    .stExpander summary, details summary { font-family: Georgia, serif !important; color: #7ec8c8 !important; letter-spacing: 0.04em; }
    .stExpander { border: 1px solid #1a3a5a !important; border-left: 3px solid #7ec8c8 !important; border-radius: 3px !important; background-color: #0a1828 !important; }
    .stAlert { border-radius: 3px !important; }
    .footer { text-align: center; color: #3a5a7a; font-size: 11px; margin-top: 30px; padding-top: 15px; border-top: 1px solid #1a3a5a; letter-spacing: 0.04em; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# TEXTOS MULTIIDIOMA
# ─────────────────────────────────────────────────────────────────────────────

TEXTOS = {
    "CA": {
        "titol": "Calculadora de Puntals de Varada",
        "subtitol": "Helena Maymí Ardèvol · Facultat de Nàutica de Barcelona · UPC",
        "descripcio": "Càlcul del nombre mínim de puntals per varar una embarcació d'esbarjo considerant el pes propi (ISO 12215-5) i l'acció del vent (IAP-11).",
        "dades": " Dades de l'embarcació",
        "lwl": "Lwl — Eslora en la flotació (m)",
        "bc": "Bc — Mànega al pantoc (m)",
        "t": "T — Calat (m)",
        "tipus": "Tipus d'embarcació",
        "potencia": "Potència del motor (kW)",
        "motora": "MOTORA", "veler": "VELER",
        "calcular": "️ Calcular",
        "resultats": " Resultats",
        "ntfg": "Puntals sense vent",
        "ntfm": "Puntals amb vent",
        "increment": "Increment pel vent",
        "dmin": "Distància mínima",
        "correcte": " CORRECTE — Els puntals caben dins la mànega del vaixell.",
        "atencio": "️ ATENCIÓ — d_min supera B/2. Revisar la distribució dels puntals.",
        "recomanacio": " Recomanació: Col·locar els puntals a ≥ {dmin:.2f} m del centre, idealment tan a prop de B/2 = {bmig:.2f} m com sigui possible.",
        "detall": " Veure detall dels càlculs",
        "diagrama": " Diagrama esquemàtic",
        "costat_barlot": "Barlovent",
        "costat_sotav": "Sotavent",
        "centre": "Centre",
        "vent": "VENT →",
        "peu_diagrama": "Vista frontal de l'embarcació varada. Els puntals (en verd) han d'estar a ≥ d_min del centre.",
        "ajuda_lwl": "Longitud mesurada a la línia de flotació",
        "ajuda_bc": "Amplada a la part més ampla del fons",
        "ajuda_t": "Profunditat sota la línia de flotació",
        "ajuda_tipus": "Selecciona el tipus d'embarcació",
        "ajuda_potencia": "Només necessari per a motores",
        "footer": "Calculadora desenvolupada per Helena Maymí Ardèvol · TFM · Facultat de Nàutica de Barcelona · UPC · 2026 · Basat en ISO 12215-5 i IAP-11",
    },
    "ES": {
        "titol": "Calculadora de Puntales de Varada",
        "subtitol": "Helena Maymí Ardèvol · Facultad de Náutica de Barcelona · UPC",
        "descripcio": "Cálculo del número mínimo de puntales para varar una embarcación de recreo considerando el peso propio (ISO 12215-5) y la acción del viento (IAP-11).",
        "dades": " Datos de la embarcación",
        "lwl": "Lwl — Eslora en la flotación (m)",
        "bc": "Bc — Manga en el pantoque (m)",
        "t": "T — Calado (m)",
        "tipus": "Tipo de embarcación",
        "potencia": "Potencia del motor (kW)",
        "motora": "MOTORA", "veler": "VELERO",
        "calcular": "️ Calcular",
        "resultats": " Resultados",
        "ntfg": "Puntales sin viento",
        "ntfm": "Puntales con viento",
        "increment": "Incremento por viento",
        "dmin": "Distancia mínima",
        "correcte": " CORRECTO — Los puntales caben dentro de la manga del barco.",
        "atencio": "️ ATENCIÓN — d_min supera B/2. Revisar la distribución de los puntales.",
        "recomanacio": " Recomendación: Colocar los puntales a ≥ {dmin:.2f} m del centro, idealmente tan cerca de B/2 = {bmig:.2f} m como sea posible.",
        "detall": " Ver detalle de los cálculos",
        "diagrama": " Diagrama esquemático",
        "costat_barlot": "Barlovento",
        "costat_sotav": "Sotavento",
        "centre": "Centro",
        "vent": "VIENTO →",
        "peu_diagrama": "Vista frontal de la embarcación varada. Los puntales (en verde) deben estar a ≥ d_min del centro.",
        "ajuda_lwl": "Longitud medida en la línea de flotación",
        "ajuda_bc": "Anchura en la parte más ancha del fondo",
        "ajuda_t": "Profundidad bajo la línea de flotación",
        "ajuda_tipus": "Selecciona el tipo de embarcación",
        "ajuda_potencia": "Solo necesario para motoras",
        "footer": "Calculadora desarrollada por Helena Maymí Ardèvol · TFM · Facultad de Náutica de Barcelona · UPC · 2026 · Basado en ISO 12215-5 e IAP-11",
    },
    "EN": {
        "titol": "Boat Docking Support Calculator",
        "subtitol": "Helena Maymí Ardèvol · Faculty of Nautical Sciences of Barcelona · UPC",
        "descripcio": "Minimum number of supports to safely dock a recreational boat considering self-weight (ISO 12215-5) and wind action (IAP-11).",
        "dades": " Vessel Data",
        "lwl": "Lwl — Waterline length (m)",
        "bc": "Bc — Chine beam (m)",
        "t": "T — Draft (m)",
        "tipus": "Vessel type",
        "potencia": "Engine power (kW)",
        "motora": "MOTORBOAT", "veler": "SAILBOAT",
        "calcular": "️ Calculate",
        "resultats": " Results",
        "ntfg": "Supports without wind",
        "ntfm": "Supports with wind",
        "increment": "Wind increment",
        "dmin": "Minimum distance",
        "correcte": " CORRECT — Supports fit within the vessel's beam.",
        "atencio": "️ WARNING — d_min exceeds B/2. Review support distribution.",
        "recomanacio": " Recommendation: Place supports at ≥ {dmin:.2f} m from centre, ideally as close to B/2 = {bmig:.2f} m as possible.",
        "detall": " View calculation detail",
        "diagrama": " Schematic diagram",
        "costat_barlot": "Windward",
        "costat_sotav": "Leeward",
        "centre": "Centre",
        "vent": "WIND →",
        "peu_diagrama": "Front view of the docked vessel. Supports (in green) must be at ≥ d_min from centre.",
        "ajuda_lwl": "Length measured at the waterline",
        "ajuda_bc": "Width at the widest part of the bottom",
        "ajuda_t": "Depth below the waterline",
        "ajuda_tipus": "Select vessel type",
        "ajuda_potencia": "Only required for motorboats",
        "footer": "Calculator developed by Helena Maymí Ardèvol · TFM · Faculty of Nautical Sciences of Barcelona · UPC · 2026 · Based on ISO 12215-5 and IAP-11",
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# CAPÇALERA AMB LOGOS I SELECTOR D'IDIOMA
# ─────────────────────────────────────────────────────────────────────────────

idioma = st.selectbox("", ["CA", "ES", "EN"], label_visibility="collapsed")
st.markdown("""
<style>
    /* Valor dels selects visible en blau clar */
    [data-baseweb="select"] [data-testid="stMarkdownContainer"] p,
    [data-baseweb="select"] span { color: #4a9ad4 !important; font-weight: bold !important; }
    div[data-baseweb="select"] > div { 
        background-color: #0f1e36 !important; 
        border: 1px solid #2a5a9a !important;
        color: #4a9ad4 !important;
    }
</style>
""", unsafe_allow_html=True)
T_ = TEXTOS[idioma]
st.markdown(f"""
<div style='text-align:center; padding:16px 0 10px 0; border-bottom: 1px solid #1a3a5a; margin-bottom: 8px;'>
    <div style='width:60px; height:2px; background:linear-gradient(90deg,#7ec8c8,#f0d080); margin:0 auto 12px auto;'></div>
    <span style='font-size:30px; font-weight:bold; color:#f0d080; font-family: Georgia, serif; letter-spacing:0.05em;'>
        {T_['titol']}
    </span><br>
    <span style='font-size:11px; color:#4a8aaa; letter-spacing:0.1em; text-transform:uppercase;'>{T_['subtitol']}</span>
    <div style='width:60px; height:2px; background:linear-gradient(90deg,#f0d080,#7ec8c8); margin:12px auto 0 auto;'></div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f"<p style='text-align:center;color:#a0b8d8;font-size:13px;margin-top:5px;'>"
    f"{T_['descripcio']}</p>",
    unsafe_allow_html=True
)
st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# BLOC 1 · DADES D'ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

st.subheader(T_["dades"])

col1, col2 = st.columns(2)
with col1:
    Lwl = st.number_input(T_["lwl"], min_value=2.5, max_value=24.5,
                          value=12.35, step=0.01, help=T_["ajuda_lwl"])
    Bc  = st.number_input(T_["bc"],  min_value=1.0, max_value=10.0,
                          value=4.20,  step=0.01, help=T_["ajuda_bc"])
    T   = st.number_input(T_["t"],   min_value=0.3, max_value=5.0,
                          value=2.10,  step=0.01, help=T_["ajuda_t"])
with col2:
    tipus_sel = st.selectbox(T_["tipus"],
                             options=[T_["motora"], T_["veler"]],
                             index=1, help=T_["ajuda_tipus"])
    tipus = "MOTORA" if tipus_sel == T_["motora"] else "VELER"
    Potencia = st.number_input(T_["potencia"], min_value=0.0, max_value=5000.0,
                               value=29.44, step=1.0,
                               help=T_["ajuda_potencia"])

st.divider()

# ─────────────────────────────────────────────────────────────────────────────
# CÀLCULS
# ─────────────────────────────────────────────────────────────────────────────

if st.button(T_["calcular"], type="primary", use_container_width=True):

    # Constants
    Beta_04 = 30; x_Lwl = 0.6; Gz_max60 = 60; Cb = 0.23
    dens_as = 1.025; Kdc = 1.0; beta_coef = 0.1838
    eta_motora = 0.10; eta_veler = 0.23

    # Bloc 3
    mLDC = max(0.0, 1369 * Lwl - 7223.1)
    z = (2/3) * T;  b = Lwl / 4;  h = z / 2
    AD = min(b * b * 1e-6, 2.5 * b**2 * 1e-6)
    V = (0.0035 * Potencia + 14.516) if tipus == "MOTORA" else (2.36 * math.sqrt(Lwl))
    nCG_eq1 = 0.32 * ((Lwl/(10*Bc))+0.084) * (50-Beta_04) * ((V**2*Bc**2)/mLDC)
    nCG = nCG_eq1 if nCG_eq1 <= 3 else (0.5 * V / (mLDC**0.17))
    nCG = max(3.0, min(7.0, nCG))
    KL   = min(1.0, ((1-0.167*nCG)/0.6)*x_Lwl + 0.167*nCG)
    kR   = 1.0 if tipus == "MOTORA" else min(1.0, 1.5 - 3e-4*b)
    KAR  = kR * 0.1 * (mLDC**0.15) / (AD**0.3)
    Kz   = (z - h) / z
    KSLS = max(1.0, ((10*Gz_max60*(Lwl**0.5))/(mLDC**0.33))**0.5)
    PBM_min = 0.45*mLDC**0.33 + 0.9*Lwl*Kdc
    PSM_min = 0.9*Lwl*Kdc
    PBMD_base = 2.4*mLDC**0.33 + 20
    PBMD  = max(PBMD_base*KAR*Kdc*KL, PBM_min)
    PBMP_base = 0.1*mLDC/(Lwl*Bc)*(1+Kdc**0.5*nCG)
    PBMP  = max(PBMP_base*KAR*KL, PBM_min)
    PDM_base = 0.35*Lwl + 14.6
    PSMD  = max((PDM_base+Kz*(PBMD_base-PDM_base))*KAR*Kdc*KL, PSM_min)
    PSMP  = max((PDM_base+Kz*(0.25*PBMP_base-PDM_base))*KAR*Kdc*KL, PSM_min)
    PBS_base = (2*mLDC**0.33+18)*KSLS
    PBS_min  = 0.35*mLDC**0.33 + 1.4*Lwl*Kdc
    PBS  = max(PBS_base*KAR*Kdc*KL, PBS_min)
    PDS_base = 0.55*mLDC**0.33 + 12
    PSS_min  = 1.4*Lwl*Kdc
    PSS  = max((PDS_base+Kz*(PBS_base-PDS_base))*KAR*Kdc*KL, PSS_min)
    P_disseny = max(PBMD,PBMP,PSMD,PSMP) if tipus=="MOTORA" else max(PBS,PSS)
    F_limit = beta_coef * P_disseny * b**2
    Delta   = Lwl * Bc * T * Cb * dens_as * 1000

    # Bloc 4
    K = 0.2; T_ret = 10; kr_vent = 0.156; z0 = 0.003; z_min = 1.0; cf = 1.65
    c_prob = (((1-K*math.log(-math.log(1-1/T_ret))) /
               (1-K*math.log(-math.log(0.98))))**0.5)
    v_bT  = 29.0 * c_prob
    H_exp = Bc / 2;  A_ref = Lwl * H_exp;  h_cp = H_exp / 2
    z_ce  = max(h_cp, z_min)
    ce    = kr_vent**2 * math.log(z_ce/z0)**2 * (1 + 7*kr_vent/math.log(z_ce/z0))
    F_w   = 0.5 * 1.25 * v_bT**2 * ce * cf * A_ref
    M_w   = F_w * h_cp
    terme_vent = 2 * M_w / Bc

    # Bloc 5
    eta   = eta_motora if tipus == "MOTORA" else eta_veler
    N_TFG = math.ceil((Delta*9.81*eta) / F_limit)
    N_TFM = math.ceil((Delta*9.81*eta + terme_vent) / F_limit)
    Delta_N = N_TFM - N_TFG

    # Bloc 6
    d_min   = M_w / (F_limit * (N_TFM / 2))
    B_mig   = Bc / 2
    ok_geom = d_min <= B_mig

    # ── Resultats principals ──
    st.subheader(T_["resultats"])

    st.markdown(f"""
    <div style='display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:12px; margin:16px 0;'>
        <div style='background:linear-gradient(135deg,#0d2040,#102848); border:1px solid #2a5a8a; border-top:2px solid #7ec8c8; border-radius:4px; padding:14px 12px;'>
            <div style='color:#7ec8c8; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>{T_["ntfg"]}</div>
            <div style='color:#f0d080; font-size:2.2rem; font-weight:bold;'>{N_TFG}</div>
            <div style='color:#4a7aaa; font-size:10px; margin-top:4px;'>ISO 12215-5</div>
        </div>
        <div style='background:linear-gradient(135deg,#0d2040,#102848); border:1px solid #2a5a8a; border-top:2px solid #e07040; border-radius:4px; padding:14px 12px;'>
            <div style='color:#e07040; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>{T_["ntfm"]}</div>
            <div style='color:#f0d080; font-size:2.2rem; font-weight:bold;'>{N_TFM}</div>
            <div style='color:#4a7aaa; font-size:10px; margin-top:4px;'>+{Delta_N} IAP-11</div>
        </div>
        <div style='background:linear-gradient(135deg,#0d2040,#102848); border:1px solid #2a5a8a; border-top:2px solid #a078d8; border-radius:4px; padding:14px 12px;'>
            <div style='color:#a078d8; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>{T_["increment"]}</div>
            <div style='color:#f0d080; font-size:2.2rem; font-weight:bold;'>{Delta_N}</div>
            <div style='color:#4a7aaa; font-size:10px; margin-top:4px;'>puntals extra</div>
        </div>
        <div style='background:linear-gradient(135deg,#0d2040,#102848); border:1px solid #2a5a8a; border-top:2px solid #60c890; border-radius:4px; padding:14px 12px;'>
            <div style='color:#60c890; font-size:10px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:6px;'>{T_["dmin"]}</div>
            <div style='color:#f0d080; font-size:2.2rem; font-weight:bold;'>{d_min:.2f}</div>
            <div style='color:#4a7aaa; font-size:10px; margin-top:4px;'>metres</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if ok_geom:
        st.success(T_["correcte"])
    else:
        st.error(T_["atencio"])
    st.info(T_["recomanacio"].format(dmin=d_min, bmig=B_mig))





# ── Footer ──
st.divider()
st.markdown(f"<div class='footer'>{T_['footer']}</div>", unsafe_allow_html=True)
