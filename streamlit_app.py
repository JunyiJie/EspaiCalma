# app.py — EspaiCalma (Streamlit) con pestañas visibles (sin depender del sidebar)
# Ejecuta: streamlit run app.py

import streamlit as st
from datetime import date

st.set_page_config(
    page_title="EspaiCalma",
    page_icon="🧘",
    layout="wide",
)

# ---------------------------
# ESTADO
# ---------------------------
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"

# ---------------------------
# TEXTOS (i18n)
# ---------------------------
T = {
    "CAT": {
        "Inici": ("Benvingut/da a EspaiCalma", "Espais tranquils i còmodes per estudiar o treballar, reservables per hores."),
        "Espais i Serveis": ("Espais i Serveis", "Tria l’espai que millor s’adapta a tu."),
        "FAQs": ("FAQs", "Respostes ràpides als dubtes més freqüents."),
        "Sobre Nosaltres": ("Sobre Nosaltres", "EspaiCalma neix per facilitar concentració, productivitat i benestar."),
        "Contacte": ("Contacte", "Envia’ns un missatge i et respondrem."),
        "Reserva": ("Reserva", "Simula una reserva (MVP). Sense pagament real."),
    },
    "ESP": {
        "Inici": ("Bienvenido/a a EspaiCalma", "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas."),
        "Espais i Serveis": ("Espacios y Servicios", "Elige el espacio que mejor se adapte a ti."),
        "FAQs": ("FAQs", "Respuestas rápidas a las dudas más frecuentes."),
        "Sobre Nosaltres": ("Sobre Nosotros", "EspaiCalma nace para mejorar concentración, productividad y bienestar."),
        "Contacte": ("Contacto", "Envíanos un mensaje y te respondemos."),
        "Reserva": ("Reserva", "Simula una reserva (MVP). Sin pago real."),
    },
    "ENG": {
        "Inici": ("Welcome to EspaiCalma", "Quiet, comfortable spaces to study or work, bookable by the hour."),
        "Espais i Serveis": ("Spaces & Services", "Pick the space that fits you best."),
        "FAQs": ("FAQs", "Quick answers to common questions."),
        "Sobre Nosaltres": ("About Us", "EspaiCalma helps people focus, be productive, and feel calm."),
        "Contacte": ("Contact", "Send us a message and we’ll get back to you."),
        "Reserva": ("Booking", "Simulate a booking (MVP). No real payment."),
    },
}

