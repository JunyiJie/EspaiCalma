# app.py  — EspaiCalma (Streamlit) estilo igual al mockup
# Ejecuta:  streamlit run app.py

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

def go(page: str):
    st.session_state.page = page

# ---------------------------
# CSS (sidebar + fondo + look)
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2000&q=70"

st.markdown(
    f"""
<style>
/* Fondo como foto */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,.28), rgba(0,0,0,.28)),
    url("{BG}");
  background-size: cover;
  background-position: center;
}}

/* Ocultar chrome de Streamlit */
header {{visibility:hidden;}}
#MainMenu {{visibility:hidden;}}
footer {{visibility:hidden;}}

/* Sidebar blanco tipo tarjeta */
[data-testid="stSidebar"] {{
  background: transparent !important;
}}
[data-testid="stSidebar"] > div:first-child {{
  padding: 0 !important;
}}
.ec-side {{
  width: 320px;
  margin: 22px 0 22px 22px;
  background: rgba(255,255,255,.92);
  border-radius: 10px;
  box-shadow: 0 18px 55px rgba(0,0,0,.20);
  overflow: hidden;
}}
.ec-side-inner {{
  padding: 22px 18px 18px 18px;
}}

/* Brand */
.ec-brand {{
  display:flex;
  gap:12px;
  align-items:center;
  padding: 2px 2px 10px 2px;
}}
.ec-title {{
  font-size: 44px;
  font-weight: 500;
  color: #6b7a7a;
  line-height: 1;
  letter-spacing: .2px;
}}
.ec-title span {{
  color: #c9ad78;
}}

/* Menú */
.ec-nav {{
  margin-top: 8px;
}}
.ec-btn > button {{
  width: 100%;
  border: none !important;
  background: transparent !important;
  padding: 12px 10px !important;
  border-radius: 10px !important;
  text-align: left !important;
  color: #5b6a6a !important;
  font-size: 18px !important;
}}
.ec-btn > button:hover {{
  background: rgba(201,173,120,.14) !important;
}}
.ec-btn > button:focus {{
  box-shadow: none !important;
  outline: none !important;
}}

/* CTA Reserva (barra dorada) */
.ec-cta > button {{
  width: 100%;
  border: none !important;
  padding: 14px 10px !important;
  border-radius: 0 !important;
  background: #c9ad78 !important;
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 18px !important;
  text-align: left !important;
}}
.ec-cta > button:hover {{
  filter: brightness(.98);
}}
.ec-divider {{
  height: 1px;
  background: rgba(0,0,0,.06);
  margin: 8px 0;
}}
.ec-cta-wrap {{
  margin: 10px -18px 0 -18px;
  border-top: 1px solid rgba(0,0,0,.06);
  border-bottom: 1px solid rgba(0,0,0,.06);
}}

/* Idiomas */
.ec-lang {{
  display:flex;
  gap:14px;
  padding: 14px 4px 8px 4px;
  color: #8b9898;
  font-size: 12px;
  letter-spacing: .7px;
}}
.ec-lang button {{
  background: none;
  border: none;
  cursor: pointer;
  color: inherit;
  font: inherit;
  padding: 4px 0;
  border-bottom: 2px solid transparent;
}}
.ec-lang button.active {{
  color: #6b7a7a;
  border-bottom-color: #c9ad78;
}}

/* Social */
.ec-social {{
  display:flex;
  gap:12px;
  padding: 8px 4px 4px 4px;
  align-items:center;
}}
.ec-social a {{
  width:30px;
  height:30px;
  border-radius: 8px;
  display:flex;
  align-items:center;
  justify-content:center;
  background: rgba(0,0,0,.04);
  text-decoration:none;
  color: #6f7d7d;
  font-weight: 700;
}}
.ec-social a:hover {{
  background: rgba(201,173,120,.18);
}}

/* Contenido principal como tarjeta transparente */
.ec-main {{
  margin: 22px 22px 22px 0;
  background: rgba(255,255,255,.86);
  border-radius: 12px;
  box-shadow: 0 18px 55px rgba(0,0,0,.16);
  padding: 24px 26px;
  min-height: calc(100vh - 44px);
}}
.ec-h1 {{
  font-size: 34px;
  font-weight: 650;
  color: #4f5e5e;
  margin: 0 0 8px 0;
}}
.ec-muted {{
  color:#6f7d7d;
}}

/* Mejorar spacing en widgets */
.stTextInput, .stSelectbox, .stDateInput, .stSlider, .stTextArea {{
  margin-top: .25rem;
}}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------
# ICONOS (SVG simples)
# ---------------------------
def svg(icon: str) -> str:
    # icon: home, leaf, faq, info, mail, cal
    icons = {
        "home": """<svg width="18" height="18" viewBox="0 0 24 24" fill="#6f7d7d"><path d="M12 3l9 8h-3v10h-5v-6H11v6H6V11H3l9-8z"/></svg>""",
        "leaf": """<svg width="18" height="18" viewBox="0 0 24 24" fill="#6f7d7d"><path d="M17 8c-4.5 0-8 3.5-8 8 0 1.2.3 2.3.7 3.3C6.4 18 4 15 4 11 4 6.6 7.6 3 12 3c2 0 3.9.8 5.3 2.1C16.6 6 16.9 7 17 8z"/><path d="M20 10c0 6-4 11-11 11 6-3 8-7 9-11h2z"/></svg>""",
        "faq":  """<svg width="18" height="18" viewBox="0 0 24 24" fill="#6f7d7d"><path d="M12 2C6.5 2 2 6 2 11c0 3 1.7 5.7 4.3 7.4L6 22l4.1-2.3c.6.1 1.3.2 1.9.2 5.5 0 10-4 10-9s-4.5-9-10-9zm1 15h-2v-2h2v2zm2.1-7.5-.9.9c-.7.7-1.2 1.3-1.2 2.6h-2v-.5c0-1 .4-1.9 1.1-2.6l1.2-1.2c.3-.3.6-.8.6-1.3 0-1-.8-1.8-1.8-1.8s-1.8.8-1.8 1.8H8c0-2.1 1.7-3.8 3.8-3.8S15.6 6.9 15.6 9c0 .8-.3 1.5-.5 1.5z"/></svg>""",
        "info": """<svg width="18" height="18" viewBox="0 0 24 24" fill="#6f7d7d"><path d="M11 17h2v-6h-2v6zm0-8h2V7h-2v2zm1-7C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"/></svg>""",
        "mail": """<svg width="18" height="18" viewBox="0 0 24 24" fill="#6f7d7d"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4-8 5-8-5V6l8 5 8-5v2z"/></svg>""",
        "cal":  """<svg width="18" height="18" viewBox="0 0 24 24" fill="#ffffff"><path d="M7 2h2v2h6V2h2v2h3c1.1 0 2 .9 2 2v16c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2h3V2zm14 8H3v12h18V10z"/></svg>""",
    }
    return icons[icon]

