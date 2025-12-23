import streamlit as st
from datetime import date

st.set_page_config(page_title="EspaiCalma", page_icon="🧘", layout="wide")

# ---------------------------
# CONFIG / ESTADO
# ---------------------------
PAGES = ["inici", "espais", "faqs", "sobre", "contacte", "reserva"]
LANGS = ["CAT", "ESP", "ENG"]

def qp_get(key, default=None):
    try:
        return st.query_params.get(key, default)
    except Exception:
        return default

def qp_set(**kwargs):
    try:
        st.query_params.update(kwargs)
    except Exception:
        pass

if "page" not in st.session_state:
    st.session_state.page = qp_get("page", "inici")
if "lang" not in st.session_state:
    st.session_state.lang = qp_get("lang", "CAT")

# normaliza
st.session_state.page = st.session_state.page if st.session_state.page in PAGES else "inici"
st.session_state.lang = st.session_state.lang if st.session_state.lang in LANGS else "CAT"

def navigate(page=None, lang=None):
    if page:
        st.session_state.page = page
    if lang:
        st.session_state.lang = lang
    qp_set(page=st.session_state.page, lang=st.session_state.lang)

# ---------------------------
# TEXTOS (simple)
# ---------------------------
TXT = {
    "CAT": {
        "brand": "Espai<span>Calma</span>",
        "inici": ("Benvingut/da a EspaiCalma",
                 "Espais tranquils i còmodes per estudiar o treballar, reservables per hores des d’una app o web.",
                 "MVP: demo de navegació + simulació de reserva (sense pagament real)."),
        "espais": ("Espais i Serveis", "Tria l’espai que millor s’adapta a tu."),
        "faqs": ("FAQs", "Respostes ràpides als dubtes més freqüents."),
        "sobre": ("Sobre Nosaltres", "EspaiCalma neix per facilitar concentració, productivitat i benestar."),
        "contacte": ("Contacte", "Envia’ns un missatge i et respondrem."),
        "reserva": ("Reserva", "Simula una reserva (MVP). Sense pagament real."),
        "menu": {
            "inici": "🏠  Inici",
            "espais": "🌿  Espais i Serveis",
            "faqs": "❓  FAQs",
            "sobre": "ℹ️  Sobre Nosaltres",
            "contacte": "✉️  Contacte",
            "reserva": "🗓️  Reserva",
        },
        "pricing": "Tarifes",
        "send": "Enviar",
        "ok": "✅ Reserva simulada (demo).",
        "msg_sent": "Missatge enviat (demo).",
    },
    "ESP": {
        "brand": "Espai<span>Calma</span>",
        "inici": ("Bienvenido/a a EspaiCalma",
                 "Espacios tranquilos y cómodos para estudiar o trabajar, reservables por horas desde una app o web.",
                 "MVP: demo de navegación + simulación de reserva (sin pago real)."),
        "espais": ("Espacios y Servicios", "Elige el espacio que mejor se adapte a ti."),
        "faqs": ("FAQs", "Respuestas rápidas a las dudas más frecuentes."),
        "sobre": ("Sobre Nosotros", "EspaiCalma nace para mejorar concentración, productividad y bienestar."),
        "contacte": ("Contacto", "Envíanos un mensaje y te respondemos."),
        "reserva": ("Reserva", "Simula una reserva (MVP). Sin pago real."),
        "menu": {
            "inici": "🏠  Inicio",
            "espais": "🌿  Espacios y Servicios",
            "faqs": "❓  FAQs",
            "sobre": "ℹ️  Sobre Nosotros",
            "contacte": "✉️  Contacto",
            "reserva": "🗓️  Reserva",
        },
        "pricing": "Tarifas",
        "send": "Enviar",
        "ok": "✅ Reserva simulada (demo).",
        "msg_sent": "Mensaje enviado (demo).",
    },
    "ENG": {
        "brand": "Espai<span>Calma</span>",
        "inici": ("Welcome to EspaiCalma",
                 "Quiet, comfortable spaces to study or work, bookable by the hour from an app or web.",
                 "MVP: navigation demo + booking simulation (no real payment)."),
        "espais": ("Spaces & Services", "Pick the space that fits you best."),
        "faqs": ("FAQs", "Quick answers to common questions."),
        "sobre": ("About Us", "EspaiCalma helps people focus, be productive, and feel calm."),
        "contacte": ("Contact", "Send us a message and we’ll get back to you."),
        "reserva": ("Booking", "Simulate a booking (MVP). No real payment."),
        "menu": {
            "inici": "🏠  Home",
            "espais": "🌿  Spaces & Services",
            "faqs": "❓  FAQs",
            "sobre": "ℹ️  About Us",
            "contacte": "✉️  Contact",
            "reserva": "🗓️  Booking",
        },
        "pricing": "Pricing",
        "send": "Send",
        "ok": "✅ Booking simulated (demo).",
        "msg_sent": "Message sent (demo).",
    }
}

