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
# DICCIONARI DE TEXTOS
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "EspaiCalma",
        "subtitle": "La teva xarxa d'espais privats per al silenci i la concentració.",
        "mvp": "🚀 MVP: Demo oficial per a la validació del Pla d'Empresa.",
        "spaces_title": "Els Nostres Espais",
        "spaces_sub": "Tria l'ambient que millor s'adapti al teu flux de treball.",
        "faqs_title": "Preguntes Freqüents",
        "about_title": "Sobre el Projecte",
        "contact_title": "Contacte",
        "booking_title": "Reserva el teu espai",
        "contact_send": "Enviar Missatge",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit!",
        "booking_error": "❌ Error: Has d'emplenar Nom, Cognoms, Email i Telèfon.",
        "contact_error": "❌ Error: Si us plau, introdueix el teu correu electrònic.",
        "booking_info": "Aquesta acció ens ajuda a mesurar l'interès real del projecte.",
        "cancel_warning": "⚠️ Avís: Si passats 10 minuts de l'hora de reserva no hi ha ningú, la reserva es cancel·larà.",
        "loc": "Ubicació",
        "space": "Tipus d'Espai",
        "date": "Data",
        "hours": "Durada (Hores)",
        "price": "Preu total estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Email",
        "phone": "Telèfon",
        "pricing": "Tarifes i Packs",
        "team_title": "Equip Directiu",
    },
    "ESP": {
        "welcome": "EspaiCalma",
        "subtitle": "Tu red de espacios privados para el silencio y la concentración.",
        "mvp": "🚀 MVP: Demo oficial para la validación del Plan de Empresa.",
        "spaces_title": "Nuestros Espacios",
        "spaces_sub": "Elige el ambiente que mejor se adapte a tu flujo de trabajo.",
        "faqs_title": "Preguntas Frecuentes",
        "about_title": "Sobre el Proyecto",
        "contact_title": "Contacto",
        "booking_title": "Reserva tu espacio",
        "contact_send": "Enviar Mensaje",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ ¡Reserva simulada con éxito!",
        "booking_error": "❌ Error: Debes rellenar Nombre, Apellidos, Email y Teléfono.",
        "contact_error": "❌ Error: Por favor, introduce tu correo electrónico.",
        "booking_info": "Esta acción nos ayuda a medir el interés real del proyecto.",
        "cancel_warning": "⚠️ Aviso: Si pasados 10 minutos de la hora de reserva no hay nadie, la reserva se cancelará.",
        "loc": "Ubicación",
        "space": "Tipo de Espacio",
        "date": "Fecha",
        "hours": "Duración (Horas)",
        "price": "Precio total estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Email",
        "phone": "Teléfono",
        "pricing": "Tarifas y Packs",
        "team_title": "Equipo Directivo",
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
    .hero-title {{ font-size: 70px; font-weight: 850; color: white; text-align: center; }}
    .hero-sub {{ font-size: 26px; color: #E0E0E0; text-align: center; margin-bottom: 40px; }}
    .ec-card {{
        background: rgba(255, 255, 255, 0.98);
        padding: 35px; border-radius: 15px;
        color: #1a1a1a;
    }}
    /* Targetes d'equip amb lletres visibles (Negre) */
    .team-card {{
        background: #f1f3f5; 
        padding: 20px; 
        border-radius: 10px;
        text-align: center; 
        border-top: 5px solid #C9AD78;
        color: #1a1a1a !important;
        font-weight: bold;
    }}
    .team-card p, .team-card b {{
        color: #1a1a1a !important;
    }}
</style>
""", unsafe_allow_html=True)

lang = st.session_state.lang
t = TXT.get(lang, TXT["CAT"])

# ---------------------------
# HEADER
# ---------------------------
col_l, _ = st.columns([2, 8])
with col_l:
    c_cat, c_esp = st.columns(2)
    if c_cat.button("CAT"): st.session_state.lang = "CAT"; st.rerun()
    if c_esp.button("ESP"): st.session_state.lang = "ESP"; st.rerun()

st.markdown(f'<h1 class="hero-title">{t["welcome"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-sub">{t["subtitle"]}</p>', unsafe_allow_html=True)

tabs = st.tabs(["🏠 Inici", "🌿 Serveis", "👥 Equip", "❓ FAQs", "✉️ Contacte", "🗓️ Reserva"])

# --- TAB SERVEIS (AMB IMATGES) ---
with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    st.write(t["spaces_sub"])
    
    col_img1, col_img2, col_img3 = st.columns(3)
    with col_img1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400", caption="Cabina Privada Insonoritzada")
    with col_img2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400", caption="Espai de Coworking Obert")
    with col_img3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?w=400", caption="Zona Confort amb Llum Natural")
    
    st.divider()
    st.subheader(t["pricing"])
    st.write("3 € / hora (Packs de 10h i 20h disponibles)")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB EQUIP (CORRECCIÓ COLOR LLETRES) ---
with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["team_title"])
    
    eq1, eq2, eq3, eq4 = st.columns(4)
    with eq1: st.markdown('<div class="team-card"><b>Aleix Trogal</b><br><span style="color:#555">CEO & Estratègia</span></div>', unsafe_allow_html=True)
    with eq2: st.markdown('<div class="team-card"><b>Eloi Gil</b><br><span style="color:#555">CMO & Màrqueting</span></div>', unsafe_allow_html=True)
    with eq3: st.markdown('<div class="team-card"><b>Marc Vidal</b><br><span style="color:#555">CFO & Finances</span></div>', unsafe_allow_html=True)
    with eq4: st.markdown('<div class="team-card"><b>Junyi Jie</b><br><span style="color:#555">CTO & Disseny</span></div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB CONTACTE (VALIDACIÓ EMAIL) ---
with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("contact_form"):
        nom_c = st.text_input("Nom i Cognoms")
        mail_c = st.text_input("Email")
        msg_c = st.text_area("El teu missatge")
        
        btn_c = st.form_submit_button(t["contact_send"])
        if btn_c:
            if not mail_c.strip():
                st.error(t["contact_error"])
            else:
                st.success("Missatge enviat correctament. Ens posarem en contacte amb tu!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB RESERVA (VALIDACIÓ ESTRICTA) ---
with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    st.markdown(f'<div class="warning-text" style="color:red; font-weight:bold;">{t["cancel_warning"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form_v2"):
        st.markdown("#### 👤 Dades Obligatòries")
        b1, b2 = st.columns(2)
        with b1:
            nom_v = st.text_input(t["name"])
            cog_v = st.text_input(t["surname"])
        with b2:
            mail_v = st.text_input(t["email"])
            tel_v = st.text_input(t["phone"])
            
        st.divider()
        b3, b4 = st.columns(2)
        with b3:
            loc_v = st.selectbox(t["loc"], ["EEBE (Campus Besòs)", "Les Corts (Zona Univ.)"])
            tip_v = st.selectbox(t["space"], ["Cabina Individual", "Sala de Treball", "Zona Llum Natural"])
        with b4:
            dat_v = st.date_input(t["date"], min_value=date.today())
            hor_v = st.slider(t["hours"], 1, 8, 2)

        st.markdown(f"### Total: {hor_v * 3} €")
        
        btn_reserva = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    if btn_reserva:
        if not nom_v.strip() or not cog_v.strip() or not mail_v.strip() or not tel_v.strip():
            st.error(t["booking_error"])
        else:
            st.success(t["booking_ok"])
            st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
