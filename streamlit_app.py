# app.py — EspaiCalma (Streamlit) con menú arriba a la izquierda (sidebar)
# Ejecuta: streamlit run app.py

import streamlit as st
from datetime import date

st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# ESTADO
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "Inici"
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

def go(p):
    st.session_state.page = p

# ---------------------------
# TEXTOS
# ---------------------------
TXT = {
    "CAT": {
        "welcome": "Benvingut/da a EspaiCalma",
        "subtitle": "Espais tranquils i còmodes per estudiar o treballar, reservables per hores des d’una app o web.",
        "mvp": "MVP: demo de navegació + simulació de reserva (sense pagament real).",
        "spaces": "Espais i Serveis",
        "faqs": "FAQs",
        "about": "Sobre Nosaltres",
        "contact": "Contacte",
        "booking": "Reserva",
        "pricing": "Tarifes",
        "send": "Enviar",
        "confirm": "Confirmar reserva",
        "ok": "✅ Reserva simulada (demo).",
        "info": "Aquesta acció pot comptar com a ‘reserva de prova’ per a les mètriques de l’experiment.",
        "loc": "Ubicació",
        "space": "Espai",
        "dt": "Data",
        "hours": "Hores",
        "price": "Preu estimat",
        "name": "Nom",
        "msg": "Missatge",
        "faq1": "Com funciona la reserva?",
        "faq1a": "Selecciona ubicació, data i hores. Confirma i reps una confirmació (demo).",
        "faq2": "Hi ha horaris nocturns?",
        "faq2a": "En fase pilot es poden ampliar horaris en períodes d’exàmens segons demanda.",
        "faq3": "Què inclou l’espai?",
        "faq3a": "Wi-Fi, taula, cadira ergonòmica, endolls i ambient tranquil.",
        "about1": "Projecte orientat a estudiants i joves professionals que necessiten concentració fora de casa.",
        "about2": "Objectiu: reduir soroll i distraccions i facilitar una reserva simple i ràpida.",
        "sent": "Missatge enviat (demo).",
    },
    "ESP": {
        "welcome": "Bienvenido/a a EspaiCalma",
        "subtitle": "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas desde una app o web.",
        "mvp": "MVP: demo de navegación + simulación de reserva (sin pago real).",
        "spaces": "Espacios y Servicios",
        "faqs": "FAQs",
        "about": "Sobre Nosotros",
        "contact": "Contacto",
        "booking": "Reserva",
        "pricing": "Tarifas",
        "send": "Enviar",
        "confirm": "Confirmar reserva",
        "ok": "✅ Reserva simulada (demo).",
        "info": "Esta acción puede contar como ‘reserva de prueba’ para las métricas del experimento.",
        "loc": "Ubicación",
        "space": "Espacio",
        "dt": "Fecha",
        "hours": "Horas",
        "price": "Precio estimado",
        "name": "Nombre",
        "msg": "Mensaje",
        "faq1": "¿Cómo funciona la reserva?",
        "faq1a": "Selecciona ubicación, fecha y horas. Confirma y recibes una confirmación (demo).",
        "faq2": "¿Hay horarios nocturnos?",
        "faq2a": "En fase piloto se pueden ampliar horarios en periodos de exámenes según demanda.",
        "faq3": "¿Qué incluye el espacio?",
        "faq3a": "Wi-Fi, mesa, silla ergonómica, enchufes y ambiente tranquilo.",
        "about1": "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración fuera de casa.",
        "about2": "Objetivo: reducir ruido y distracciones y facilitar una reserva simple y rápida.",
        "sent": "Mensaje enviado (demo).",
    },
    "ENG": {
        "welcome": "Welcome to EspaiCalma",
        "subtitle": "Quiet, comfortable spaces to study or work, bookable by the hour from an app or web.",
        "mvp": "MVP: navigation demo + booking simulation (no real payment).",
        "spaces": "Spaces & Services",
        "faqs": "FAQs",
        "about": "About Us",
        "contact": "Contact",
        "booking": "Booking",
        "pricing": "Pricing",
        "send": "Send",
        "confirm": "Confirm booking",
        "ok": "✅ Booking simulated (demo).",
        "info": "This action can count as a ‘test booking’ for your experiment metrics.",
        "loc": "Location",
        "space": "Space",
        "dt": "Date",
        "hours": "Hours",
        "price": "Estimated price",
        "name": "Name",
        "msg": "Message",
        "faq1": "How does booking work?",
        "faq1a": "Pick location, date and hours. Confirm and get a demo confirmation.",
        "faq2": "Do you offer night hours?",
        "faq2a": "In the pilot, hours can be extended during exam periods depending on demand.",
        "faq3": "What's included?",
        "faq3a": "Wi-Fi, desk, ergonomic chair, power outlets, and a quiet atmosphere.",
        "about1": "A project for students and young professionals who need focus outside home.",
        "about2": "Goal: reduce noise/distractions and make booking simple and fast.",
        "sent": "Message sent (demo).",
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
  background: linear-gradient(rgba(0,0,0,.34), rgba(0,0,0,.34)), url("{BG}");
  background-size: cover;
  background-position: center;
}}
header {{visibility:hidden;}}
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}

