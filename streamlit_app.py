# app.py  (Streamlit)
# Ejecuta:  streamlit run app.py
import streamlit as st

st.set_page_config(page_title="EspaiCalma MVP", page_icon="🧘", layout="wide")

# --- Estilos (sidebar como en la imagen) ---
st.markdown(
    """
<style>
/* Fondo (tipo foto desenfocada) */
.stApp{
  background:
    linear-gradient(rgba(0,0,0,.25),rgba(0,0,0,.25)),
    url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=1800&q=70");
  background-size: cover;
  background-position: center;
}

/* Sidebar panel */
[data-testid="stSidebar"]{
  background: #ffffff !important;
}
[data-testid="stSidebar"] > div:first-child{
  padding-top: 24px;
}

/* Quitar header/menú */
header{visibility:hidden;}
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}

/* Botón/CTA estilo "Reserva" */
.ec-cta{
  display:flex; align-items:center; gap:10px;
  padding:12px 14px;
  background:#c9ad78;
  color:white;
  border-radius:8px;
  font-weight:600;
  text-decoration:none;
}
.ec-cta:hover{ filter:brightness(0.98); }

/* Links del menú */
.ec-item{
  display:flex; align-items:center; gap:10px;
  padding:10px 8px;
  color:#5b6a6a;
  text-decoration:none;
  border-radius:8px;
}
.ec-item:hover{ background: rgba(201,173,120,.14); }

/* Título marca */
.ec-brand{
  font-size:38px;
  font-weight:500;
  color:#6b7a7a;
  line-height:1;
}
.ec-brand span{ color:#c9ad78; }

/* Iconos pequeños */
.ec-ico{ width:18px; height:18px; fill:#6f7d7d; }
.ec-social a{
  display:inline-flex; align-items:center; justify-content:center;
  width:30px; height:30px; border-radius:8px;
  background: rgba(0,0,0,.04);
  margin-right:10px;
  text-decoration:none;
}
.ec-social a:hover{ background: rgba(201,173,120,.18); }
</style>
""",
    unsafe_allow_html=True,
)

# --- Estado de navegación ---
if "page" not in st.session_state:
    st.session_state.page = "Inici"
if "lang" not in st.session_state:
    st.session_state.lang = "CAT"


def nav(to_page: str):
    st.session_state.page = to_page


