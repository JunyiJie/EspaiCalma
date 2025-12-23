import streamlit as st
from datetime import date
import re

# Función auxiliar para validar email
def is_valid_email(email):
    # Patrón estándar de validación de correo electrónico
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Configuración de la página
st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTADO DEL IDIOMA
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# DICCIONARIO DE TEXTOS (CAT, ESP, ENG)
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "EspaiCalma",
        "subtitle": "La teva xarxa d'espais privats per al silenci i la concentració.",
        "mvp": "🚀 MVP: Demo oficial per a la validació del Pla d'Empresa.",
        "spaces_title": "Els Nostres Espais",
        "spaces_sub": "Tria l'ambient que millor s'adapti al teu flux de treball.",
        "faqs_title": "Preguntes Freqüents",
        "about_title": "Sobre Nosaltres",
        "contact_title": "Contacte",
        "booking_title": "Reserva el teu espai",
        "rules_title": "Normativa de l'Espai",
        "contact_send": "Enviar Missatge",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit!",
        "booking_error": "❌ Error: Emplena tots els camps correctament.",
        "email_error": "❌ Error: Introdueix un correu electrònic vàlid.",
        "phone_error": "❌ Error: El telèfon ha de tenir 9 xifres (Espanya).",
        "contact_error": "❌ Error: Introdueix el teu correu electrònic.",
        "cancel_warning": "⚠️ Avís: Si passats 10 minuts de la reserva no hi ha ningú, es cancel·larà.",
        "loc": "Ubicació",
        "space": "Tipus de Servei",
        "date": "Data",
        "hours": "Hores",
        "price": "Preu total estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Email",
        "phone": "Telèfon (9 xifres)",
        "pricing": "Tarifes",
        "team_title": "Equip Directiu",
        "faq1": "Com funciona?", "faq1a": "Selecciona espai, data i confirma dades.",
        "faq2": "On som?", "faq2a": "A prop de la UPC (EEBE) i Zona Universitària.",
    },
    "ESP": {
        "welcome": "EspaiCalma",
        "subtitle": "Tu red de espacios privados para el silencio y la concentración.",
        "mvp": "🚀 MVP: Demo oficial para la validación del Plan de Empresa.",
        "spaces_title": "Nuestros Espacios",
        "spaces_sub": "Elige el ambiente que mejor se adapte a tu trabajo.",
        "faqs_title": "Preguntas Frecuentes",
        "about_title": "Sobre Nosotros",
        "contact_title": "Contacto",
        "booking_title": "Reserva tu espacio",
        "rules_title": "Normativa del Espacio",
        "contact_send": "Enviar Mensaje",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ ¡Reserva simulada con éxito!",
        "booking_error": "❌ Error: Rellena todos los campos correctamente.",
        "email_error": "❌ Error: Introduce un correo electrónico válido.",
        "phone_error": "❌ Error: El teléfono debe tener 9 cifras (España).",
        "contact_error": "❌ Error: Introduce tu email.",
        "cancel_warning": "⚠️ Aviso: Si pasados 10 minutos de la reserva no hay nadie, se cancelará.",
        "loc": "Ubicación",
        "space": "Tipo de Servicio",
        "date": "Fecha",
        "hours": "Horas",
        "price": "Precio total estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Email",
        "phone": "Teléfono (9 cifras)",
        "pricing": "Tarifas",
        "team_title": "Equipo Directivo",
        "faq1": "¿Cómo funciona?", "faq1a": "Selecciona espacio, fecha y confirma datos.",
        "faq2": "¿Dónde estamos?", "faq2a": "Cerca de la UPC (EEBE) y Zona Universitaria.",
    },
    "ENG": {
        "welcome": "EspaiCalma",
        "subtitle": "Your network of private spaces for silence and focus.",
        "mvp": "🚀 MVP: Official demo for Business Plan validation.",
        "spaces_title": "Our Spaces",
        "spaces_sub": "Choose the environment that best fits your workflow.",
        "faqs_title": "FAQs",
        "about_title": "About Us",
        "contact_title": "Contact",
        "booking_title": "Book your space",
        "rules_title": "Space Regulations",
        "contact_send": "Send Message",
        "booking_confirm": "Confirm booking",
        "booking_ok": "✅ Booking simulated successfully!",
        "booking_error": "❌ Error: Fill in all fields correctly.",
        "email_error": "❌ Error: Please enter a valid email address.",
        "phone_error": "❌ Error: Phone must be 9 digits (Spain).",
        "contact_error": "❌ Error: Please enter your email.",
        "cancel_warning": "⚠️ Notice: If no one is present 10 min after the booking, it will be cancelled.",
        "loc": "Location",
        "space": "Service Type",
        "date": "Date",
        "hours": "Hours",
        "price": "Estimated total price",
        "name": "First Name",
        "surname": "Last Name",
        "email": "Email",
        "phone": "Phone (9 digits)",
        "pricing": "Pricing",
        "team_title": "Management Team",
        "faq1": "How it works?", "faq1a": "Select space, date and confirm your details.",
        "faq2": "Location?", "faq2a": "Near UPC (EEBE) and Zona Universitària.",
    }
}

