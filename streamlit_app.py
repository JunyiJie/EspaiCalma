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
        "welcome": "Benvingut/da a EspaiCalma",
        "subtitle": "Espais tranquils i còmodes per estudiar o treballar.",
        "mvp": "MVP: demo de navegació + simulació de reserva.",
        "spaces_title": "Espais i Serveis",
        "spaces_sub": "Tria l’espai que millor s’adapta a tu.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosaltres",
        "contact_title": "Contacte",
        "booking_title": "Reserva el teu espai",
        "contact_send": "Enviar Missatge",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit!",
        "booking_error": "❌ Error: Has d'emplenar Nom, Cognoms, Email i Telèfon per reservar.",
        "booking_info": "Aquesta acció és una prova per a l'experiment del projecte.",
        "cancel_warning": "⚠️ Avís: Si passats 10 minuts de l'hora de reserva no hi ha ningú a l'aula, la reserva es cancel·larà automàticament.",
        "loc": "Ubicació",
        "space": "Tipus d'Espai",
        "date": "Data",
        "hours": "Quantes hores?",
        "price": "Preu estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Correu electrònic",
        "phone": "Telèfon",
        "message": "El teu missatge",
        "pricing": "Tarifes",
        "faq1": "Com funciona la reserva?",
        "faq1a": "Selecciona ubicació, data i hores. Un cop confirmis les dades, rebràs una confirmació digital.",
        "faq2": "Hi ha horaris especials?",
        "faq2a": "En períodes d'exàmens ampliem l'horari fins a la matinada segons la demanda dels usuaris.",
        "faq3": "Què inclou el preu?",
        "faq3a": "Accés a Wi-Fi 6, cafè/aigua gratuïts, cadira ergonòmica i un ambient de silenci rigorós.",
        "about1": "Som un projecte creat per a estudiants i nòmades digitals que busquen un refugi de concentració.",
        "about2": "El nostre objectiu és oferir un espai on el silenci i la comoditat estiguin garantits.",
    },
    "ESP": {
        "welcome": "Bienvenido/a a EspaiCalma",
        "subtitle": "Espacios tranquilos y cómodos para estudiar o trabajar.",
        "mvp": "MVP: demo de navegación + simulación de reserva.",
        "spaces_title": "Espacios y Servicios",
        "spaces_sub": "Elige el espacio que mejor se adapte a ti.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosotros",
        "contact_title": "Contacto",
        "booking_title": "Reserva tu espacio",
        "contact_send": "Enviar Mensaje",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ ¡Reserva simulada con éxito!",
        "booking_error": "❌ Error: Debes rellenar Nombre, Apellidos, Email y Teléfono para reservar.",
        "booking_info": "Esta acción es una prueba para el experimento del proyecto.",
        "cancel_warning": "⚠️ Aviso: Si pasados 10 minutos de la hora de reserva no hay nadie en el aula, la reserva se cancelará automáticamente.",
        "loc": "Ubicación",
        "space": "Tipo de Espacio",
        "date": "Fecha",
        "hours": "¿Cuántas horas?",
        "price": "Precio estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Correo electrónico",
        "phone": "Teléfono",
        "message": "Tu mensaje",
        "pricing": "Tarifas",
        "faq1": "¿Cómo funciona la reserva?",
        "faq1a": "Selecciona ubicación, fecha y horas. Al confirmar, recibirás una confirmación digital.",
        "faq2": "¿Hay horarios especiales?",
        "faq2a": "En periodos de exámenes ampliamos el horario hasta la madrugada según la demanda.",
        "faq3": "¿Qué incluye el precio?",
        "faq3a": "Acceso a Wi-Fi 6, café/agua gratis, silla ergonómica y un ambiente de silencio riguroso.",
        "about1": "Somos un proyecto creado para estudiantes y nómadas digitales que buscan concentración.",
        "about2": "Nuestro objetivo es ofrecer un espacio donde el silencio y la comodidad estén garantizados.",
    },
    "ENG": {
        "welcome": "Welcome to EspaiCalma",
        "subtitle": "Quiet, comfortable spaces to study or work.",
        "mvp": "MVP: navigation demo + booking simulation.",
        "spaces_title": "Spaces & Services",
        "spaces_sub": "Pick the space that fits you best.",
        "faqs_title": "FAQs",
        "about_title": "About Us",
        "contact_title": "Contact",
        "booking_title": "Book your space",
        "contact_send": "Send Message",
        "booking_confirm": "Confirm booking",
        "booking_ok": "✅ Booking successful (demo)!",
        "booking_error": "❌ Error: You must fill in Name, Surname, Email, and Phone to book.",
        "booking_info": "This action is a test for the project experiment.",
        "cancel_warning": "⚠️ Notice: If no one is in the room 10 minutes after the booking time, the reservation will be automatically cancelled.",
        "loc": "Location",
        "space": "Space Type",
        "date": "Date",
        "hours": "How many hours?",
        "price": "Estimated price",
        "name": "First Name",
        "surname": "Last Name",
        "email": "Email",
        "phone": "Phone number",
        "message": "Your message",
        "pricing": "Pricing",
        "faq1": "How does booking work?",
        "faq1a": "Choose location, date, and hours. Once confirmed, you will receive a digital confirmation.",
        "faq2": "Are there special hours?",
        "faq2a": "During exam periods, we extend our hours until late at night based on demand.",
        "faq3": "What's included?",
        "faq3a": "High-speed Wi-Fi 6, free coffee/water, ergonomic chair, and a strict quiet environment.",
        "about1": "A project designed for students and digital nomads seeking a focus sanctuary.",
        "about2": "Our goal is to provide a space where silence and comfort are guaranteed.",
    },
}