lang = st.session_state.lang
t = TXT[lang]

# ---------------------------
# CSS + LAYOUT (HTML)
# ---------------------------
BG = "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=2400&q=70"

st.markdown(
    f"""
<style>
/* Ocultar UI de Streamlit */
header, footer {{ visibility: hidden; }}
#MainMenu {{ visibility: hidden; }}

/* Fondo */
.stApp {{
  background:
    linear-gradient(rgba(0,0,0,.34), rgba(0,0,0,.34)),
    url("{BG}");
  background-size: cover;
  background-position: center;
}}

/* Hacemos el contenido ancho */
.block-container {{
  padding-top: 1.25rem;
  padding-bottom: 1.25rem;
}}

/* Grid principal */
.ec-wrap {{
  display: grid;
  grid-template-columns: 330px 1fr;
  gap: 230px;
  align-items: start;
  max-width: 15000px;
  margin: 0 auto;
}}

/* Panel lateral */
.ec-panel {{
  background: rgba(255,255,255,.92);
  border-radius: 18px;
  box-shadow: 0 30px 80px rgba(0,0,0,.25);
  overflow: hidden;
}}
.ec-panel-inner {{
  padding: 30px 25px 25px 25px;
}}
.ec-brand {{
  font-size: 60px;
  font-weight: 600;
  color: #6b7a7a;
  line-height: 1;
  margin-bottom: 18px;
}}
.ec-brand span {{ color: #c9ad78; }}

/* Botones menú */
.ec-btn {{
  width: 100%;
  border: 0;
  background: #2b2f35;
  color: #fff;
  padding: 20px 20px;
  border-radius: 20px;
  font-weight: 800;
  font-size: 25px;
  text-align: left;
  margin: 18px 0;
  cursor: pointer;
  opacity: .100;
}}
.ec-btn:hover {{ opacity: 1; }}

.ec-btn.secondary {{
  background: #2b2f35;
}}
.ec-btn.active {{
  outline: 3px solid rgba(201,173,120,.45);
}}

.ec-cta {{
  width: 100%;
  border: 0;
  background: #ea5a53;
  color: #fff;
  padding: 16px 14px;
  border-radius: 14px;
  font-weight: 900;
  font-size: 20px;
  text-align: center;
  margin: 16px 0 8px 0;
  cursor: pointer;
}}
.ec-cta:hover {{ filter: brightness(.98); }}

/* Idiomas */
.ec-lang {{
  display: flex;
  gap: 12px;
  margin: 14px 0 6px 0;
}}
.ec-pill {{
  flex: 1;
  border: 0;
  background: rgba(0,0,0,.08);
  color: #2b2f35;
  padding: 10px 0;
  border-radius: 12px;
  font-weight: 900;
  cursor: pointer;
}}
.ec-pill.active {{
  background: rgba(43,47,53,.92);
  color: #fff;
}}

/* Social */
.ec-social {{
  display:flex;
  gap: 10px;
  margin-top: 10px;
}}
.ec-ico {{
  width: 36px;
  height: 36px;
  border-radius: 12px;
  background: rgba(0,0,0,.07);
  display:flex;
  align-items:center;
  justify-content:center;
  text-decoration:none;
  color: #2b2f35;
  font-weight: 900;
}}
.ec-ico:hover {{ background: rgba(201,173,120,.22); }}

/* Main card */
.ec-main {{
  background: rgba(255,255,255,.88);
  border-radius: 18px;
  box-shadow: 0 18px 55px rgba(0,0,0,.22);
  padding: 26px 28px;
  min-height: 640px;
}}
.ec-h1 {{
  font-size: 44px;
  font-weight: 950;
  margin: 0 0 8px 0;
  color: #1f252b;
}}
.ec-sub {{
  margin: 0 0 18px 0;
  color: #55626d;
  font-size: 16px;
}}
.ec-chip {{
  display: inline-block;
  background: rgba(43,47,53,.10);
  color: #2b2f35;
  padding: 10px 12px;
  border-radius: 12px;
  font-weight: 800;
  margin: 6px 0 16px 0;
}}
</style>
""",
    unsafe_allow_html=True
)

