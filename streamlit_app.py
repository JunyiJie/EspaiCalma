import streamlit as st
from datetime import date

st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTADO
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# TEXTOS (CAT/ESP/ENG)
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "Benvingut/da a EspaiCalma",
        "subtitle": "Espais tranquils i còmodes per estudiar o treballar, reservables per hores des d’una app o web.",
        "mvp": "MVP: demo de navegació + simulació de reserva (sense pagament real).",
        "spaces_title": "Espais i Serveis",
        "spaces_sub": "Tria l’espai que millor s’adapta a tu.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosaltres",
        "contact_title": "Contacte",
        "booking_title": "Reserva",
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada (demo).",
        "booking_info": "Aquesta acció pot comptar com a ‘reserva de prova’ per a les mètriques de l’experiment.",
        "loc": "Ubicació",
        "space": "Espai",
        "date": "Data",
        "hours": "Hores",
        "price": "Preu estimat",
        "name": "Nom",
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
        "contact_ok": "Missatge enviat (demo).",
    },
    "ESP": {
        "welcome": "Bienvenido/a a EspaiCalma",
        "subtitle": "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas desde una app o web.",
        "mvp": "MVP: demo de navegación + simulación de reserva (sin pago real).",
        "spaces_title": "Espacios y Servicios",
        "spaces_sub": "Elige el espacio que mejor se adapte a ti.",
        "faqs_title": "FAQs",
        "about_title": "Sobre Nosotros",
        "contact_title": "Contacto",
        "booking_title": "Reserva",
        "contact_send": "Enviar",
        "booking_confirm": "Confirmar reserva",
        "booking_ok": "✅ Reserva simulada (demo).",
        "booking_info": "Esta acción puede contar como ‘reserva de prueba’ para las métricas del experimento.",
        "loc": "Ubicación",
        "space": "Espacio",
        "date": "Fecha",
        "hours": "Horas",
        "price": "Precio estimado",
        "name": "Nombre",
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
        "contact_ok": "Mensaje enviado (demo).",
    },
    "ENG": {
        "welcome": "Welcome to EspaiCalma",
        "subtitle": "Quiet, comfortable spaces to study or work, bookable by the hour from an app or web.",
        "mvp": "MVP: navigation demo + booking simulation (no real payment).",
        "spaces_title": "Spaces & Services",
        "spaces_sub": "Pick the space that fits you best.",
        "faqs_title": "FAQs",
        "about_title": "About Us",
        "contact_title": "Contact",
        "booking_title": "Booking",
        "contact_send": "Send",
        "booking_confirm": "Confirm booking",
        "booking_ok": "✅ Booking simulated (demo).",
        "booking_info": "This action can count as a ‘test booking’ for your experiment metrics.",
        "loc": "Location",
        "space": "Space",
        "date": "Date",
        "hours": "Hours",
        "price": "Estimated price",
        "name": "Name",
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
# ESTILO (mockup)
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(
    f"""
<style>
/* Fondo */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,.34), rgba(0,0,0,.34)),
    url("{BG}");
  background-size: cover;
  background-position: center;
}}

/* Ocultar barra de Streamlit */
header {{visibility:hidden;}}
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}

/* Contenedor centrado */
.ec-wrap {{
  max-width: 1200px;
  margin: 50px auto;
  padding: 0 30px;
}}

/* Título estilo portada */
.ec-hero-title {{
  font-size: 66px;
  font-weight: 1000;
  color: white;
  margin: 0 0 6px 0;
  text-shadow: 0 10px 30px rgba(0,0,0,.35);
}}
.ec-hero-sub {{
  font-size: 30px;
  color: rgba(255,255,255,.92);
  margin: 0 0 20px 0;
  text-shadow: 0 10px 30px rgba(0,0,0,.35);
}}

/* Tarjeta blanca translúcida */
.ec-card {{
  background: rgba(255,255,255,.88);
  border-radius: 16px;
  box-shadow: 0 18px 55px rgba(0,0,0,.18);
  padding: 22px 24px;
}}

/* Tabs como botones */
.stTabs [data-baseweb="tab-list"] {{
  gap: 10px;
  flex-wrap: wrap;
}}
.stTabs [data-baseweb="tab"] {{
  background: rgba(0,0,0,.30);
  border-radius: 14px;
  padding: 10px 14px;
  color: white;
  border: 1px solid rgba(255,255,255,.12);
}}
.stTabs [aria-selected="true"] {{
  background: rgba(201,173,120,.95);
  color: #1b1f24;
  border: 1px solid rgba(0,0,0,.06);
  font-weight: 1000;
}}

/* Botones idioma compactos */
.ec-lang button {{
  border-radius: 12px !important;
  font-weight: 800 !important;
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
    if st.button("CAT", use_container_width=True, key="lang_cat"):
        st.session_state.lang = "CAT"
with c2:
    if st.button("ESP", use_container_width=True, key="lang_esp"):
        st.session_state.lang = "ESP"
with c3:
    if st.button("ENG", use_container_width=True, key="lang_eng"):
        st.session_state.lang = "ENG"

lang = st.session_state.lang
t = TXT[lang]

st.markdown(f'<div class="ec-hero-title">{t["welcome"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ec-hero-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)

# ---------------------------
# NAVEGACIÓN (pestañas SIEMPRE visibles)
# ---------------------------
tab_inici, tab_spaces, tab_faqs, tab_about, tab_contact, tab_booking = st.tabs(
    ["🏠 Inici", "🌿 Espais i Serveis", "❓ FAQs", "ℹ️ Sobre", "✉️ Contacte", "🗓️ Reserva"]
)

# ---------------------------
# CONTENIDO
# ---------------------------
with tab_inici:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.write(
        "• Wi-Fi estable\n• Silenci real\n• Taula + cadira ergonòmica\n• Reserva ràpida"
        if lang == "CAT"
        else "• Wi-Fi estable\n• Silencio real\n• Mesa + silla ergonómica\n• Reserva rápida"
        if lang == "ESP"
        else "• Stable Wi-Fi\n• Real quiet\n• Desk + ergonomic chair\n• Fast booking"
    )
    st.markdown("</div>", unsafe_allow_html=True)

with tab_spaces:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["spaces_title"])
    st.caption(t["spaces_sub"])

    a, b, c = st.columns(3)
    with a:
        st.image(
            "https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=70",
            caption="Sala privada (1)",
        )
        st.caption("Wi-Fi • Silenci • Endolls" if lang != "ENG" else "Wi-Fi • Quiet • Outlets")
    with b:
        st.image(
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=70",
            caption="Sala petita (2)",
        )
        st.caption("Ideal per reunions" if lang == "CAT" else "Ideal para reuniones" if lang == "ESP" else "Great for meetings")
    with c:
        st.image(
            "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=70",
            caption="Llum natural" if lang == "CAT" else "Luz natural" if lang == "ESP" else "Natural light",
        )
        st.caption("Ventilació • Confort" if lang == "CAT" else "Ventilación • Confort" if lang == "ESP" else "Ventilation • Comfort")

    st.subheader(t["pricing"])
    st.write(
        "• 3 € / hora\n• 30 € / mes (accés il·limitat a certs espais)"
        if lang == "CAT"
        else "• 3 € / hora\n• 30 € / mes (acceso ilimitado a ciertos espacios)"
        if lang == "ESP"
        else "• 3 € / hour\n• 30 € / month (unlimited access to selected spaces)"
    )
    st.markdown("</div>", unsafe_allow_html=True)

with tab_faqs:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["faqs_title"])
    with st.expander(t["faq1"]):
        st.write(t["faq1a"])
    with st.expander(t["faq2"]):
        st.write(t["faq2a"])
    with st.expander(t["faq3"]):
        st.write(t["faq3a"])
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
        sent = st.form_submit_button(t["contact_send"])
    if sent:
        st.success(t["contact_ok"])
    st.markdown("</div>", unsafe_allow_html=True)

with tab_booking:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])

    with st.form("booking_form"):
        loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
        sp = st.selectbox(t["space"], ["Sala privada (1)", "Sala petita (2)", "Llum natural"])
        st.date_input(t["date"], value=date.today())
        h = st.slider(t["hours"], 1, 8, 2)

        price_per_hour = 3
        st.write(f'{t["price"]}: **{h * price_per_hour} €** ({price_per_hour} €/hora)' if lang != "ENG"
                 else f'{t["price"]}: **{h * price_per_hour} €** ({price_per_hour} €/hour)')

        ok = st.form_submit_button(t["booking_confirm"])

    if ok:
        st.success(t["booking_ok"])
        st.info(t["booking_info"])

    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

