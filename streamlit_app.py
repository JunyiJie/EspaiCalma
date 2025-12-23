import streamlit as st
from datetime import date

# Configuro la pàgina
st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTAT DE L'IDIOMA
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# DICCIONARI DE TEXTOS (AMPLIAT AMB PDF)
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "EspaiCalma",
        "subtitle": "La teva xarxa d'espais privats per al silenci i la concentració.",
        "mvp": "🚀 MVP: Demo oficial per a la validació del Pla d'Empresa.",
        "spaces_title": "Els Nostres Espais",
        "spaces_sub": "Dissenyats sota la metodologia Lean Startup per maximitzar la teva productivitat.",
        "faqs_title": "Preguntes Freqüents",
        "about_title": "Sobre el Projecte",
        "contact_title": "Contacte",
        "booking_title": "Reserva el teu espai",
        "contact_send": "Enviar Missatge",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit! Hem registrat el teu interès.",
        "booking_error": "❌ Error: Has d'emplenar Nom, Cognoms, Email i Telèfon per reservar.",
        "booking_info": "Aquesta acció ens ajuda a mesurar el 'Product-Market Fit' del projecte.",
        "cancel_warning": "⚠️ Avís: Si passats 10 minuts de l'hora de reserva no hi ha ningú a l'aula, la reserva es cancel·larà automàticament.",
        "loc": "Ubicació",
        "space": "Tipus d'Espai",
        "date": "Data",
        "hours": "Durada (Hores)",
        "price": "Preu total estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Email UPC / Personal",
        "phone": "Telèfon mobil",
        "pricing": "Tarifes i Packs",
        "team_title": "Equip Directiu",
        "mission_title": "La Nostra Missió",
        "mission_text": "Apropar el silenci i el confort a cada estudiant i treballador, eliminant les distraccions de les biblioteques saturades.",
    },
    "ESP": {
        "welcome": "EspaiCalma",
        "subtitle": "Tu red de espacios privados para el silencio y la concentración.",
        "mvp": "🚀 MVP: Demo oficial para la validación del Plan de Empresa.",
        "spaces_title": "Nuestros Espacios",
        "spaces_sub": "Diseñados bajo metodología Lean Startup para maximizar tu productividad.",
        "faqs_title": "Preguntas Frecuentes",
        "about_title": "Sobre el Proyecto",
        "contact_title": "Contacto",
        "booking_title": "Reserva tu espacio",
        "contact_send": "Enviar Mensaje",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ ¡Reserva simulada con éxito!",
        "booking_error": "❌ Error: Debes rellenar Nombre, Apellidos, Email y Teléfono para reservar.",
        "booking_info": "Esta acción nos ayuda a medir el 'Product-Market Fit' del proyecto.",
        "cancel_warning": "⚠️ Aviso: Si pasados 10 minutos de la hora de reserva no hay nadie en el aula, la reserva se cancelará automáticamente.",
        "loc": "Ubicación",
        "space": "Tipo de Espacio",
        "date": "Fecha",
        "hours": "Duración (Horas)",
        "price": "Precio total estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Email UPC / Personal",
        "phone": "Teléfono móvil",
        "pricing": "Tarifas y Packs",
        "team_title": "Equipo Directivo",
        "mission_title": "Nuestra Misión",
        "mission_text": "Acercar el silencio y el confort a cada estudiante y trabajador, eliminando las distracciones de las bibliotecas saturadas.",
    }
}

# ---------------------------
# ESTILS CSS
# ---------------------------
BG_URL = "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80"