# ---------------------------
# HTML del menú (con forms)
# ---------------------------
def menu_button(label, page_key, active=False, cta=False):
    cls = "ec-cta" if cta else ("ec-btn active" if active else "ec-btn secondary")
    return f"""
<form action="" method="get">
  <input type="hidden" name="page" value="{page_key}">
  <input type="hidden" name="lang" value="{st.session_state.lang}">
  <button class="{cls}" type="submit">{label}</button>
</form>
"""

def lang_button(code, active=False):
    cls = "ec-pill active" if active else "ec-pill"
    return f"""
<form action="" method="get" style="flex:1;">
  <input type="hidden" name="page" value="{st.session_state.page}">
  <input type="hidden" name="lang" value="{code}">
  <button class="{cls}" type="submit">{code}</button>
</form>
"""

# Actualiza estado desde query_params (por si viniste desde un click HTML)
st.session_state.page = qp_get("page", st.session_state.page)
st.session_state.lang = qp_get("lang", st.session_state.lang)
st.session_state.page = st.session_state.page if st.session_state.page in PAGES else "inici"
st.session_state.lang = st.session_state.lang if st.session_state.lang in LANGS else "CAT"
lang = st.session_state.lang
t = TXT[lang]

# ---------------------------
# RENDER (una sola “pantalla”)
# ---------------------------
st.markdown('<div class="ec-wrap">', unsafe_allow_html=True)

# PANEL IZQUIERDO (HTML)
left_html = f"""
<div class="ec-panel">
  <div class="ec-panel-inner">
    <div class="ec-brand">{t["brand"]}</div>

    <div class="ec-lang">
      {lang_button("CAT", st.session_state.lang=="CAT")}
      {lang_button("ESP", st.session_state.lang=="ESP")}
      {lang_button("ENG", st.session_state.lang=="ENG")}
    </div>

    {menu_button(t["menu"]["inici"], "inici", active=st.session_state.page=="inici")}
    {menu_button(t["menu"]["espais"], "espais", active=st.session_state.page=="espais")}
    {menu_button(t["menu"]["faqs"], "faqs", active=st.session_state.page=="faqs")}
    {menu_button(t["menu"]["sobre"], "sobre", active=st.session_state.page=="sobre")}
    {menu_button(t["menu"]["contacte"], "contacte", active=st.session_state.page=="contacte")}

    {menu_button(t["menu"]["reserva"], "reserva", active=st.session_state.page=="reserva", cta=True)}

    <div class="ec-social">
      <a class="ec-ico" href="https://instagram.com" target="_blank" title="Instagram">IG</a>
      <a class="ec-ico" href="https://x.com" target="_blank" title="X">X</a>
      <a class="ec-ico" href="https://linkedin.com" target="_blank" title="LinkedIn">in</a>
    </div>
  </div>
</div>
"""
st.markdown(left_html, unsafe_allow_html=True)

# MAIN (Streamlit normal dentro de card HTML)
st.markdown('<div class="ec-main">', unsafe_allow_html=True)

page = st.session_state.page

