import streamlit as st
from datetime import date

# Configuració de la pàgina
st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTAT DE LA SESSIÓ (Idioma)
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# DICCIONARI DE TEXTOS
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "Benvingut/da a EspaiCalma",
        "subtitle": "Espais tranquils i còmodes per estudiar o treballar.",
        "mvp": "MVP: demo de navegació + simulació de reserva (sense pagament real).",
        "spaces_title": "Espais i Serveis",
        "spaces_sub": "Tria l’espai que millor s’adapta a tu.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosaltres",
        "contact_title": "Contacte",
        "booking_title": "Reserva el teu espai",
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit!",
        "booking_info": "Aquesta acció compta com a 'reserva de prova' per a les mètriques de l’experiment.",
        "cancel_warning": "⚠️ ATENCIÓ: Si passats 10 minuts de l'hora de reserva no hi ha ningú a l'aula, la reserva es cancel·larà automàticament.",
        "loc": "Ubicació",
        "space": "Espai",
        "date": "Data de reserva",
        "hours": "Quantes hores necessites?",
        "price": "Preu estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Correu electrònic",
        "phone": "Telèfon de contacte",
        "message": "Missatge",
        "pricing": "Tarifes",
        "faq1": "Com funciona la reserva?",
        "faq1a": "Selecciona ubicació, data i hores. Confirma i reps una confirmació (demo).",
        "faq2": "Hi ha horaris nocturns?",
        "faq2a": "En fase pilot es poden ampliar horaris en períodes d’exàmens segons demanda.",
        "faq3": "Què inclou l’espai?",
        "faq3a": "Wi-Fi, taula, cadira ergonòmica, endolls i ambient tranquil.",
        "about1": "Projecte orientat a estudiants i joves professionals que necessiten concentració fora de casa.",
        "about2": "Objectiu: reduir soroll i distraccions i facilitar una reserva simple i ràpida.",
        "contact_ok": "Missatge enviat correctament (demo).",
    },
    "ESP": {
        "welcome": "Bienvenido/a a EspaiCalma",
        "subtitle": "Espacios tranquilos y cómodos para estudiar o trabajar.",
        "mvp": "MVP: demo de navegación + simulación de reserva (sin pago real).",
        "spaces_title": "Espacios y Servicios",
        "spaces_sub": "Elige el espacio que mejor se adapte a ti.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosotros",
        "contact_title": "Contacto",
        "booking_title": "Reserva tu espacio",
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ ¡Reserva simulada con éxito!",
        "booking_info": "Esta acción cuenta como 'reserva de prueba' para las métricas del experimento.",
        "cancel_warning": "⚠️ ATENCIÓN: Si pasados 10 minutos de la hora de reserva no hay nadie en el aula, la reserva se cancelará automáticamente.",
        "loc": "Ubicación",
        "space": "Espacio",
        "date": "Fecha de reserva",
        "hours": "¿Cuántas horas necesitas?",
        "price": "Precio estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Correo electrónico",
        "phone": "Teléfono de contacto",
        "message": "Mensaje",
        "pricing": "Tarifas",
        "faq1": "¿Cómo funciona la reserva?",
        "faq1a": "Selecciona ubicación, fecha y horas. Confirma y recibes una confirmación (demo).",
        "faq2": "¿Hay horarios nocturnos?",
        "faq2a": "En fase piloto se pueden ampliar horarios en periodos de exámenes según demanda.",
        "faq3": "¿Qué incluye el espacio?",
        "faq3a": "Wi-Fi, mesa, silla ergonómica, enchufes y ambiente tranquilo.",
        "about1": "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración fuera de casa.",
        "about2": "Objetivo: reducir ruido y distracciones y facilitar una reserva simple y rápida.",
        "contact_ok": "Mensaje enviado correctamente (demo).",
    },
    "ENG": {
        "welcome": "Welcome to EspaiCalma",
        "subtitle": "Quiet, comfortable spaces to study or work.",
        "mvp": "MVP: navigation demo + booking simulation (no real payment).",
        "spaces_title": "Spaces & Services",
        "spaces_sub": "Pick the space that fits you best.",
        "faqs_title": "FAQs",
        "about_title": "About Us",
        "contact_title": "Contact",
        "booking_title": "Book your space",
        "contact_send": "Send",
        "booking_confirm": "Confirm booking",
        "booking_ok": "✅ Booking simulated successfully!",
        "booking_info": "This action counts as a 'test booking' for experiment metrics.",
        "cancel_warning": "⚠️ NOTICE: If no one is in the room 10 minutes after the booking time, the reservation will be automatically cancelled.",
        "loc": "Location",
        "space": "Space",
        "date": "Booking date",
        "hours": "How many hours?",
        "price": "Estimated price",
        "name": "First Name",
        "surname": "Last Name",
        "email": "Email address",
        "phone": "Phone number",
        "message": "Message",
        "pricing": "Pricing",
        "faq1": "How does booking work?",
        "faq1a": "Choose location, date and hours. Confirm and get a demo confirmation.",
        "faq2": "Do you offer night hours?",
        "faq2a": "During the pilot, hours can be extended in exam periods depending on demand.",
        "faq3": "What's included?",
        "faq3a": "Wi-Fi, desk, ergonomic chair, power outlets, and a quiet atmosphere.",
        "about1": "A project for students and young professionals who need focus outside home.",
        "about2": "Goal: reduce noise/distractions and make booking simple and fast.",
        "contact_ok": "Message sent (demo).",
    },
}

