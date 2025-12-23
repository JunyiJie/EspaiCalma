with tabs[5]:
    st.markdown('<div class="ec-card">', unsafe_allow_html=True)
    st.subheader(t["booking_title"])
    
    # Aviso de los 10 minutos con estilo de alerta
    st.warning(t["cancel_warning"])

    with st.form("booking_form"):
        st.markdown(f"#### 1. {t['name']} & {t['contact_title']}")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            nom = st.text_input(t["name"], placeholder="Joan")
            cognom = st.text_input(t["surname"], placeholder="García")
        with c_p2:
            email = st.text_input(t["email"], placeholder="exemple@correu.com")
            tlf = st.text_input(t["phone"], placeholder="+34 600 000 000")
            
        st.write("---")
        st.markdown(f"#### 2. {t['space']} & {t['hours']}")
        
        c_s1, c_s2 = st.columns(2)
        with c_s1:
            loc = st.selectbox(t["loc"], ["Eixample", "Gràcia", "Sants", "Poblenou"])
            sp = st.selectbox(t["space"], ["Sala privada", "Sala petita", "Llum natural"])
        with c_s2:
            st.date_input(t["date"], value=date.today())
            # Al mover este slider, el valor de 'h' cambia y el cálculo de abajo se actualiza
            h = st.slider(t["hours"], 1, 12, 2)

        # CÁLCULO DINÁMICO DEL PRECIO
        precio_hora = 3
        total = h * precio_hora
        
        # Mostramos el precio con un formato grande y destacado
        st.markdown(
            f"""
            <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #d1d5db;">
                <span style="font-size: 1.2rem; color: #4b5563;">{t['price']}</span><br>
                <span style="font-size: 2.5rem; font-weight: 800; color: #1f2937;">{total} €</span><br>
                <span style="font-size: 0.9rem; color: #6b7280;">({h} hores x {precio_hora}€/h)</span>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.write("") # Espaciado
        submit = st.form_submit_button(t["booking_confirm"], use_container_width=True)

    if submit:
        if nom and cognom and email and tlf:
            st.success(f"{t['booking_ok']} - Gràcies, {nom}!")
            st.balloons()
        else:
            st.error("Si us plau, emplena tots els camps obligatoris per continuar.")
            
    st.markdown("</div>", unsafe_allow_html=True)