# ---------------------------
# ESTILOS CSS
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
    .ec-card {{ background: rgba(255, 255, 255, 0.98); padding: 35px; border-radius: 15px; color: #1a1a1a; margin-bottom: 20px; }}
    .team-card {{
        background: #f1f3f5; padding: 20px; border-radius: 10px; text-align: center; 
        border-top: 5px solid #C9AD78; color: #1a1a1a !important;
    }}
    .team-card b {{ color: #1a1a1a !important; font-size: 1.2rem; }}
    .team-card span {{ color: #444 !important; }}
    .rule-item {{ margin-bottom: 10px; padding-left: 20px; border-left: 3px solid #C9AD78; }}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SELECTOR IDIOMA
# ---------------------------
l1, l2, l3, _ = st.columns([1, 1, 1, 7])
if l1.button("CAT"): st.session_state.lang = "CAT"; st.rerun()
if l2.button("ESP"): st.session_state.lang = "ESP"; st.rerun()
if l3.button("ENG"): st.session_state.lang = "ENG"; st.rerun()

lang = st.session_state.lang
t = TXT[lang]

# ---------------------------
# HEADER
# ---------------------------
st.markdown(f'<h1 class="hero-title">{t["welcome"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-sub">{t["subtitle"]}</p>', unsafe_allow_html=True)

tabs = st.tabs(["🏠 Inici", "🌿 Serveis", "👥 Equip", "📜 Normativa", "❓ FAQs", "✉️ Contacte", "🗓️ Reserva"])

# --- TAB INICI ---
with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.markdown("### Focus & Silence")
    st.write("EspaiCalma és la solució ideal per a qui busca un ambient de treball lliure de sorolls.")
    
    st.markdown("### Per què EspaiCalma?")
    c1, c2, c3 = st.columns(3)
    c1.markdown("#### 🔇 Silenci Real\nInsonorització certificada per a una concentració absoluta.")
    c2.markdown("#### 🪑 Ergonomia\nCadires d'oficina de gamma alta per evitar fatiga física.")
    c3.markdown("#### 🚀 Connexió\nWi-Fi 6 de baixa latència, ideal per a exàmens o videotrucades.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB SERVEIS ---
with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    c1, c2, c3 = st.columns(3)
    c1.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400", caption="Cabina Privada")
    c2.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400", caption="Zona Cowork")
    c3.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?w=400", caption="Zona Confort")
    st.divider()
    st.subheader(t["pricing"])
    st.write("3 € / hora")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB EQUIP ---
with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["team_title"])
    e1, e2, e3, e4 = st.columns(4)
    e1.markdown('<div class="team-card"><b>Aleix Trogal</b><br><span>CEO & Estratègia</span></div>', unsafe_allow_html=True)
    e2.markdown('<div class="team-card"><b>Eloi Gil</b><br><span>Marketing Manager</span></div>', unsafe_allow_html=True)
    e3.markdown('<div class="team-card"><b>Marc Vidal</b><br><span>CFO & Finances</span></div>', unsafe_allow_html=True)
    e4.markdown('<div class="team-card"><b>Junyi Jie</b><br><span>CTO & Design</span></div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB NORMATIVA ---
with tabs[3]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["rules_title"])
    
    col_rules1, col_rules2 = st.columns(2)
    with col_rules1:
        st.markdown("#### 🔇 Silenci i Comportament")
        st.markdown('<div class="rule-item"><b>Respecte al silenci:</b> Les zones de cabines i silenci obert exigeixen silenci absolut. Prohibit l\'ús d\'altaveus.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rule-item"><b>Trucades:</b> Les trucades només es poden realitzar dins de les cabines privades insonoritzades.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rule-item"><b>Sense fums:</b> Prohibit fumar o utilitzar vapers en qualsevol àrea de l\'establiment.</div>', unsafe_allow_html=True)
    
    with col_rules2:
        st.markdown("#### 🍎 Alimentació i Higiene")
        st.markdown('<div class="rule-item"><b>Zones de menjar:</b> Prohibit menjar a les taules de treball. S\'ha d\'utilitzar exclusivament la <b>sala de menjador / office</b>.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rule-item"><b>Begudes:</b> Es permeten begudes sempre que estiguin en envasos amb tapa per evitar vessaments sobre l\'equipament.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rule-item"><b>Neteja:</b> Cada usuari és responsable de deixar el seu espai net i recollit en finalitzar la reserva.</div>', unsafe_allow_html=True)
    
    st.warning("L'incompliment d'aquestes normes pot comportar la cancel·lació de la reserva sense dret a reemborsament.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB FAQS ---
with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander(t["faq1"]): st.write(t["faq1a"])
    with st.expander(t["faq2"]): st.write(t["faq2a"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB CONTACTE ---
with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("c_form"):
        st.text_input(t["name"])
        mail_c = st.text_input(t["email"])
        st.text_area("Message")
        if st.form_submit_button(t["contact_send"]):
            if not mail_c.strip():
                st.error(t["contact_error"])
            elif not is_valid_email(mail_c):
                st.error(t["email_error"])
            else:
                st.success("Sent!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB RESERVA ---
with tabs[6]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    st.markdown(f'<div style="color:red; font-weight:bold; margin-bottom:15px;">{t["cancel_warning"]}</div>', unsafe_allow_html=True)
    
    with st.form("b_form"):
        st.markdown("#### 1. Datos de Usuario")
        col_a, col_b = st.columns(2)
        n_v = col_a.text_input(t["name"])
        s_v = col_a.text_input(t["surname"])
        m_v = col_b.text_input(t["email"])
        # Campo de teléfono con instrucción de 9 cifras
        p_v = col_b.text_input(t["phone"])
        
        st.divider()
        st.markdown("#### 2. Detalles del Servicio")
        col_c, col_d = st.columns(2)
        with col_c:
            localizacion = st.selectbox(t["loc"], ["EEBE - Campus Besòs (UPC)", "Zona Universitària - Les Corts"])
            tipo_servicio = st.selectbox(t["space"], ["Cabina Privada", "Sala de Treball", "Zona Silenci", "Zona Confort"])
        with col_d:
            fecha = st.date_input(t["date"], min_value=date.today())
            h_v = st.slider(t["hours"], 1, 8, 2)
            
        st.write(f"### {t['price']}: {h_v * 3} €")
        
        if st.form_submit_button(t["booking_confirm"], use_container_width=True):
            if not n_v.strip() or not s_v.strip() or not m_v.strip() or not p_v.strip():
                st.error(t["booking_error"])
            elif not is_valid_email(m_v):
                st.error(t["email_error"])
            # VALIDACIÓN: Debe ser numérico Y tener exactamente 9 caracteres
            elif not p_v.isdigit() or len(p_v) != 9:
                st.error(t["phone_error"])
            else:
                st.success(f"{t['booking_ok']} - {localizacion}")
                st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