if page == "inici":
    h1, sub, chip = t["inici"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-chip">{chip}</div>', unsafe_allow_html=True)

    st.write(
        "• Wi-Fi estable\n• Silenci real\n• Taula + cadira ergonòmica\n• Reserva ràpida"
        if lang == "CAT"
        else "• Wi-Fi estable\n• Silencio real\n• Mesa + silla ergonómica\n• Reserva rápida"
        if lang == "ESP"
        else "• Stable Wi-Fi\n• Real quiet\n• Desk + ergonomic chair\n• Fast booking"
    )

elif page == "espais":
    h1, sub = t["espais"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=900&q=70",
                 caption="Sala privada (1)")
        st.caption("Wi-Fi • Silenci • Endolls" if lang != "ENG" else "Wi-Fi • Quiet • Outlets")
    with c2:
        st.image("https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=70",
                 caption="Sala petita (2)")
        st.caption("Ideal per reunions" if lang == "CAT" else "Ideal para reuniones" if lang == "ESP" else "Great for meetings")
    with c3:
        st.image("https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=900&q=70",
                 caption="Llum natural" if lang == "CAT" else "Luz natural" if lang == "ESP" else "Natural light")
        st.caption("Ventilació • Confort" if lang == "CAT" else "Ventilación • Confort" if lang == "ESP" else "Ventilation • Comfort")

    st.subheader(t["pricing"])
    st.write("• 3 € / hora\n• 30 € / mes" if lang != "ENG" else "• 3 € / hour\n• 30 € / month")

elif page == "faqs":
    h1, sub = t["faqs"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)

    with st.expander("Com funciona la reserva?" if lang=="CAT" else "¿Cómo funciona la reserva?" if lang=="ESP" else "How does booking work?"):
        st.write("Selecciona ubicació, data i hores i confirma (demo)." if lang=="CAT"
                 else "Selecciona ubicación, fecha y horas y confirma (demo)." if lang=="ESP"
                 else "Pick location, date and hours, then confirm (demo).")
    with st.expander("Hi ha horaris nocturns?" if lang=="CAT" else "¿Hay horarios nocturnos?" if lang=="ESP" else "Do you offer night hours?"):
        st.write("En pilot, es poden ampliar en períodes d’exàmens." if lang=="CAT"
                 else "En piloto, se pueden ampliar en periodos de exámenes." if lang=="ESP"
                 else "During the pilot, hours can be extended in exam periods.")
    with st.expander("Què inclou l’espai?" if lang=="CAT" else "¿Qué incluye el espacio?" if lang=="ESP" else "What's included?"):
        st.write("Wi-Fi, taula, cadira, endolls i silenci." if lang=="CAT"
                 else "Wi-Fi, mesa, silla, enchufes y silencio." if lang=="ESP"
                 else "Wi-Fi, desk, chair, outlets and quiet.")

elif page == "sobre":
    h1, sub = t["sobre"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)
    st.write(
        "Projecte orientat a estudiants i joves professionals que necessiten concentració fora de casa."
        if lang == "CAT"
        else "Proyecto orientado a estudiantes y jóvenes profesionales que necesitan concentración fuera de casa."
        if lang == "ESP"
        else "A project for students and young professionals who need focus outside home."
    )

elif page == "contacte":
    h1, sub = t["contacte"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)

    with st.form("contact_form"):
        st.text_input("Nom" if lang=="CAT" else "Nombre" if lang=="ESP" else "Name")
        st.text_input("Email")
        st.text_area("Missatge" if lang=="CAT" else "Mensaje" if lang=="ESP" else "Message")
        sent = st.form_submit_button(t["send"])
    if sent:
        st.success(t["msg_sent"])

elif page == "reserva":
    h1, sub = t["reserva"]
    st.markdown(f'<div class="ec-h1">{h1}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="ec-sub">{sub}</div>', unsafe_allow_html=True)

    with st.form("booking_form"):
        loc = st.selectbox("Ubicació" if lang!="ENG" else "Location",
                           ["Eixample", "Gràcia", "Sants", "Poblenou"])
        sp = st.selectbox("Espai" if lang=="CAT" else "Espacio" if lang=="ESP" else "Space",
                          ["Sala privada (1)", "Sala petita (2)", "Llum natural"])
        st.date_input("Data" if lang!="ENG" else "Date", value=date.today())
        h = st.slider("Hores" if lang!="ENG" else "Hours", 1, 8, 2)
        price = 3
        st.markdown(f"**Preu estimat:** {h*price} € ({price} €/hora)" if lang!="ENG"
                    else f"**Estimated price:** {h*price} € ({price} €/hour)")
        ok = st.form_submit_button("Confirmar reserva" if lang!="ENG" else "Confirm booking")
    if ok:
        st.success(t["ok"])

st.markdown("</div>", unsafe_allow_html=True)  # ec-main
st.markdown("</div>", unsafe_allow_html=True)  # ec-wrap
 app.py — EspaiCalma (Streamlit) DESDE CERO con HTML/CSS (mockup) + letras grandes y alto contraste
# Ejecuta: streamlit run app.py