# ---------------------------
# ESTILS CSS (Fonts i Contrast)
# ---------------------------
BG_URL = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), url("{BG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    html, body, [class*="st-"] {{
        font-size: 1.15rem;
    }}
    .hero-title {{
        font-size: 72px; font-weight: 800; color: white;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.7); margin-bottom: 0px;
    }}
    .hero-sub {{
        font-size: 32px; color: #f1f1f1;
        text-shadow: 1px 1px 10px rgba(0,0,0,0.7); margin-bottom: 40px;
    }}
    .ec-card {{
        background: rgba(255, 255, 255, 0.98);
        padding: 40px; border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        color: #1a1a1a; border: 1px solid #ddd;
    }}
    .warning-text {{
        color: #D32F2F; font-weight: bold; padding: 15px;
        border: 2px solid #D32F2F; border-radius: 10px;
        background-color: #FFEBEE; margin-bottom: 25px;
    }}
    .stTabs [data-baseweb="tab-list"] button p {{
        font-size: 1.3rem; font-weight: bold;
    }}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SELECTOR D'IDIOMA
# ---------------------------
c_l1, c_l2, c_l3, _ = st.columns([1, 1, 1, 6])
with c_l1:
    if st.button("CAT", use_container_width=True): st.session_state.lang = "CAT"; st.rerun()
with c_l2:
    if st.button("ESP", use_container_width=True): st.session_state.lang = "ESP"; st.rerun()
with c_l3:
    if st.button("ENG", use_container_width=True): st.session_state.lang = "ENG"; st.rerun()

lang = st.session_state.lang
t = TXT[lang]

# ---------------------------
# TITULAR
# ---------------------------
st.markdown(f'<h1 class="hero-title">{t["welcome"]}</h1>', unsafe_allow_html=True)
st.markdown(f'<p class="hero-sub">{t["subtitle"]}</p>', unsafe_allow_html=True)

# ---------------------------
# NAVEGACIÓ (TABS)
# ---------------------------
tabs = st.tabs(["🏠 Inici", "🌿 Espais", "❓ FAQs", "ℹ️ Sobre", "✉️ Contacte", "🗓️ Reserva"])

# --- TAB INICI ---
with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.markdown("### Què ens fa diferents?")
    st.markdown("- **Concentració:** Silenci garantit per contracte.\n- **Tecnologia:** Connexió simètrica de fibra òptica.\n- **Ubicació:** Al cor dels barris més actius.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB ESPAIS ---
with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    st.write(t["spaces_sub"])
    col1, col2, col3 = st.columns(3)
    with col1: st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=400", caption="Sala Privada")
    with col2: st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=400", caption="Zona Cowork")
    with col3: st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?w=400", caption="Llum Natural")
    
    st.divider()
    st.markdown(f"### {t['pricing']}: **3 € / hora**")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB FAQS ---
with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander(t["faq1"]): st.write(t["faq1a"])
    with st.expander(t["faq2"]): st.write(t["faq2a"])
    with st.expander(t["faq3"]): st.write(t["faq3a"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB SOBRE ---
with tabs[3]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["about_title"])
    st.write(t["about1"])
    st.write(t["about2"])
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB CONTACTE ---
with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("contact_form"):
        st.text_input(t["name"])
        st.text_input("Email")
        st.text_area(t["message"])
        if st.form_submit_button(t["contact_send"]):
            st.success("Missatge enviat correctament.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- TAB RESERVA (AMB VALIDACIÓ) ---
with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    st.markdown(f'<div class="warning-text">{t["cancel_warning"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form"):
        st.markdown("#### 👤 1. Dades de l'usuari")
        b_c1, b_c2 = st.columns(2)
        with b_c1:
            nom_res = st.text_input(t["name"], placeholder="Joan")
            cog_res = st.text_input(t["surname"], placeholder="Pou Vila")
        with b_c2:
            mail_res = st.text_input(t["email"], placeholder="joan@exemple.com")
            tel_res = st.text_input(t["phone"], placeholder="600 000 000")

        st.divider()
        st.markdown("#### 📍 2. Detalls del lloguer")
        b_c3, b_c4 = st.columns(2)
        with b_c3:
            loc_res = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
            sp_res = st.selectbox(t["space"], ["Sala privada", "Sala petita", "Llum natural"])
        with b_c4:
            data_res = st.date_input(t["date"], value=date.today())
            hores_res = st.slider(t["hours"], 1, 10, 2)

        # Preu dinàmic
        preu_h = 3
        total = hores_res * preu_h
        st.markdown(f"### {t['price']}: **{total} €**")

        btn_confirmar = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    # Validació estricte al prémer el botó
    if btn_confirmar:
        if nom_res.strip() == "" or cog_res.strip() == "" or mail_res.strip() == "" or tel_res.strip() == "":
            st.error(t["booking_error"])
        else:
            st.success(t["booking_ok"])
            st.info(t["booking_info"])
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)