[data-testid="stSidebar"] {{
  background: transparent !important;
}}
/* Caja blanca del sidebar */
.ec-side {{
  margin: 14px 0 14px 14px;
  padding: 18px 16px;
  background: rgba(255,255,255,.92);
  border-radius: 14px;
  box-shadow: 0 18px 55px rgba(0,0,0,.20);
}}
.ec-logo {{
  font-size: 36px;
  font-weight: 800;
  color: #6b7a7a;
  margin: 0 0 6px 0;
}}
.ec-logo span {{ color: #c9ad78; }}
.ec-mini {{ color:#6f7d7d; font-size: 13px; margin-bottom: 12px; }}

.ec-nav button {{
  width: 100%;
  border-radius: 14px !important;
  font-weight: 800 !important;
}}
/* CTA Reserva destacada */
.ec-cta button {{
  background: #c9ad78 !important;
  color: #1b1f24 !important;
}}
/* Tarjeta principal */
.ec-main {{
  margin: 18px 18px 18px 0;
  background: rgba(255,255,255,.86);
  border-radius: 16px;
  box-shadow: 0 18px 55px rgba(0,0,0,.18);
  padding: 22px 24px;
  min-height: calc(100vh - 50px);
}}
.ec-h1 {{
  font-size: 44px;
  font-weight: 900;
  margin: 0 0 6px 0;
  color: #2c3238;
}}
.ec-sub {{
  color: #5c676f;
  margin: 0 0 14px 0;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------
# SIDEBAR (pestañas arriba a la izquierda)
# ---------------------------
with st.sidebar:
    st.markdown('<div class="ec-side">', unsafe_allow_html=True)
    st.markdown('<div class="ec-logo">Espai<span>Calma</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="ec-mini">MVP · reserva per hores</div>', unsafe_allow_html=True)

    # Idiomas (arriba)
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("CAT", use_container_width=True):
            st.session_state.lang = "CAT"
    with c2:
        if st.button("ESP", use_container_width=True):
            st.session_state.lang = "ESP"
    with c3:
        if st.button("ENG", use_container_width=True):
            st.session_state.lang = "ENG"

    st.divider()

    lang = st.session_state.lang
    t = TXT[lang]

    # Menú (arriba-izquierda)
    st.markdown('<div class="ec-nav">', unsafe_allow_html=True)
    st.button("🏠 Inici", use_container_width=True, on_click=go, args=("Inici",))
    st.button("🌿 " + t["spaces"], use_container_width=True, on_click=go, args=("Espais",))
    st.button("❓ " + t["faqs"], use_container_width=True, on_click=go, args=("FAQs",))
    st.button("ℹ️ " + t["about"], use_container_width=True, on_click=go, args=("Sobre",))
    st.button("✉️ " + t["contact"], use_container_width=True, on_click=go, args=("Contacte",))

    st.markdown('<div class="ec-cta">', unsafe_allow_html=True)
    st.button("🗓️ " + t["booking"], use_container_width=True, on_click=go, args=("Reserva",))
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# MAIN
# ---------------------------
lang = st.session_state.lang
t = TXT[lang]
page = st.session_state.page

st.markdown('<div class="ec-main">', unsafe_allow_html=True)

# Header
if page == "Inici":
    st.markdown(f'<div class="ec-h1">{t["welcome"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)
    st.info(t["mvp"])
    st.write(
        "• Wi-Fi estable\n• Silenci real\n• Taula + cadira ergonòmica\n• Reserva ràpida"
        if lang == "CAT"
        else "• Wi-Fi estable\n• Silencio real\n• Mesa + silla ergonómica\n• Reserva rápida"
        if lang == "ESP"
        else "• Stable Wi-Fi\n• Real quiet\n• Desk + ergonomic chair\n• Fast booking"
    )

elif page == "Espais":
    st.markdown(f'<div class="ec-h1">{t["spaces"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["spaces"]}: {t["subtitle"]}</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)
    with a:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=70",
                 caption="Sala privada (1)")
        st.caption("Wi-Fi • Silenci • Endolls" if lang != "ENG" else "Wi-Fi • Quiet • Outlets")
    with b:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=70",
                 caption="Sala petita (2)")
        st.caption("Ideal per reunions" if lang == "CAT" else "Ideal para reuniones" if lang == "ESP" else "Great for meetings")
    with c:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=70",
                 caption="Llum natural" if lang == "CAT" else "Luz natural" if lang == "ESP" else "Natural light")
        st.caption("Ventilació • Confort" if lang == "CAT" else "Ventilación • Confort" if lang == "ESP" else "Ventilation • Comfort")

    st.subheader(t["pricing"])
    st.write(
        "• 3 € / hora\n• 30 € / mes (accés il·limitat a certs espais)"
        if lang == "CAT"
        else "• 3 € / hora\n• 30 € / mes (acceso ilimitado a ciertos espacios)"
        if lang == "ESP"
        else "• 3 € / hour\n• 30 € / month (unlimited access to selected spaces)"
    )

elif page == "FAQs":
    st.markdown(f'<div class="ec-h1">{t["faqs"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["mvp"]}</div>', unsafe_allow_html=True)

    with st.expander(t["faq1"]):
        st.write(t["faq1a"])
    with st.expander(t["faq2"]):
        st.write(t["faq2a"])
    with st.expander(t["faq3"]):
        st.write(t["faq3a"])

elif page == "Sobre":
    st.markdown(f'<div class="ec-h1">{t["about"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)
    st.write(t["about1"])
    st.write(t["about2"])

elif page == "Contacte":
    st.markdown(f'<div class="ec-h1">{t["contact"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["subtitle"]}</div>', unsafe_allow_html=True)

    with st.form("contact_form"):
        st.text_input(t["name"])
        st.text_input("Email")
        st.text_area(t["msg"])
        sent = st.form_submit_button(t["send"])
    if sent:
        st.success(t["sent"])

elif page == "Reserva":
    st.markdown(f'<div class="ec-h1">{t["booking"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{t["mvp"]}</div>', unsafe_allow_html=True)

    with st.form("booking_form"):
        loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
        sp = st.selectbox(t["space"], ["Sala privada (1)", "Sala petita (2)", "Llum natural"])
        st.date_input(t["dt"], value=date.today())
        h = st.slider(t["hours"], 1, 8, 2)
        price_per_hour = 3
        st.write(f'{t["price"]}: **{h * price_per_hour} €** ({price_per_hour} €/hora)' if lang != "ENG"
                 else f'{t["price"]}: **{h * price_per_hour} €** ({price_per_hour} €/hour)')
        ok = st.form_submit_button(t["confirm"])

    if ok:
        st.success(t["ok"])
        st.info(t["info"])

st.markdown("</div>", unsafe_allow_html=True)

