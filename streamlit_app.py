import streamlit as st
from datetime import date

st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTADO
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# TEXTOS ACTUALIZADOS
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
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada amb èxit.",
        "booking_info": "Aquesta acció és una prova per a l'experiment.",
        "cancel_warning": "⚠️ Avís: Si passats 10 minuts de l'hora de reserva no hi ha ningú a l'aula, la reserva es cancel·larà automàticament.",
        "loc": "Ubicació",
        "space": "Espai",
        "date": "Data",
        "hours": "Hores",
        "price": "Preu estimat",
        "name": "Nom",
        "surname": "Cognoms",
        "email": "Correu electrònic",
        "phone": "Telèfon",
        "message": "Missatge",
        "pricing": "Tarifes",
        "faq1": "Com funciona la reserva?",
        "faq1a": "Selecciona ubicació, data i hores. Confirma i reps una confirmació (demo).",
        "faq2": "Hi ha horaris nocturns?",
        "faq2a": "En fase pilot es poden ampliar horaris en períodes d’exàmens segons demanda.",
        "faq3": "Què inclou l’espai?",
        "faq3a": "Wi-Fi, taula, cadira ergonòmica, endolls i ambient tranquil.",
        "about1": "Projecte orientat a estudiants i joves professionals que necessiten concentració.",
        "about2": "Objectiu: reduir soroll i distraccions.",
        "contact_ok": "Missatge enviat (demo).",
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
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada con éxito.",
        "booking_info": "Esta acción es una prueba para el experimento.",
        "cancel_warning": "⚠️ Aviso: Si pasados 10 minutos de la hora de reserva no hay nadie en el aula, la reserva se cancelará automáticamente.",
        "loc": "Ubicación",
        "space": "Espacio",
        "date": "Fecha",
        "hours": "Horas",
        "price": "Precio estimado",
        "name": "Nombre",
        "surname": "Apellidos",
        "email": "Correo electrónico",
        "phone": "Teléfono",
        "message": "Mensaje",
        "pricing": "Tarifas",
        "faq1": "¿Cómo funciona la reserva?",
        "faq1a": "Selecciona ubicación, fecha y horas. Confirma y recibes una confirmación (demo).",
        "faq2": "¿Hay horarios nocturnos?",
        "faq2a": "En fase pilot se pueden ampliar horarios en periodos de exámenes según demanda.",
        "faq3": "¿Qué incluye el espacio?",
        "faq3a": "Wi-Fi, mesa, silla ergonómica, enchufes y ambiente tranquilo.",
        "about1": "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración.",
        "about2": "Objetivo: reducir ruido y distracciones.",
        "contact_ok": "Mensaje enviado (demo).",
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
        "contact_send": "Send",
        "booking_confirm": "Confirm booking",
        "booking_ok": "✅ Booking successful (demo).",
        "booking_info": "This action is a test for the experiment.",
        "cancel_warning": "⚠️ Notice: If no one is in the room after 10 minutes of the booking time, the reservation will be automatically cancelled.",
        "loc": "Location",
        "space": "Space",
        "date": "Date",
        "hours": "Hours",
        "price": "Estimated price",
        "name": "First Name",
        "surname": "Last Name",
        "email": "Email",
        "phone": "Phone number",
        "message": "Message",
        "pricing": "Pricing",
        "faq1": "How does booking work?",
        "faq1a": "Choose location, date and hours. Confirm and get a demo confirmation.",
        "faq2": "Do you offer night hours?",
        "faq2a": "During the pilot, hours can be extended in exam periods depending on demand.",
        "faq3": "What's included?",
        "faq3a": "Wi-Fi, desk, ergonomic chair, power outlets, and a quiet atmosphere.",
        "about1": "A project for students and young professionals who need focus.",
        "about2": "Goal: reduce noise and distractions.",
        "contact_ok": "Message sent (demo).",
    },
}