# ---------------------------
# CSS (fondo + tarjeta + tabs)
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(
    f"""
<style>
/* Fondo */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,.32), rgba(0,0,0,.32)),
    url("{BG}");
  background-size: cover;
  background-position: center;
}}

/* Ocultar chrome */
header {{visibility:hidden;}}
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}

/* Contenedor principal centrado */
.ec-wrap {{
  max-width: 1200px;
  margin: 36px auto;
  padding: 0 18px;
}}

/* Tarjeta */
.ec-card {{
  background: rgba(255,255,255,.86);
  border-radius: 16px;
  box-shadow: 0 18px 55px rgba(0,0,0,.18);
  padding: 26px 28px;
}}

/* Títulos */
.ec-h1 {{
  font-size: 44px;
  font-weight: 800;
  color: #ffffff;
  margin: 0 0 6px 0;
  text-shadow: 0 6px 26px rgba(0,0,0,.35);
}}
.ec-sub {{
  color: rgba(255,255,255,.92);
  font-size: 18px;
  margin-bottom: 18px;
  text-shadow: 0 6px 26px rgba(0,0,0,.35);
}}

/* Tabs: que parezcan botones */
.stTabs [data-baseweb="tab-list"] {{
  gap: 10px;
}}
.stTabs [data-baseweb="tab"] {{
  background: rgba(0,0,0,.35);
  border-radius: 12px;
  padding: 10px 14px;
  color: white;
  border: 1px solid rgba(255,255,255,.12);
}}
.stTabs [aria-selected="true"] {{
  background: rgba(201,173,120,.95);
  color: #1b1f24;
  border: 1px solid rgba(0,0,0,.06);
  font-weight: 800;
}}

/* Botón Reserva dentro de la sección (CTA) */
.ec-cta button {{
  background: #c94f4f !important;
  color: white !important;
  border-radius: 14px !important;
  border: none !important;
  padding: 12px 16px !important;
  font-weight: 800 !important;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------
# HEADER (como tu mockup)
# ---------------------------
lang = st.session_state.lang

st.markdown('<div class="ec-wrap">', unsafe_allow_html=True)

# selector de idioma arriba (como los 3 botones)
c_lang1, c_lang2, c_lang3, _ = st.columns([1, 1, 1, 6])
with c_lang1:
    if st.button("CAT", use_container_width=True):
        st.session_state.lang = "CAT"
with c_lang2:
    if st.button("ESP", use_container_width=True):
        st.session_state.lang = "ESP"
with c_lang3:
    if st.button("ENG", use_container_width=True):
        st.session_state.lang = "ENG"

lang = st.session_state.lang

title, subtitle = T[lang]["Inici"]  # título de bienvenida fijo (como landing)
st.markdown(f'<div class="ec-h1">{title}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="ec-sub">{subtitle}</div>', unsafe_allow_html=True)

# ---------------------------
# NAV (PESTAÑAS ARRIBA: SIEMPRE visibles)
# ---------------------------
tabs = st.tabs(["🏠 Inici", "🌿 Espais i Serveis", "❓ FAQs", "ℹ️ Sobre Nosaltres", "✉️ Contacte", "🗓️ Reserva"])

# ---------------------------
# TAB 1: Inici
# ---------------------------
with tabs[0]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.info("MVP: demo de navegació + simulació de reserva (sense pagament real)." if lang == "CAT"
            else "MVP: demo de navegación + simulación de reserva (sin pago real)." if lang == "ESP"
            else "MVP: navigation demo + booking simulation (no real payment).")

    st.write(
        "EspaiCalma ofereix espais silenciosos amb Wi-Fi, taula i cadira ergonòmica. Reserva ràpida i flexible."
        if lang == "CAT"
        else "EspaiCalma ofrece espacios silenciosos con Wi-Fi, mesa y silla ergonómica. Reserva rápida y flexible."
        if lang == "ESP"
        else "EspaiCalma offers quiet spaces with Wi-Fi, desk and ergonomic chair. Fast, flexible booking."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# TAB 2: Espais i Serveis
# ---------------------------
with tabs[1]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader("Espais (exemple)" if lang != "ENG" else "Spaces (sample)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=70",
                 caption="Sala privada (1)")
        st.caption("Wi-Fi • Silenci • Endolls")
    with c2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=70",
                 caption="Sala petita (2)")
        st.caption("Ideal per reunions" if lang == "CAT" else "Ideal para reuniones" if lang == "ESP" else "Great for meetings")
    with c3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=70",
                 caption="Llum natural" if lang == "CAT" else "Luz natural" if lang == "ESP" else "Natural light")
        st.caption("Ventilació • Confort" if lang == "CAT" else "Ventilación • Confort" if lang == "ESP" else "Ventilation • Comfort")

    st.subheader("Tarifes" if lang != "ENG" else "Pricing")
    st.write("• 3 € / hora\n\n• 30 € / mes (accés il·limitat a certs espais)"
             if lang == "CAT"
             else "• 3 € / hora\n\n• 30 € / mes (acceso ilimitado a ciertos espacios)"
             if lang == "ESP"
             else "• 3 € / hour\n\n• 30 € / month (unlimited access to selected spaces)")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# TAB 3: FAQs
# ---------------------------
with tabs[2]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    with st.expander("Com funciona la reserva?" if lang == "CAT" else "¿Cómo funciona la reserva?" if lang == "ESP" else "How does booking work?"):
        st.write("Selecciona ubicació, data i hores. Confirma i rep una confirmació (demo)."
                 if lang != "ENG" else "Choose location, date and hours. Confirm and get a demo confirmation.")
    with st.expander("Hi ha horaris nocturns?" if lang == "CAT" else "¿Hay horarios nocturnos?" if lang == "ESP" else "Do you offer night hours?"):
        st.write("En fase pilot es poden ampliar horaris en períodes d’exàmens segons demanda."
                 if lang == "CAT" else
                 "En fase piloto se pueden ampliar horarios en periodos de exámenes según demanda."
                 if lang == "ESP" else
                 "During the pilot, we can extend hours in exam periods depending on demand.")
    with st.expander("Què inclou l’espai?" if lang == "CAT" else "¿Qué incluye el espacio?" if lang == "ESP" else "What's included?"):
        st.write("Wi-Fi, taula, cadira ergonòmica, endolls i ambient tranquil."
                 if lang == "CAT" else
                 "Wi-Fi, mesa, silla ergonómica, enchufes y ambiente tranquilo."
                 if lang == "ESP" else
                 "Wi-Fi, desk, ergonomic chair, power outlets, and a quiet atmosphere.")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# TAB 4: Sobre Nosaltres
# ---------------------------
with tabs[3]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.write(
        "Projecte orientat a estudiants i joves professionals que necessiten concentració fora de casa."
        if lang == "CAT"
        else "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración fuera de casa."
        if lang == "ESP"
        else "A project for students and young professionals who need focus outside home."
    )
    st.write(
        "Objectiu: reduir soroll i distraccions i facilitar una reserva simple i ràpida."
        if lang == "CAT"
        else "Objetivo: reducir ruido y distracciones y facilitar una reserva simple y rápida."
        if lang == "ESP"
        else "Goal: reduce noise/distractions and make booking simple and fast."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# TAB 5: Contacte
# ---------------------------
with tabs[4]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    with st.form("contact"):
        st.text_input("Nom" if lang == "CAT" else "Nombre" if lang == "ESP" else "Name")
        st.text_input("Email")
        st.text_area("Missatge" if lang == "CAT" else "Mensaje" if lang == "ESP" else "Message")
        sent = st.form_submit_button("Enviar" if lang != "ENG" else "Send")
    if sent:
        st.success("Missatge enviat (demo)." if lang == "CAT" else "Mensaje enviado (demo)." if lang == "ESP" else "Message sent (demo).")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------
# TAB 6: Reserva
# ---------------------------
with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    with st.form("booking"):
        loc = st.selectbox("Ubicació" if lang == "CAT" else "Ubicación" if lang == "ESP" else "Location",
                           ["Eixample", "Gràcia", "Sants", "Poblenou"])
        sp = st.selectbox("Espai" if lang == "CAT" else "Espacio" if lang == "ESP" else "Space",
                          ["Sala privada (1)", "Sala petita (2)", "Llum natural"])
        st.date_input("Data" if lang == "CAT" else "Fecha" if lang == "ESP" else "Date",
                      value=date.today())
        h = st.slider("Hores" if lang == "CAT" else "Horas" if lang == "ESP" else "Hours",
                      1, 8, 2)
        price = 3
        st.write((f"Preu estimat: **{h*price} €** ({price} €/hora)" if lang == "CAT"
                 else f"Precio estimado: **{h*price} €** ({price} €/hora)" if lang == "ESP"
                 else f"Estimated price: **{h*price} €** ({price} €/hour)"))
        ok = st.form_submit_button("Confirmar reserva" if lang != "ENG" else "Confirm booking")

    if ok:
        st.success("✅ Reserva simulada (demo).")
        st.info("Aquesta acció pot comptar com a ‘reserva de prova’ per a les mètriques de l’experiment."
                if lang == "CAT"
                else "Esta acción puede contar como ‘reserva de prueba’ para las métricas del experimento."
                if lang == "ESP"
                else "This action can count as a ‘test booking’ for your experiment metrics.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

