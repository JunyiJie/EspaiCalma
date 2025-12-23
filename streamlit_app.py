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
        "booking_error": "❌ Error: Has d'emplenar tots els camps de contacte (Nom, Cognoms, Email i Telèfon) per poder reservar.",
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
        "booking_error": "❌ Error: Debes rellenar todos los campos de contacto (Nombre, Apellidos, Email y Teléfono) para poder reservar.",
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
        "booking_error": "❌ Error: You must fill in all contact fields (Name, Surname, Email, and Phone) to book.",
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
    },
}

# ---------------------------
# ESTILO
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(
    f"""
<style>
.stApp {{
    background: linear-gradient(rgba(0,0,0,.65), rgba(0,0,0,.65)), url("{BG}");
    background-size: cover;
    background-position: center;
}}
html, body, [class*="st-"] {{ font-size: 1.15rem; }}
.ec-hero-title {{
    font-size: 72px; font-weight: 800; color: #FFFFFF;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.8); margin-bottom: 10px;
}}
.ec-hero-sub {{
    font-size: 34px; color: #F0F0F0;
    text-shadow: 1px 1px 8px rgba(0,0,0,0.8); margin-bottom: 30px;
}}
.ec-card {{
    background: rgba(255, 255, 255, 0.98);
    color: #1A1A1A; border-radius: 20px; padding: 35px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.4); border: 1px solid #ddd;
}}
.warning-text {{
    color: #D32F2F; font-weight: bold; padding: 15px;
    border: 2px solid #D32F2F; border-radius: 10px;
    background-color: #FFEBEE; margin-bottom: 25px;
    font-size: 1.2rem;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------
# HEADER
# ---------------------------
c1, c2, c3, _ = st.columns([1, 1, 1, 6])
with c1:
    if st.button("CAT", use_container_width=True): st.session_state.lang = "CAT"; st.rerun()
with c2:
    if st.button("ESP", use_container_width=True): st.session_state.lang = "ESP"; st.rerun()
with c3:
    if st.button("ENG", use_container_width=True): st.session_state.lang = "ENG"; st.rerun()

lang = st.session_state.lang
t = TXT[lang]

st.markdown(f'<div class="ec-hero-title">{t["welcome"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ec-hero-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)

# ---------------------------
# NAVEGACIÓN
# ---------------------------
tabs = st.tabs(["🏠 Inici", "🌿 Espais", "❓ FAQs", "ℹ️ Sobre", "✉️ Contacte", "🗓️ Reserva"])

with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.markdown("### Característiques\n- **Wi-Fi 6**\n- **Silenci total**\n- **Reserva en 1 min**")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    
    # Aviso de los 10 minutos
    st.markdown(f'<div class="warning-text">{t["cancel_warning"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form"):
        st.markdown("#### 1. Dades de contacte")
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input(t["name"])
            cognom = st.text_input(t["surname"])
        with col2:
            email = st.text_input(t["email"])
            tlf = st.text_input(t["phone"])
            
        st.divider()
        st.markdown("#### 2. Detalls de la reserva")
        col3, col4 = st.columns(2)
        with col3:
            loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
            sp = st.selectbox(t["space"], ["Sala privada", "Sala petita", "Llum natural"])
        with col4:
            st.date_input(t["date"], value=date.today())
            h = st.slider(t["hours"], 1, 8, 2)

        # Cálculo dinámico del precio
        price_total = h * 3
        st.markdown(f"### {t['price']}: {price_total} €")
        
        submit = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    # --- LÓGICA DE VALIDACIÓN ---
    if submit:
        # Verificamos que todos los campos de texto tengan contenido (no estén vacíos)
        if nom.strip() == "" or cognom.strip() == "" or email.strip() == "" or tlf.strip() == "":
            st.error(t["booking_error"])
        else:
            st.success(t["booking_ok"])
            st.info(t["booking_info"])
            st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)
