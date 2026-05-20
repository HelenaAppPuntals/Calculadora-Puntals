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
    page_icon="⚓",
    layout="centered"
)

# ── CSS fosc nàutic ──
st.markdown("""
<style>
    .stApp { background-color: #0a1628 !important; }
    section[data-testid="stMain"] { background-color: #0a1628 !important; }
    .stApp * { color: #e8edf5; }
    h1, h2, h3 { color: #ffffff !important; font-family: 'Georgia', serif; }
    label, .stSelectbox label, .stNumberInput label {
        color: #a8b8d0 !important; font-size: 13px !important;
    }
    .stButton > button {
        background-color: #1a56db !important;
        color: white !important;
        border-radius: 8px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 12px !important;
        border: none !important;
        width: 100% !important;
    }
    .stButton > button:hover { background-color: #2563eb !important; }
    .stNumberInput input, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #111 !important;
        border-radius: 6px !important;
    }
    .stAlert { border-radius: 8px !important; }
    .footer {
        text-align: center; color: #6b7a99; font-size: 11px;
        margin-top: 30px; padding-top: 15px; border-top: 1px solid #1e3a5f;
    }
    hr { border-color: #1e3a5f !important; }
    .stMetric { background-color: #0f2040 !important; border-radius: 8px; padding: 8px; }
    .stExpanderHeader { color: #a8b8d0 !important; }
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
        "dades": "📋 Dades de l'embarcació",
        "lwl": "Lwl — Eslora en la flotació (m)",
        "bc": "Bc — Mànega al pantoc (m)",
        "t": "T — Calat (m)",
        "tipus": "Tipus d'embarcació",
        "potencia": "Potència del motor (kW)",
        "motora": "MOTORA", "veler": "VELER",
        "calcular": "⚙️ Calcular",
        "resultats": "📊 Resultats",
        "ntfg": "Puntals sense vent",
        "ntfm": "Puntals amb vent",
        "increment": "Increment pel vent",
        "dmin": "Distància mínima",
        "correcte": "✅ CORRECTE — Els puntals caben dins la mànega del vaixell.",
        "atencio": "⚠️ ATENCIÓ — d_min supera B/2. Revisar la distribució dels puntals.",
        "recomanacio": "💡 **Recomanació:** Col·locar els puntals a ≥ {dmin:.2f} m del centre, idealment tan a prop de B/2 = {bmig:.2f} m com sigui possible.",
        "detall": "🔍 Veure detall dels càlculs",
        "diagrama": "📐 Diagrama esquemàtic",
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
        "footer": "Calculadora desenvolupada per Helena Maymí Ardèvol · TFM · Facultat de Nàutica de Barcelona · UPC · 2024 · Basat en ISO 12215-5 i IAP-11",
        "error_rang": "⚠️ **Dades fora de rang** — Amb Lwl = {lwl:.2f} m, la massa de desplaçament estimada per la ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) resulta zero o negativa. La normativa requereix una eslora mínima d'aproximadament **5.27 m** per poder aplicar aquesta metodologia. Reviseu les dades introduïdes.",
    },
    "ES": {
        "titol": "Calculadora de Puntales de Varada",
        "subtitol": "Helena Maymí Ardèvol · Facultad de Náutica de Barcelona · UPC",
        "descripcio": "Cálculo del número mínimo de puntales para varar una embarcación de recreo considerando el peso propio (ISO 12215-5) y la acción del viento (IAP-11).",
        "dades": "📋 Datos de la embarcación",
        "lwl": "Lwl — Eslora en la flotación (m)",
        "bc": "Bc — Manga en el pantoque (m)",
        "t": "T — Calado (m)",
        "tipus": "Tipo de embarcación",
        "potencia": "Potencia del motor (kW)",
        "motora": "MOTORA", "veler": "VELERO",
        "calcular": "⚙️ Calcular",
        "resultats": "📊 Resultados",
        "ntfg": "Puntales sin viento",
        "ntfm": "Puntales con viento",
        "increment": "Incremento por viento",
        "dmin": "Distancia mínima",
        "correcte": "✅ CORRECTO — Los puntales caben dentro de la manga del barco.",
        "atencio": "⚠️ ATENCIÓN — d_min supera B/2. Revisar la distribución de los puntales.",
        "recomanacio": "💡 **Recomendación:** Colocar los puntales a ≥ {dmin:.2f} m del centro, idealmente tan cerca de B/2 = {bmig:.2f} m como sea posible.",
        "detall": "🔍 Ver detalle de los cálculos",
        "diagrama": "📐 Diagrama esquemático",
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
        "footer": "Calculadora desarrollada por Helena Maymí Ardèvol · TFM · Facultad de Náutica de Barcelona · UPC · 2024 · Basado en ISO 12215-5 e IAP-11",
        "error_rang": "⚠️ **Datos fuera de rango** — Con Lwl = {lwl:.2f} m, la masa de desplazamiento estimada por la ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) resulta cero o negativa. La normativa requiere una eslora mínima de aproximadamente **5.27 m** para aplicar esta metodología. Revisad los datos introducidos.",
    },
    "EN": {
        "titol": "Boat Docking Support Calculator",
        "subtitol": "Helena Maymí Ardèvol · Faculty of Nautical Sciences of Barcelona · UPC",
        "descripcio": "Minimum number of supports to safely dock a recreational boat considering self-weight (ISO 12215-5) and wind action (IAP-11).",
        "dades": "📋 Vessel Data",
        "lwl": "Lwl — Waterline length (m)",
        "bc": "Bc — Chine beam (m)",
        "t": "T — Draft (m)",
        "tipus": "Vessel type",
        "potencia": "Engine power (kW)",
        "motora": "MOTORBOAT", "veler": "SAILBOAT",
        "calcular": "⚙️ Calculate",
        "resultats": "📊 Results",
        "ntfg": "Supports without wind",
        "ntfm": "Supports with wind",
        "increment": "Wind increment",
        "dmin": "Minimum distance",
        "correcte": "✅ CORRECT — Supports fit within the vessel's beam.",
        "atencio": "⚠️ WARNING — d_min exceeds B/2. Review support distribution.",
        "recomanacio": "💡 **Recommendation:** Place supports at ≥ {dmin:.2f} m from centre, ideally as close to B/2 = {bmig:.2f} m as possible.",
        "detall": "🔍 View calculation detail",
        "diagrama": "📐 Schematic diagram",
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
        "footer": "Calculator developed by Helena Maymí Ardèvol · TFM · Faculty of Nautical Sciences of Barcelona · UPC · 2024 · Based on ISO 12215-5 and IAP-11",
        "error_rang": "⚠️ **Data out of range** — With Lwl = {lwl:.2f} m, the displacement mass estimated by ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) is zero or negative. The standard requires a minimum waterline length of approximately **5.27 m** to apply this methodology. Please review the input data.",
    }
}

# ─────────────────────────────────────────────────────────────────────────────
# CAPÇALERA AMB LOGOS I SELECTOR D'IDIOMA
# ─────────────────────────────────────────────────────────────────────────────

# ── Selector d'idioma ──
st.markdown("""
<style>
    div[data-testid="stSelectbox"]:first-of-type div[data-baseweb="select"] > div {
        background-color: #1a3a7a !important;
        color: #ffffff !important;
        border: 1px solid #2a5090 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stSelectbox"]:first-of-type svg { fill: #ffffff !important; }
</style>
""", unsafe_allow_html=True)
idioma = st.selectbox("", ["CA", "ES", "EN"], label_visibility="collapsed")
T_ = TEXTOS[idioma]

# ── Header fosc amb etiquetes ──
st.markdown(f"""
<div style="background: linear-gradient(135deg, #0f2554 0%, #1a3a7a 100%);
            border-radius: 12px; padding: 28px 32px; margin-bottom: 24px;
            border: 1px solid #1e4080;">
    <p style="color:#7eb3e8; font-size:11px; font-weight:600;
              letter-spacing:2px; margin:0 0 8px 0;">NÀUTICA · UPC</p>
    <h1 style="color:#ffffff !important; font-size:28px; font-weight:800;
               margin:0 0 6px 0; font-family:'Georgia',serif;">
        {T_['titol']}
    </h1>
    <p style="color:#a8c4e0; font-size:13px; margin:0 0 12px 0;">
        {T_['subtitol']}
    </p>
    <p style="color:#c8d8ea; font-size:13px; margin:0 0 16px 0;">
        {T_['descripcio']}
    </p>
    <span style="background:#1a4080; color:#7eb3e8; border:1px solid #2a5090;
                 border-radius:20px; padding:4px 12px; font-size:11px;
                 font-weight:600; margin-right:8px;">ISO 12215-5</span>
    <span style="background:#1a4080; color:#7eb3e8; border:1px solid #2a5090;
                 border-radius:20px; padding:4px 12px; font-size:11px;
                 font-weight:600; margin-right:8px;">IAP-11</span>
    <span style="background:#1a4080; color:#7eb3e8; border:1px solid #2a5090;
                 border-radius:20px; padding:4px 12px; font-size:11px;
                 font-weight:600;">TFM 2024</span>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# BLOC 1 · DADES D'ENTRADA
# ─────────────────────────────────────────────────────────────────────────────

st.markdown(f"<p style='color:#7eb3e8; font-size:11px; font-weight:600; letter-spacing:2px; margin:0 0 12px 0;'>{T_['dades'].replace('📋 ', '').upper()}</p>", unsafe_allow_html=True)

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
                               disabled=(tipus == "VELER"),
                               help=T_["ajuda_potencia"])

st.markdown("<div style='margin-top:16px'></div>", unsafe_allow_html=True)

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

    # Validació: mLDC ha de ser > 0 per poder continuar
    if mLDC <= 0:
        st.error(T_["error_rang"].format(lwl=Lwl))
        st.stop()

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
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(T_["ntfg"],      f"{N_TFG}", "ISO 12215-5")
    c2.metric(T_["ntfm"],      f"{N_TFM}",
              delta=f"+{Delta_N}", delta_color="inverse")
    c3.metric(T_["increment"], f"{Delta_N}")
    c4.metric(T_["dmin"],      f"{d_min:.2f} m")

    if ok_geom:
        st.success(T_["correcte"])
    else:
        st.error(T_["atencio"])
    st.info(T_["recomanacio"].format(dmin=d_min, bmig=B_mig))

    # ── Detall tècnic ──
    with st.expander(T_["detall"]):
        ca, cb = st.columns(2)
        with ca:
            st.markdown("**ISO 12215-5**")
            for k, v in {"mLDC (kg)": f"{mLDC:,.0f}", "b=l (m)": f"{b:.3f}",
                         "V (kn)": f"{V:.3f}", "nCG": f"{nCG:.4f}",
                         "KL": f"{KL:.4f}", "KAR": f"{KAR:.4f}",
                         "P_disseny (N/m²)": f"{P_disseny:.2f}",
                         "F_limit (N)": f"{F_limit:,.0f}",
                         "Δ (kg)": f"{Delta:,.0f}"}.items():
                st.markdown(f"- **{k}**: {v}")
        with cb:
            st.markdown("**IAP-11**")
            for k, v in {"v_b(T) (m/s)": f"{v_bT:.3f}", "c_prob": f"{c_prob:.5f}",
                         "H_exp (m)": f"{H_exp:.3f}", "A_ref (m²)": f"{A_ref:.3f}",
                         "ce(z)": f"{ce:.4f}", "F_w (N)": f"{F_w:,.0f}",
                         "M_w (N·m)": f"{M_w:,.0f}",
                         "2·M_w/B (N)": f"{terme_vent:,.0f}"}.items():
                st.markdown(f"- **{k}**: {v}")

# ── Footer ──
st.divider()
st.markdown(f"<div class='footer'>{T_['footer']}</div>", unsafe_allow_html=True)