st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url("{BG_URL}");
        background-size: cover;
        background-attachment: fixed;
    }}
    .hero-title {{ font-size: 80px; font-weight: 850; color: white; text-align: center; margin-bottom: 0px; }}
    .hero-sub {{ font-size: 28px; color: #E0E0E0; text-align: center; margin-bottom: 40px; }}
    .ec-card {{
        background: rgba(255, 255, 255, 0.98);
        padding: 35px; border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        color: #1a1a1a;
    }}
    .team-card {{
        background: #f8f9fa; padding: 20px; border-radius: 10px;
        text-align: center; border-top: 5px solid #C9AD78;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# HEADER I IDIOMA
# ---------------------------
lang = st.session_state.lang
t = TXT.get(lang, TXT["CAT"])

col_l, _ = st.columns([2, 8])
with col_l:
    c_cat, c_esp = st.columns(2)
    if c_cat.button("CAT"): st.session_state.lang = "CAT"; st.rerun()
    if c_esp.button("ESP"): st.session_state.lang = "ESP"; st.rerun()

st.markdown(f'<h1 class="hero-title">{t["welcome"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-sub">{t["subtitle"]}</p>', unsafe_allow_html=True)

# ---------------------------
# TABS PRINCIPALS
# ---------------------------
tabs = st.tabs(["🏠 Inici", "🌿 Serveis", "👥 Equip", "❓ FAQs", "✉️ Contacte", "🗓️ Reserva"])

# --- TAB INICI (Basat en Proposta de Valor) ---
with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.subheader(t["mission_title"])
    st.write(t["mission_text"])
    
    st.markdown("---")
    st.markdown("### Per què EspaiCalma?")
    c1, c2, c3 = st.columns(3)
    c1.markdown("#### 🔇 Silenci Real\nInsonorització certificada per a una concentració absoluta.")
    c2.markdown("#### 🪑 Ergonomia\nCadires d'oficina de gamma alta per evitar fatiga física.")
    c3.markdown("#### 🚀 Connexió\nWi-Fi 6 de baixa latència, ideal per a exàmens o videotrucades.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB SERVEIS I TARIFES (Basat en Pla Econòmic) ---
with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["pricing"])
    st.write("Segons el nostre pla de viabilitat, oferim opcions flexibles:")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### ⏱️ Pagament per Ús")
        st.write("- **Tarifa Estàndard:** 3 € / hora")
        st.write("- **Reserva de dia complet:** 20 €")
    with col_t2:
        st.markdown("#### 🎟️ Packs d'Estalvi")
        st.write("- **Pack 10 hores:** 25 € (Estalvi del 17%)")
        st.write("- **Abonament Mensual:** 45 € (20 hores incloses)")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB EQUIP (Dades reals del PDF) ---
with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["team_title"])
    st.write("Els fundadors darrere d'EspaiCalma, estudiants de l'EEBE (UPC):")
    
    eq1, eq2, eq3, eq4 = st.columns(4)
    with eq1: st.markdown('<div class="team-card"><b>Aleix Trogal</b><br>CEO & Estratègia</div>', unsafe_allow_html=True)
    with eq2: st.markdown('<div class="team-card"><b>Eloi Gil</b><br>CMO & Màrqueting</div>', unsafe_allow_html=True)
    with eq3: st.markdown('<div class="team-card"><b>Marc Vidal</b><br>CFO & Finances</div>', unsafe_allow_html=True)
    with eq4: st.markdown('<div class="team-card"><b>Junyi Jie</b><br>CTO & Disseny</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TABS FAQS I SOBRE (Contingut estàndard) ---
with tabs[3]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander("On estem ubicats?"): st.write("La nostra primera fase se centra en la Zona Universitària (Les Corts / EEBE).")
    with st.expander("Es pot menjar dins els espais?"): st.write("Només es permeten begudes amb tapa i petits snacks per mantenir la neteja i l'olor de l'espai.")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("contact"):
        st.text_input("Nom i Cognoms")
        st.text_input("Email")
        st.text_area("Com et podem ajudar?")
        st.form_submit_button(t["contact_send"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB RESERVA (AMB EL SISTEMA DE VALIDACIÓ REQUERIT) ---
with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    st.markdown(f'<div class="warning-text">{t["cancel_warning"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form_final"):
        st.markdown("#### 👤 1. Dades del Client (Obligatòries)")
        b1, b2 = st.columns(2)
        with b1:
            nom_v = st.text_input(t["name"])
            cog_v = st.text_input(t["surname"])
        with b2:
            mail_v = st.text_input(t["email"])
            tel_v = st.text_input(t["phone"])
            
        st.divider()
        st.markdown("#### 📍 2. Configuració de l'Espai")
        b3, b4 = st.columns(2)
        with b3:
            loc_v = st.selectbox(t["loc"], ["EEBE (Campus Besòs)", "Les Corts (Zona Univ.)", "Eixample"])
            tip_v = st.selectbox(t["space"], ["Cabina Individual", "Sala de Treball (Max 2)", "Zona Llum Natural"])
        with b4:
            dat_v = st.date_input(t["date"], min_value=date.today())
            hor_v = st.slider(t["hours"], 1, 8, 2)

        # Preu dinàmic 3€/h
        p_total = hor_v * 3
        st.markdown(f"### {t['price']}: {p_total} €")
        
        btn_reserva = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    if btn_reserva:
        # VALIDACIÓ ESTRICTA: No es permet si falta algun camp clau
        if not nom_v.strip() or not cog_v.strip() or not mail_v.strip() or not tel_v.strip():
            st.error(t["booking_error"])
        else:
            st.success(t["booking_ok"])
            st.balloons()
            st.info(t["booking_info"])
    st.markdown("</div>", unsafe_allow_html=True)
