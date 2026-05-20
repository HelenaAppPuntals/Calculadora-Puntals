"""
Calculadora de Puntals de Varada
Helena Maymi Ardèvol · Facultat de Nautica de Barcelona · UPC
streamlit run calculadora_puntals_FINAL.py
"""

import math
import streamlit as st

st.set_page_config(page_title="Calculadora de Puntals", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #07111f;
    background-image:
        radial-gradient(ellipse at 15% 0%, rgba(0,70,150,0.22) 0%, transparent 55%),
        radial-gradient(ellipse at 85% 100%, rgba(0,35,90,0.28) 0%, transparent 55%);
}

.main .block-container {
    max-width: 1000px;
    padding: 2rem 2rem 4rem;
}

/* Capçalera */
.cap {
    background: linear-gradient(135deg, #0c2040 0%, #0a3268 55%, #0c2040 100%);
    border: 1px solid rgba(80,140,240,0.16);
    border-radius: 14px;
    padding: 30px 36px 26px;
    margin-bottom: 28px;
}
.cap-label {
    font-size: 0.65rem;
    font-weight: 700;
    color: #3a78c0;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.cap-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #e2f0ff;
    line-height: 1.15;
    margin-bottom: 6px;
}
.cap-line {
    width: 44px; height: 3px;
    background: linear-gradient(90deg, #1a6aff, #00b4d8);
    border-radius: 2px;
    margin: 12px 0;
}
.cap-sub {
    font-size: 0.76rem;
    color: #6a9ecc;
    letter-spacing: 0.03em;
    margin-bottom: 10px;
}
.cap-desc {
    font-size: 0.83rem;
    color: #9abce0;
    line-height: 1.55;
    max-width: 620px;
}
.badge {
    display: inline-block;
    background: rgba(0,90,210,0.22);
    border: 1px solid rgba(70,140,255,0.28);
    border-radius: 20px;
    padding: 3px 13px;
    font-size: 0.68rem;
    color: #6ab8ff;
    margin-right: 6px;
    margin-top: 12px;
    letter-spacing: 0.07em;
    font-weight: 600;
}

/* Seccio dades */
.sec-label {
    font-size: 0.65rem;
    font-weight: 700;
    color: #3a78c0;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(60,110,200,0.12);
}

/* Inputs */
.stNumberInput label, .stSelectbox label {
    font-size: 0.8rem !important;
    color: #6a9ecc !important;
    font-weight: 500 !important;
    letter-spacing: 0.03em !important;
}
.stNumberInput > div > div > input {
    background: rgba(4,14,38,0.9) !important;
    border: 1px solid rgba(60,120,210,0.22) !important;
    border-radius: 8px !important;
    color: #d8eeff !important;
    font-size: 0.95rem !important;
}
.stSelectbox > div > div {
    background: rgba(4,14,38,0.9) !important;
    border: 1px solid rgba(60,120,210,0.22) !important;
    border-radius: 8px !important;
    color: #d8eeff !important;
}

/* Boto */
.stButton > button {
    background: linear-gradient(135deg, #1655b8 0%, #0c3a98 100%) !important;
    color: #e0f0ff !important;
    border: 1px solid rgba(90,160,255,0.28) !important;
    border-radius: 10px !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    font-family: 'DM Sans', sans-serif !important;
    letter-spacing: 0.05em !important;
    box-shadow: 0 4px 18px rgba(0,50,170,0.32) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1e68d0 0%, #1048b8 100%) !important;
    box-shadow: 0 6px 26px rgba(0,70,210,0.45) !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: rgba(6,18,46,0.9) !important;
    border: 1px solid rgba(50,110,190,0.16) !important;
    border-radius: 10px !important;
    color: #7aaee0 !important;
    font-size: 0.83rem !important;
}
.streamlit-expanderContent {
    background: rgba(6,18,46,0.7) !important;
    border: 1px solid rgba(50,110,190,0.1) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
    color: #9abce0 !important;
    font-size: 0.83rem !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #2a5080;
    font-size: 0.7rem;
    margin-top: 40px;
    padding-top: 16px;
    border-top: 1px solid rgba(40,80,140,0.14);
    letter-spacing: 0.04em;
}
</style>
""", unsafe_allow_html=True)

# ── TEXTOS ──
TEXTOS = {
    "CA": {
        "titol": "Calculadora de Puntals de Varada",
        "subtitol": "Helena Maymí Ardèvol · Facultat de Nàutica de Barcelona · UPC",
        "descripcio": "Càlcul del nombre mínim de puntals per varar una embarcació d'esbarjo considerant el pes propi (ISO 12215-5) i l'acció del vent (IAP-11).",
        "dades": "Dades de l'embarcació",
        "lwl": "Lwl — Eslora en la flotació (m)",
        "bc": "Bc — Mànega al pantoc (m)",
        "t": "T — Calat (m)",
        "tipus": "Tipus d'embarcació",
        "potencia": "Potència del motor (kW)",
        "motora": "MOTORA", "veler": "VELER",
        "calcular": "Calcular",
        "resultats": "Resultats",
        "ntfg": "Puntals sense vent",
        "ntfm": "Puntals amb vent",
        "increment": "Increment pel vent",
        "dmin": "Distància mínima",
        "correcte": "CORRECTE — Els puntals caben dins la mànega del vaixell.",
        "atencio": "ATENCIÓ — d_min supera B/2. Revisar la distribució dels puntals.",
        "recomanacio": "Recomanació: Col·locar els puntals a >= {dmin:.2f} m del centre, idealment tan a prop de B/2 = {bmig:.2f} m com sigui possible.",
        "detall": "Veure detall dels càlculs",
        "ajuda_lwl": "Longitud mesurada a la línia de flotació",
        "ajuda_bc": "Amplada a la part més ampla del fons",
        "ajuda_t": "Profunditat sota la línia de flotació",
        "ajuda_tipus": "Selecciona el tipus d'embarcació",
        "ajuda_potencia": "Només necessari per a motores",
        "footer": "Calculadora desenvolupada per Helena Maymí Ardèvol · TFM · Facultat de Nàutica de Barcelona · UPC · 2024 · Basat en ISO 12215-5 i IAP-11",
        "error_rang": "⚠️ Dades fora de rang — Amb Lwl = {lwl:.2f} m, la massa de desplaçament estimada per la ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) resulta zero o negativa. La normativa requereix una eslora mínima d'aproximadament 5.27 m per poder aplicar aquesta metodologia. Reviseu les dades introduïdes.",
    },
    "ES": {
        "titol": "Calculadora de Puntales de Varada",
        "subtitol": "Helena Maymí Ardèvol · Facultad de Náutica de Barcelona · UPC",
        "descripcio": "Cálculo del número mínimo de puntales para varar una embarcación de recreo considerando el peso propio (ISO 12215-5) y la acción del viento (IAP-11).",
        "dades": "Datos de la embarcación",
        "lwl": "Lwl — Eslora en la flotación (m)",
        "bc": "Bc — Manga en el pantoque (m)",
        "t": "T — Calado (m)",
        "tipus": "Tipo de embarcación",
        "potencia": "Potencia del motor (kW)",
        "motora": "MOTORA", "veler": "VELERO",
        "calcular": "Calcular",
        "resultats": "Resultados",
        "ntfg": "Puntales sin viento",
        "ntfm": "Puntales con viento",
        "increment": "Incremento por viento",
        "dmin": "Distancia mínima",
        "correcte": "CORRECTO — Los puntales caben dentro de la manga del barco.",
        "atencio": "ATENCIÓN — d_min supera B/2. Revisar la distribución de los puntales.",
        "recomanacio": "Recomendación: Colocar los puntales a >= {dmin:.2f} m del centro, idealmente tan cerca de B/2 = {bmig:.2f} m como sea posible.",
        "detall": "Ver detalle de los cálculos",
        "ajuda_lwl": "Longitud medida en la línea de flotación",
        "ajuda_bc": "Anchura en la parte más ancha del fondo",
        "ajuda_t": "Profundidad bajo la línea de flotación",
        "ajuda_tipus": "Selecciona el tipo de embarcación",
        "ajuda_potencia": "Sólo necesario para motoras",
        "footer": "Calculadora desarrollada por Helena Maymí Ardèvol · TFM · Facultad de Náutica de Barcelona · UPC · 2024 · Basado en ISO 12215-5 e IAP-11",
        "error_rang": "⚠️ Datos fuera de rango — Con Lwl = {lwl:.2f} m, la masa de desplazamiento estimada por la ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) resulta cero o negativa. La normativa requiere una eslora mínima de aproximadamente 5.27 m para aplicar esta metodología. Revisad los datos introducidos.",
    },
    "EN": {
        "titol": "Boat Docking Support Calculator",
        "subtitol": "Helena Maymí Ardèvol · Faculty of Nautical Sciences of Barcelona · UPC",
        "descripcio": "Minimum number of supports to safely dock a recreational boat considering self-weight (ISO 12215-5) and wind action (IAP-11).",
        "dades": "Vessel Data",
        "lwl": "Lwl — Waterline length (m)",
        "bc": "Bc — Chine beam (m)",
        "t": "T — Draft (m)",
        "tipus": "Vessel type",
        "potencia": "Engine power (kW)",
        "motora": "MOTORBOAT", "veler": "SAILBOAT",
        "calcular": "Calculate",
        "resultats": "Results",
        "ntfg": "Supports without wind",
        "ntfm": "Supports with wind",
        "increment": "Wind increment",
        "dmin": "Minimum distance",
        "correcte": "CORRECT — Supports fit within the vessel beam.",
        "atencio": "WARNING — d_min exceeds B/2. Review support distribution.",
        "recomanacio": "Recommendation: Place supports at >= {dmin:.2f} m from centre, ideally as close to B/2 = {bmig:.2f} m as possible.",
        "detall": "View calculation detail",
        "ajuda_lwl": "Length measured at the waterline",
        "ajuda_bc": "Width at the widest part of the bottom",
        "ajuda_t": "Depth below the waterline",
        "ajuda_tipus": "Select vessel type",
        "ajuda_potencia": "Only required for motorboats",
        "footer": "Calculator developed by Helena Maymi Ardèvol · TFM · Faculty of Nautical Sciences of Barcelona · UPC · 2024 · Based on ISO 12215-5 and IAP-11",
        "error_rang": "⚠️ Data out of range — With Lwl = {lwl:.2f} m, the displacement mass estimated by ISO 12215-5 (mLDC = 1369·Lwl − 7223.1) is zero or negative. The standard requires a minimum waterline length of approximately 5.27 m to apply this methodology. Please review the input data.",
    }
}

# ── SELECTOR IDIOMA ──
idioma = st.selectbox("Idioma", ["CA", "ES", "EN"], label_visibility="hidden")
T_ = TEXTOS[idioma]

# ── CAPÇALERA ──
st.markdown(f"""
<div class="cap">
    <div class="cap-label">Nàutica · UPC</div>
    <div class="cap-title">{T_['titol']}</div>
    <div class="cap-line"></div>
    <div class="cap-sub">{T_['subtitol']}</div>
    <div class="cap-desc">{T_['descripcio']}</div>
    <div>
        <span class="badge">ISO 12215-5</span>
        <span class="badge">IAP-11</span>
        <span class="badge">TFM 2024</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ── DADES ──
st.markdown(f'<div class="sec-label">{T_["dades"]}</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")
with col1:
    Lwl = st.number_input(T_["lwl"], min_value=2.5, max_value=24.5, value=12.35, step=0.01, help=T_["ajuda_lwl"])
    Bc  = st.number_input(T_["bc"],  min_value=1.0, max_value=10.0, value=4.20,  step=0.01, help=T_["ajuda_bc"])
    T   = st.number_input(T_["t"],   min_value=0.3, max_value=5.0,  value=2.10,  step=0.01, help=T_["ajuda_t"])
with col2:
    tipus_sel = st.selectbox(T_["tipus"], options=[T_["motora"], T_["veler"]], index=1, help=T_["ajuda_tipus"])
    tipus = "MOTORA" if tipus_sel == T_["motora"] else "VELER"
    Potencia = st.number_input(T_["potencia"], min_value=0.0, max_value=5000.0, value=29.44, step=1.0,
                               disabled=(tipus == "VELER"), help=T_["ajuda_potencia"])

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

# ── CALCULAR ──
if st.button(T_["calcular"], use_container_width=True):

    Beta_04 = 30; x_Lwl = 0.6; Gz_max60 = 60; Cb = 0.23
    dens_as = 1.025; Kdc = 1.0; beta_coef = 0.1838
    eta_motora = 0.10; eta_veler = 0.23

    mLDC = max(0.0, 1369 * Lwl - 7223.1)

    if mLDC <= 0:
        st.markdown(f"""
        <div style="background:rgba(180,30,30,0.12); border:1px solid rgba(210,60,60,0.3);
                    border-radius:10px; padding:16px 20px; color:#ff8a80;
                    font-size:0.86rem; line-height:1.6;">
            {T_['error_rang'].format(lwl=Lwl)}
        </div>
        """, unsafe_allow_html=True)
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

    K = 0.2; T_ret = 10; kr_vent = 0.156; z0 = 0.003; z_min = 1.0; cf = 1.65
    c_prob = (((1-K*math.log(-math.log(1-1/T_ret))) / (1-K*math.log(-math.log(0.98))))**0.5)
    v_bT  = 29.0 * c_prob
    H_exp = Bc / 2;  A_ref = Lwl * H_exp;  h_cp = H_exp / 2
    z_ce  = max(h_cp, z_min)
    ce    = kr_vent**2 * math.log(z_ce/z0)**2 * (1 + 7*kr_vent/math.log(z_ce/z0))
    F_w   = 0.5 * 1.25 * v_bT**2 * ce * cf * A_ref
    M_w   = F_w * h_cp
    terme_vent = 2 * M_w / Bc

    eta   = eta_motora if tipus == "MOTORA" else eta_veler
    N_TFG = math.ceil((Delta*9.81*eta) / F_limit)
    N_TFM = math.ceil((Delta*9.81*eta + terme_vent) / F_limit)
    Delta_N = N_TFM - N_TFG
    d_min   = M_w / (F_limit * (N_TFM / 2))
    B_mig   = Bc / 2
    ok_geom = d_min <= B_mig

    col_ok   = "#00e676" if ok_geom else "#ff5252"
    bg_ok    = "rgba(0,160,70,0.1)" if ok_geom else "rgba(200,30,30,0.1)"
    brd_ok   = "rgba(0,200,90,0.22)" if ok_geom else "rgba(210,50,50,0.22)"

    # ── RESULTATS ──
    st.markdown(f"""
    <div style="font-size:0.65rem; font-weight:700; color:#3a78c0;
                letter-spacing:0.14em; text-transform:uppercase;
                margin:24px 0 14px; padding-bottom:10px;
                border-bottom:1px solid rgba(50,110,200,0.12);">
        {T_['resultats']}
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    def card(col, label, value, sub, sub_color="#2e6090"):
        col.markdown(f"""
        <div style="background:rgba(3,10,30,0.85);
                    border:1px solid rgba(50,100,190,0.18);
                    border-radius:12px; padding:26px 12px 20px;
                    text-align:center; height:100%;">
            <div style="font-size:0.6rem; font-weight:700; color:#4a80b4;
                        letter-spacing:0.1em; text-transform:uppercase; margin-bottom:14px;">
                {label}
            </div>
            <div style="font-family:'Playfair Display',Georgia,serif; font-size:3.8rem;
                        font-weight:700; color:#c8e4ff; line-height:1;">
                {value}
            </div>
            <div style="font-size:0.63rem; color:{sub_color}; margin-top:12px; letter-spacing:0.06em;">
                {sub}
            </div>
        </div>
        """, unsafe_allow_html=True)

    card(c1, T_['ntfg'],      N_TFG,          "ISO 12215-5")
    card(c2, T_['ntfm'],      N_TFM,          f"+{Delta_N} IAP-11", "#c06030")
    card(c3, T_['increment'], Delta_N,        "&nbsp;")
    card(c4, T_['dmin'],      f"{d_min:.2f}", "metres")

    st.markdown("<div style='height:14px'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{bg_ok}; border:1px solid {brd_ok}; border-radius:10px;
                padding:14px 18px; margin-bottom:10px; color:{col_ok};
                font-size:0.86rem; font-weight:500;">
        {T_['correcte'] if ok_geom else T_['atencio']}
    </div>
    <div style="background:rgba(0,35,90,0.3); border:1px solid rgba(50,110,220,0.16);
                border-radius:10px; padding:14px 18px; color:#90b8e0;
                font-size:0.83rem; line-height:1.6; margin-bottom:8px;">
        {T_['recomanacio'].format(dmin=d_min, bmig=B_mig)}
    </div>
    """, unsafe_allow_html=True)

    # ── DETALL TECNIC ──
    with st.expander(T_["detall"]):
        ca, cb = st.columns(2)
        with ca:
            st.markdown("**ISO 12215-5**")
            for k, v in {"mLDC (kg)": f"{mLDC:,.0f}", "b=l (m)": f"{b:.3f}",
                         "V (kn)": f"{V:.3f}", "nCG": f"{nCG:.4f}",
                         "KL": f"{KL:.4f}", "KAR": f"{KAR:.4f}",
                         "P_disseny (N/m2)": f"{P_disseny:.2f}",
                         "F_limit (N)": f"{F_limit:,.0f}",
                         "Delta (kg)": f"{Delta:,.0f}"}.items():
                st.markdown(f"- **{k}**: {v}")
        with cb:
            st.markdown("**IAP-11**")
            for k, v in {"v_b(T) (m/s)": f"{v_bT:.3f}", "c_prob": f"{c_prob:.5f}",
                         "H_exp (m)": f"{H_exp:.3f}", "A_ref (m2)": f"{A_ref:.3f}",
                         "ce(z)": f"{ce:.4f}", "F_w (N)": f"{F_w:,.0f}",
                         "M_w (N·m)": f"{M_w:,.0f}",
                         "2·M_w/B (N)": f"{terme_vent:,.0f}"}.items():
                st.markdown(f"- **{k}**: {v}")

# ── FOOTER ──
st.markdown(f"<div class='footer'>{T_['footer']}</div>", unsafe_allow_html=True)