# ---------------------------
# ESTIL PERSONALITZAT (CSS)
# ---------------------------
BG_URL = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(f"""
<style>
    /* Fons amb capa fosca per contrast */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), url("{BG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Estil de les fonts globals */
    html, body, [class*="st-"] {{
        font-size: 1.15rem;
        color: #1a1a1a;
    }}

    /* Títols Hero */
    .hero-title {{
        font-size: 4.5rem;
        font-weight: 800;
        color: white;
        text-shadow: 2px 4px 15px rgba(0,0,0,0.5);
        margin-bottom: 0px;
    }}
    .hero-sub {{
        font-size: 1.8rem;
        color: #f1f1f1;
        margin-bottom: 40px;
        text-shadow: 1px 2px 10px rgba(0,0,0,0.5);
    }}

    /* Targetes de contingut (Alt contrast) */
    .ec-card {{
        background: rgba(255, 255, 255, 0.97);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        border: 1px solid #e0e0e0;
    }}

    /* Tabs (Botons de navegació) */
    .stTabs [data-baseweb="tab-list"] {{ gap: 15px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255,255,255,0.1);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 600;
    }}
    .stTabs [aria-selected="true"] {{
        background: #C9AD78 !important;
        color: #1a1a1a !important;
    }}

    /* Preu destacat */
    .price-box {{
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #C9AD78;
        margin: 20px 0;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SELECCIÓ D'IDIOMA
# ---------------------------
col_l1, col_l2, col_l3, _ = st.columns([1, 1, 1, 6])
with col_l1:
    if st.button("CAT", use_container_width=True): 
        st.session_state.lang = "CAT"; st.rerun()
with col_l2:
    if st.button("ESP", use_container_width=True): 
        st.session_state.lang = "ESP"; st.rerun()
with col_l3:
    if st.button("ENG", use_container_width=True): 
        st.session_state.lang = "ENG"; st.rerun()

lang = st.session_state.lang
t = TXT[lang]

# ---------------------------
# HERO SECTION
# ---------------------------
st.markdown(f'<h1 class="hero-title">{t["welcome"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-sub">{t["subtitle"]}</p>', unsafe_allow_html=True)

# ---------------------------
# NAVEGACIÓ PRINCIPAL
# ---------------------------
tab_home, tab_spaces, tab_faqs, tab_about, tab_contact, tab_booking = st.tabs(
    ["🏠 Inici", "🌿 Espais", "❓ FAQs", "ℹ️ Sobre", "✉️ Contacte", "🗓️ Reserva"]
)

with tab_home:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.markdown("### Què oferim?")
    st.markdown(f"""
    - **Silenci Absolut:** Zones de treball lliures de soroll.
    - **Connectivitat:** Fibra òptica d'alta velocitat i endolls individuals.
    - **Flexibilitat:** Reserva només les hores que necessitis.
    - **Ubicacions Clau:** Prop de les principals zones d'estudi.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

with tab_spaces:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400", caption="Sala Privada")
    with col2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400", caption="Zona Coworking")
    with col3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?w=400", caption="Zona Llum Natural")
    
    st.markdown(f"### {t['pricing']}")
    st.write("• 3 € / hora")
    st.write("• 30 € / abonament mensual (accés limitat)")
    st.markdown("</div>", unsafe_allow_html=True)

with tab_faqs:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander(t["faq1"]): st.write(t["faq1a"])
    with st.expander(t["faq2"]): st.write(t["faq2a"])
    with st.expander(t["faq3"]): st.write(t["faq3a"])
    st.markdown("</div>", unsafe_allow_html=True)

with tab_about:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["about_title"])
    st.write(t["about1"])
    st.write(t["about2"])
    st.markdown("</div>", unsafe_allow_html=True)