# ---------------------------
# SIDEBAR (HTML container + botones)
# ---------------------------
with st.sidebar:
    st.markdown('<div class="ec-side"><div class="ec-side-inner">', unsafe_allow_html=True)

    # Brand
    st.markdown(
        f"""
<div class="ec-brand">
  <svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true">
    <path d="M12 26 L32 12 L52 26" stroke="#6f7d7d" stroke-width="3" fill="none" opacity="0.65"/>
    <rect x="29.5" y="16" width="5" height="5" rx="1" fill="#6f7d7d" opacity="0.65"/>
    <path d="M18 38c5-9 9-10 14-10s9 1 14 10c-3 8-9 12-14 12s-11-4-14-12z" fill="#c9ad78" opacity="0.95"/>
    <path d="M32 30c-4 0-7 3-7 7 0 4 3 7 7 7s7-3 7-7c0-4-3-7-7-7z" fill="#fff" opacity="0.35"/>
  </svg>
  <div class="ec-title">Espai<span>Calma</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Nav buttons
    def nav_button(label, icon_key, target):
        # Use streamlit button but we fake icon with emoji fallback in label
        # for reliability; we also show SVG to the left via markdown line above.
        cols = st.columns([0.12, 0.88])
        with cols[0]:
            st.markdown(svg(icon_key), unsafe_allow_html=True)
        with cols[1]:
            st.markdown('<div class="ec-btn">', unsafe_allow_html=True)
            st.button(label, key=f"nav_{target}", on_click=go, args=(target,))
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="ec-nav">', unsafe_allow_html=True)
    nav_button("Inici", "home", "Inici")
    nav_button("Espais i Serveis", "leaf", "Espais i Serveis")
    nav_button("FAQs", "faq", "FAQs")
    nav_button("Sobre Nosaltres", "info", "Sobre Nosaltres")
    nav_button("Contacte", "mail", "Contacte")
    st.markdown("</div>", unsafe_allow_html=True)

    # CTA Reserva
    st.markdown('<div class="ec-cta-wrap">', unsafe_allow_html=True)
    cta_cols = st.columns([0.12, 0.88])
    with cta_cols[0]:
        st.markdown(svg("cal"), unsafe_allow_html=True)
    with cta_cols[1]:
        st.markdown('<div class="ec-cta">', unsafe_allow_html=True)
        st.button("Reserva", key="nav_Reserva", on_click=go, args=("Reserva",))
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Lang selector (HTML buttons)
    def lang_btn(code):
        active = "active" if st.session_state.lang == code else ""
        st.markdown(
            f"""
<form action="" method="post">
  <button class="{active}" type="button" onclick="window.location.hash='{code}'">{code}</button>
</form>
""",
            unsafe_allow_html=True,
        )

    # Real lang buttons using Streamlit (simple & reliable)
    st.markdown('<div class="ec-lang">', unsafe_allow_html=True)
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("CAT", use_container_width=True):
            st.session_state.lang = "CAT"
    with b2:
        if st.button("ESP", use_container_width=True):
            st.session_state.lang = "ESP"
    with b3:
        if st.button("ENG", use_container_width=True):
            st.session_state.lang = "ENG"
    st.markdown("</div>", unsafe_allow_html=True)

    # Social
    st.markdown(
        """
<div class="ec-social">
  <a href="https://instagram.com" target="_blank" title="Instagram">▢</a>
  <a href="https://x.com" target="_blank" title="X">X</a>
  <a href="https://linkedin.com" target="_blank" title="LinkedIn">in</a>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown("</div></div>", unsafe_allow_html=True)

# ---------------------------
# CONTENIDO (texto por idioma)
# ---------------------------
T = {
    "CAT": {
        "Inici": ("Benvingut/da", "Espais tranquils i còmodes per estudiar o treballar, reservables per hores."),
        "Espais i Serveis": ("Espais i Serveis", "Tria l’espai que millor s’adapta a tu."),
        "FAQs": ("FAQs", "Respostes ràpides als dubtes més freqüents."),
        "Sobre Nosaltres": ("Sobre Nosaltres", "EspaiCalma neix per facilitar concentració, productivitat i benestar."),
        "Contacte": ("Contacte", "Envia’ns un missatge i et respondrem."),
        "Reserva": ("Reserva", "Simula una reserva (MVP). Sense pagament real."),
    },
    "ESP": {
        "Inici": ("Bienvenido/a", "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas."),
        "Espais i Serveis": ("Espacios y Servicios", "Elige el espacio que mejor se adapte a ti."),
        "FAQs": ("FAQs", "Respuestas rápidas a las dudas más frecuentes."),
        "Sobre Nosaltres": ("Sobre Nosotros", "EspaiCalma nace para mejorar concentración, productividad y bienestar."),
        "Contacte": ("Contacto", "Envíanos un mensaje y te respondemos."),
        "Reserva": ("Reserva", "Simula una reserva (MVP). Sin pago real."),
    },
    "ENG": {
        "Inici": ("Welcome", "Quiet, comfortable spaces to study or work, bookable by the hour."),
        "Espais i Serveis": ("Spaces & Services", "Pick the space that fits you best."),
        "FAQs": ("FAQs", "Quick answers to common questions."),
        "Sobre Nosaltres": ("About Us", "EspaiCalma helps people focus, be productive, and feel calm."),
        "Contacte": ("Contact", "Send us a message and we’ll get back to you."),
        "Reserva": ("Booking", "Simulate a booking (MVP). No real payment."),
    },
}

# ---------------------------
# MAIN WRAPPER
# ---------------------------
page = st.session_state.page
lang = st.session_state.lang
title, subtitle = T[lang][page]

st.markdown(f'<div class="ec-main"><div class="ec-h1">{title}</div><div class="ec-muted">{subtitle}</div><br/>', unsafe_allow_html=True)

# ---------------------------
# PÁGINAS
# ---------------------------
if page == "Inici":
    st.write(
        "EspaiCalma ofereix espais silenciosos amb Wi-Fi, taula i cadira ergonòmica. Reserva ràpida i flexible."
        if lang == "CAT"
        else "EspaiCalma ofrece espacios silenciosos con Wi-Fi, mesa y silla ergonómica. Reserva rápida y flexible."
        if lang == "ESP"
        else "EspaiCalma offers quiet spaces with Wi-Fi, desk and ergonomic chair. Fast, flexible booking."
    )
    st.info("MVP: navegació + simulació de reserva per validar interès real (mètriques accionables).")

elif page == "Espais i Serveis":
    st.subheader("Espais (exemple)" if lang != "ENG" else "Spaces (sample)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=70", caption="Sala privada (1)")
        st.caption("Wi-Fi • Silenci • Endolls")
    with c2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=70", caption="Sala petita (2)")
        st.caption("Ideal per reunions")
    with c3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=70", caption="Llum natural")
        st.caption("Ventilació • Confort")

    st.subheader("Tarifes" if lang != "ENG" else "Pricing")
    st.write("• 3 € / hora\n\n• 30 € / mes (accés il·limitat a certs espais)")

elif page == "FAQs":
    with st.expander("Com funciona la reserva?" if lang == "CAT" else "¿Cómo funciona la reserva?" if lang == "ESP" else "How does booking work?"):
        st.write("Selecciona ubicació, data i hores. Confirma i rep una confirmació (demo).")
    with st.expander("Hi ha horaris nocturns?" if lang == "CAT" else "¿Hay horarios nocturnos?" if lang == "ESP" else "Do you offer night hours?"):
        st.write("En fase pilot es poden ampliar horaris en períodes d’exàmens segons demanda.")
    with st.expander("Què inclou l’espai?" if lang == "CAT" else "¿Qué incluye el espacio?" if lang == "ESP" else "What's included?"):
        st.write("Wi-Fi, taula, cadira ergonòmica, endolls i ambient tranquil.")

elif page == "Sobre Nosaltres":
    st.write(
        "Projecte orientat a estudiants i joves professionals que necessiten concentració fora de casa."
        if lang == "CAT"
        else "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración fuera de casa."
        if lang == "ESP"
        else "A project for students and young professionals who need focus outside home."
    )
    st.write("Objectiu: reduir soroll i distraccions i facilitar una reserva simple i ràpida.")

elif page == "Contacte":
    with st.form("contact"):
        st.text_input("Nom" if lang == "CAT" else "Nombre" if lang == "ESP" else "Name")
        st.text_input("Email")
        st.text_area("Missatge" if lang == "CAT" else "Mensaje" if lang == "ESP" else "Message")
        sent = st.form_submit_button("Enviar" if lang != "ENG" else "Send")
    if sent:
        st.success("Missatge enviat (demo).")

elif page == "Reserva":
    with st.form("booking"):
        loc = st.selectbox("Ubicació" if lang != "ENG" else "Location", ["Eixample", "Gràcia", "Sants", "Poblenou"])
        sp = st.selectbox("Espai" if lang == "CAT" else "Espacio" if lang == "ESP" else "Space",
                          ["Sala privada (1)", "Sala petita (2)", "Llum natural"])
        d = st.date_input("Data" if lang != "ENG" else "Date", value=date.today())
        h = st.slider("Hores" if lang != "ENG" else "Hours", 1, 8, 2)
        price = 3
        st.write(f"Preu estimat: **{h*price} €** ({price} €/hora)")
        ok = st.form_submit_button("Confirmar reserva" if lang != "ENG" else "Confirm booking")
    if ok:
        st.success(f"✅ Reserva simulada: {loc} · {sp} · {h}h · {h*price}€ (demo)")
        st.info("Aquesta acció pot comptar com a ‘reserva de prova’ per a les mètriques de l’experiment.")

st.markdown("</div>", unsafe_allow_html=True)