# --- Sidebar (como el mockup) ---
with st.sidebar:
    # Logo + marca (SVG simple)
    st.markdown(
        """
<div style="display:flex; align-items:center; gap:12px; padding:0 8px 10px 8px;">
  <svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true">
    <path d="M12 26 L32 12 L52 26 V52 H12 Z" fill="#6f7d7d" opacity="0.25"/>
    <path d="M18 28 L32 18 L46 28 V50 H18 Z" fill="#6f7d7d" opacity="0.18"/>
    <path d="M32 31c-6 0-12 4-12 10 0 5 4 9 12 9s12-4 12-9c0-6-6-10-12-10z" fill="#c9ad78" opacity="0.9"/>
    <circle cx="32" cy="26" r="3" fill="#c9ad78"/>
  </svg>
  <div class="ec-brand">Espai<span>Calma</span></div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Menú (botones Streamlit para cambiar página)
    st.button("🏠  Inici", use_container_width=True, on_click=nav, args=("Inici",))
    st.button("🌿  Espais i Serveis", use_container_width=True, on_click=nav, args=("Espais i Serveis",))
    st.button("❓  FAQs", use_container_width=True, on_click=nav, args=("FAQs",))
    st.button("ℹ️  Sobre Nosaltres", use_container_width=True, on_click=nav, args=("Sobre Nosaltres",))
    st.button("✉️  Contacte", use_container_width=True, on_click=nav, args=("Contacte",))

    st.markdown("---")

    # CTA Reserva
    st.button("📅  Reserva", type="primary", use_container_width=True, on_click=nav, args=("Reserva",))

    st.markdown("---")

    # Idiomas
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

    st.markdown("---")

    # Social (simple)
    st.markdown(
        """
<div class="ec-social" style="padding:4px 6px 0 6px;">
  <a href="https://instagram.com" target="_blank" title="Instagram">📷</a>
  <a href="https://twitter.com" target="_blank" title="X / Twitter">🐦</a>
  <a href="https://linkedin.com" target="_blank" title="LinkedIn">in</a>
</div>
""",
        unsafe_allow_html=True,
    )

# --- Contenido principal (páginas) ---
page = st.session_state.page
lang = st.session_state.lang

titles = {
    "CAT": {
        "Inici": "Benvingut/da a EspaiCalma",
        "Espais i Serveis": "Espais i Serveis",
        "FAQs": "Preguntes freqüents",
        "Sobre Nosaltres": "Sobre Nosaltres",
        "Contacte": "Contacte",
        "Reserva": "Reserva un espai",
    },
    "ESP": {
        "Inici": "Bienvenido/a a EspaiCalma",
        "Espais i Serveis": "Espacios y Servicios",
        "FAQs": "Preguntas frecuentes",
        "Sobre Nosaltres": "Sobre nosotros",
        "Contacte": "Contacto",
        "Reserva": "Reserva un espacio",
    },
    "ENG": {
        "Inici": "Welcome to EspaiCalma",
        "Espais i Serveis": "Spaces & Services",
        "FAQs": "FAQs",
        "Sobre Nosaltres": "About us",
        "Contacte": "Contact",
        "Reserva": "Book a space",
    },
}

st.title(titles[lang][page])

if page == "Inici":
    st.write(
        "Espais tranquils i còmodes per estudiar o treballar, reservables per hores des d’una app o web."
        if lang == "CAT"
        else "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas desde una app o web."
        if lang == "ESP"
        else "Quiet, comfortable spaces to study or work, bookable by the hour via app or web."
    )
    st.info("MVP: demo de navegació + simulació de reserva (sense pagament real).")

elif page == "Espais i Serveis":
    st.subheader("Exemples d’espais")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=800&q=70", caption="Sala privada (1 persona)")
        st.caption("Wi-Fi • Silenci • Taula • Endolls")
    with c2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=70", caption="Sala petita (2 persones)")
        st.caption("Ideal per reunions o treball en parella")
    with c3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=800&q=70", caption="Espai llum natural")
        st.caption("Ventilació • Confort • Concentració")

    st.subheader("Tarifes (exemple)")
    st.write("• 3 € / hora\n\n• 30 € / mes (accés il·limitat a certs espais)")

elif page == "FAQs":
    with st.expander("Com funciona la reserva?"):
        st.write("Selecciona ubicació, dia i hora. Confirma i rep la confirmació al correu.")
    with st.expander("Hi ha horaris nocturns?"):
        st.write("En fase pilot s’ampliaran horaris en períodes d’exàmens segons demanda.")
    with st.expander("Què inclou l’espai?"):
        st.write("Wi-Fi, taula, cadira ergonòmica, endolls i ambient silenciós.")

elif page == "Sobre Nosaltres":
    st.write(
        "EspaiCalma neix per resoldre la manca d’espais tranquils per a estudiants i joves professionals."
        if lang == "CAT"
        else "EspaiCalma nace para resolver la falta de espacios tranquilos para estudiantes y jóvenes profesionales."
        if lang == "ESP"
        else "EspaiCalma was created to solve the lack of quiet spaces for students and young professionals."
    )
    st.write("Objectiu: facilitar concentració, productivitat i benestar.")

elif page == "Contacte":
    st.write("Deixa’ns el teu missatge i et respondrem.")
    with st.form("contact_form"):
        name = st.text_input("Nom" if lang == "CAT" else "Nombre" if lang == "ESP" else "Name")
        email = st.text_input("Email")
        msg = st.text_area("Missatge" if lang == "CAT" else "Mensaje" if lang == "ESP" else "Message")
        ok = st.form_submit_button("Enviar" if lang != "ENG" else "Send")
    if ok:
        st.success("Missatge enviat (demo). Gràcies!")

elif page == "Reserva":
    st.write("Simula una reserva (MVP). No es farà cap cobrament real.")
    with st.form("booking_form"):
        location = st.selectbox(
            "Ubicació" if lang == "CAT" else "Ubicación" if lang == "ESP" else "Location",
            ["Eixample", "Gràcia", "Sants", "Poblenou"],
        )
        space = st.selectbox(
            "Tipus d’espai" if lang == "CAT" else "Tipo de espacio" if lang == "ESP" else "Space type",
            ["Sala privada (1)", "Sala petita (2)", "Espai llum natural"],
        )
        date = st.date_input("Data" if lang != "ENG" else "Date")
        hours = st.slider("Hores" if lang != "ENG" else "Hours", 1, 8, 2)
        price_per_hour = 3
        total = hours * price_per_hour
        st.write(f"Preu estimat: **{total} €** ({price_per_hour} €/hora)")
        submit = st.form_submit_button("Confirmar reserva" if lang == "CAT" else "Confirmar reserva" if lang == "ESP" else "Confirm booking")

    if submit:
        st.success(f"Reserva simulada ✅  {location} · {space} · {hours}h · {total}€ (demo)")
        st.info("Aquesta acció es podria comptar com a ‘reserva de prova’ per a les mètriques del vostre experiment.")