# ---------------------------
# ESTILO MEJORADO (CONTRASTE Y FUENTE)
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(
    f"""
<style>
/* Fondo con overlay más oscuro para mejorar contraste */
.stApp {{
    background: linear-gradient(rgba(0,0,0,.60), rgba(0,0,0,.60)), url("{BG}");
    background-size: cover;
    background-position: center;
}}

/* Fuentes más grandes y legibles */
html, body, [class*="st-"] {{
    font-size: 1.1rem;
}}

/* Títulos potentes */
.ec-hero-title {{
    font-size: 72px;
    font-weight: 800;
    color: #FFFFFF;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
    margin-bottom: 10px;
}}
.ec-hero-sub {{
    font-size: 34px;
    color: #F0F0F0;
    text-shadow: 1px 1px 8px rgba(0,0,0,0.8);
    margin-bottom: 30px;
}}

/* Tarjeta con máximo contraste */
.ec-card {{
    background: rgba(255, 255, 255, 0.98); /* Casi opaco */
    color: #1A1A1A;
    border-radius: 20px;
    padding: 35px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    border: 1px solid #ddd;
}}

/* Tabs más grandes */
.stTabs [data-baseweb="tab-list"] button p {{
    font-size: 1.3rem;
    font-weight: bold;
}}

/* Texto de advertencia */
.warning-text {{
    color: #D32F2F;
    font-weight: bold;
    padding: 10px;
    border: 2px solid #D32F2F;
    border-radius: 10px;
    background-color: #FFEBEE;
    margin-bottom: 20px;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------
# HEADER + IDIOMA
# ---------------------------
lang = st.session_state.lang
t = TXT[lang]

st.markdown('<div class="ec-wrap">', unsafe_allow_html=True)

c1, c2, c3, _ = st.columns([1, 1, 1, 6])
with c1:
    if st.button("CAT", use_container_width=True): st.session_state.lang = "CAT"; st.rerun()
with c2:
    if st.button("ESP", use_container_width=True): st.session_state.lang = "ESP"; st.rerun()
with c3:
    if st.button("ENG", use_container_width=True): st.session_state.lang = "ENG"; st.rerun()

st.markdown(f'<div class="ec-hero-title">{t["welcome"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ec-hero-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)

# ---------------------------
# NAVEGACIÓN
# ---------------------------
tabs = st.tabs(["🏠 Inici", "🌿 Espais", "❓ FAQs", "ℹ️ Sobre", "✉️ Contacte", "🗓️ Reserva"])

# ---------------------------
# CONTENIDO
# ---------------------------
with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.markdown(f"### {'Característiques' if lang != 'ENG' else 'Features'}")
    st.markdown("- **Wi-Fi 6** alta velocitat\n- **Silenci total** garantit\n- **Ergonomia**: Cadires d'oficina de gamma alta\n- **Reserva fàcil** en 1 minut")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    a, b, c = st.columns(3)
    with a: st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=400", caption="Sala privada")
    with b: st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=400", caption="Sala petita")
    with c: st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=400", caption="Llum natural")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander(t["faq1"]): st.write(t["faq1a"])
    with st.expander(t["faq2"]): st.write(t["faq2a"])
    with st.expander(t["faq3"]): st.write(t["faq3a"])
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["about_title"])
    st.write(t["about1"])
    st.write(t["about2"])
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["contact_title"])
    with st.form("contact_form"):
        st.text_input(t["name"])
        st.text_input("Email")
        st.text_area(t["message"])
        st.form_submit_button(t["contact_send"])
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    
    # Aviso de los 10 minutos
    st.markdown(f'<div class="warning-text">{t["cancel_warning"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input(t["name"])
            cognom = st.text_input(t["surname"])
        with col2:
            email = st.text_input(t["email"])
            tlf = st.text_input(t["phone"])
            
        st.divider()
        
        col3, col4 = st.columns(2)
        with col3:
            loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
            sp = st.selectbox(t["space"], ["Sala privada", "Sala petita", "Llum natural"])
        with col4:
            st.date_input(t["date"], value=date.today())
            h = st.slider(t["hours"], 1, 8, 2)

        price_total = h * 3
        st.markdown(f"### {t['price']}: {price_total} €")
        
        submit = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    if submit:
        if nom and cognom and email:
            st.success(t["booking_ok"])
            st.balloons()
        else:
            st.error("Si us plau, emplena les teves dades de contacte.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