with tab_contact:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("contact_form"):
        st.text_input(t["name"])
        st.text_input("Email")
        st.text_area(t["message"])
        if st.form_submit_button(t["contact_send"]):
            st.success(t["contact_ok"])
    st.markdown("</div>", unsafe_allow_html=True)

with tab_booking:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    
    # Avís important
    st.warning(t["cancel_warning"])

    with st.form("booking_form"):
        # Secció de Dades Personals
        st.markdown(f"#### 👤 1. Dades de contacte")
        c1, c2 = st.columns(2)
        with c1:
            u_nom = st.text_input(t["name"], placeholder="Ex: Marc")
            u_cog = st.text_input(t["surname"], placeholder="Ex: Vila Pou")
        with c2:
            u_mail = st.text_input(t["email"], placeholder="correu@exemple.com")
            u_tel = st.text_input(t["phone"], placeholder="+34 600 00 00 00")
        
        st.write("---")
        
        # Secció de l'Espai
        st.markdown(f"#### 📍 2. Detalls de la reserva")
        c3, c4 = st.columns(2)
        with c3:
            loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
            sp = st.selectbox(t["space"], ["Sala Privada", "Zona Coworking", "Zona Llum Natural"])
        with c4:
            data_res = st.date_input(t["date"], value=date.today())
            hores_res = st.slider(t["hours"], 1, 12, 2)

        # CÀLCUL DINÀMIC DEL PREU (S'actualitza amb el slider)
        preu_per_hora = 3
        total_preu = hores_res * preu_per_hora
        
        st.markdown(f"""
            <div class="price-box">
                <p style="margin:0; font-size: 1.2rem; color: #555;">{t['price']}</p>
                <p style="margin:0; font-size: 2.8rem; font-weight: 800; color: #1a1a1a;">{total_preu} €</p>
                <p style="margin:0; font-size: 0.9rem; color: #888;">({hores_res}h x {preu_per_hora}€/h)</p>
            </div>
        """, unsafe_allow_html=True)

        confirmar = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    if confirmar:
        if u_nom and u_cog and u_mail and u_tel:
            st.success(f"{t['booking_ok']} Gràcies, {u_nom}.")
            st.info(t["booking_info"])
            st.balloons()
        else:
            st.error("Si us plau, omple tots els camps del formulari.")
    
    st.markdown("</div>", unsafe_allow_html=True)
